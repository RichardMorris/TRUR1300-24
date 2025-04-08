# class representing a floating point number in 8 bits
# with 1 sign bit, 4 exponent bits, and 3 mantissa bits
import math

class FP8:
    __slots__ = ('bits')
    def __init__(self, rep: int):
        self.bits = rep

    def get_bits(self) -> int:
        return self.bits

    def get_sign(self) -> int:
        """Gets the sign bit of the floating point number.
        Returns 0 for positive numbers and 1 for negative numbers.
        """
        return (self.bits >> 7) & 0b1
    
    def get_sign_val(self) -> int:
        """Gets the sign value of the floating point number.
        Returns 1 for positive numbers and -1 for negative numbers.
        """
        if self.bits & 0b10000000 == 0:
            return 1
        else:
            return -1
    
    def get_exponent(self) -> int:
        return (self.bits >> 3) & 0b1111
    
    def get_mantissa(self) -> int:
        return self.bits & 0b111
    
    def get_int_rep(self) -> tuple[int,int,int]:
        """A rep (sign, mantissa, exponent) such that
        val == sign * mantissa * 2**exponent
        With an integer mantissa, exponent in the range [-9, 5]
        and sign +1 for positive and -1 for negative.
        """
        exp = self.get_exponent()
        if exp == 0:
            return (self.get_sign_val(),self.get_mantissa(),-9)
        else:
            return (self.get_sign_val(),self.get_mantissa() + 0b1000, exp - 10)

    def get_fp_rep(self) -> tuple[int,float,int]:
        """Gets floating point rep (sign, mantissa, exponent) such that
        val == sign * mantissa * 2**exponent
        where the mantissa is floating point number 1.xxxxx for normalised numbers
        and 0.xxxxx for subnormal numbers.
        The exponent is in the range [-6, 7]
        and sign +1 for positive and -1 for negative.
        """
        if self.get_exponent() == 0:
            return (self.get_sign_val(), self.get_mantissa() / 8.0, -6)
        else:
            return (self.get_sign_val(), 
                    1 + (self.get_mantissa() / 8.0), 
                    self.get_exponent() - 7)
    
    def is_infinite(self) -> bool:
        #return self.get_exponent() == 0b1111 and self.get_mantissa() == 0
        #return self.bits & 0b01111000 == 0b01111000 and self.get_mantissa() == 0
        return self.bits & 0b01111111 == 0b01111000
    
    def is_nan(self) -> bool:
        #return self.get_exponent() == 0b1111 and self.get_mantissa() != 0
        return self.bits & 0b01111000 == 0b01111000 and self.get_mantissa() != 0
    
    def is_zero(self) -> bool:
        #return self.get_exponent() == 0 and self.get_mantissa() == 0
        return self.bits & 0b01111111 == 0

    def is_subnormal(self) -> bool:
        return self.get_exponent() == 0 and self.get_mantissa() != 0
    
        
    def to_float(self) -> float:
        if self.is_infinite():
            return float('inf') if self.get_sign() == 0 else float('-inf')
        if self.is_nan():
            return float('nan')
        
        (signval,mantissa,exponent) = self.get_fp_rep()
        return signval * (mantissa) * (2 ** exponent)
    
    def __repr__(self) -> str:
        if self.is_nan():
            return "NaN"
        if self.is_infinite():
            return "Inf" if self.get_sign() == 0 else "-Inf"
        (signval,mantissa,exponent) = self.get_fp_rep()
        sign = "+" if signval == 1 else "-"
        return f"{sign}{mantissa:.3f}*2^{exponent}"
    
    def __str__(self) -> str:
        return self.to_float().__str__()
    
    def __eq__(self, other) -> bool:
        if isinstance(other, FP8):
            if self.is_nan() or other.is_nan():
                return False
            if self.is_zero() and other.is_zero():
                return True
            return self.get_bits() == other.get_bits()
        return False
    
    @classmethod
    def from_float(cls, value: float) -> 'FP8':
        if math.isnan(value):
            return NaN1  # NaN representation
        if value == float('inf'):
            return PosInf  # Positive infinity representation
        if value == float('-inf'):
            return NegInf  # Negative infinity representation
        if value == 0.0:
            if math.copysign(1, value) < 0:
                return NegZero  # Negative zero representation
            else:
                return PosZero  # Zero representation

        sign = 1 if value < 0 else 0
        abs_value = abs(value)
        
        exponent = int(math.floor(math.log2(abs_value))) + 7 
        if exponent <= 0:
            exponent = 0  # Subnormal numbers have exponent 0 and mantissa != 0
            mantissa = int((abs_value / (2 ** (exponent - 6))) * 8) & 0b111
        elif exponent >= 15:
            return PosInf if sign == 0 else NegInf  # Overflow to infinity
        else:
            mantissa = int((abs_value / (2 ** (exponent - 7))) * 8) & 0b111
        
        return FP8((sign << 7) | (exponent << 3) | mantissa)
    
    def __add__(self, other):
        sf = self.bits & 0b01111000 == 0b01111000
        of = other.bits & 0b01111000 == 0b01111000
        if sf: # self is special
            if self.bits & 0b00000111 != 0: # NaN
                return self # NaN
            # self is inf    
            if of:
                if other.bits & 0b00000111 != 0: # NaN
                    return other # NaN
                # other is inf
                samesign = self.get_sign_val() == other.get_sign_val()
                return self if samesign else NaN1
            # other is number
            return self
        elif of: # self is number, other is special
            return other # either inf or NaN


        # now numbers 
        (ss,sm,se) = self.get_int_rep() # val == ss * sm * 2^se
        (os,om,oe) = other.get_int_rep()

        exp = min(se,oe)
        # give both mantissa the same scale
        sn = (sm <<(se - exp))
        on = (om <<(oe - exp))
        if ss == -1:
            sn = -sn
        if os == -1:
            on = -on
        # add mantissas
        sum = sn + on

        # extract sign
        (sign, sum) = (0, sum) if sum > 0 else (1, -sum)

        return self.from_rep(sign, sum, exp)
        
    def __sub__(self, other):
        if self.is_nan() or other.is_nan():
            return NaN1
        val = -other  # flip sign bit
        return self.__add__(val)

    def __neg__(self):
        val = FP8(self.get_bits() ^ 0b10000000)  # flip sign bit
        return val

    def __mul__(self, other):
        sf = self.bits & 0b01111000 == 0b01111000
        of = other.bits & 0b01111000 == 0b01111000
        if sf: # self is special
            if self.bits & 0b00000111 != 0: # NaN
                return self # NaN
            if of:
                if other.bits & 0b00000111 != 0: # NaN
                    return other # NaN
            # self is inf
            if other.is_zero():
                return NaN1
            sign = self.get_sign_val() != other.get_sign_val()
            return PosInf if sign == 0 else NegInf
        elif of: # other is special
            if other.bits & 0b00000111 != 0:
                return other # NaN
            if self.is_zero():
                return NaN1
            sign = self.get_sign_val() != other.get_sign_val()
            return PosInf if sign == 0 else NegInf
                                
        # now numbers 
        (ss,sm,se) = self.get_int_rep() # val == ss * sm * 2^se
        (os,om,oe) = other.get_int_rep() # val == os * om * 2^oe
        # multiply mantissas and add exponents
        mul = sm * om
        exp = se + oe
        return self.from_rep(ss != os, mul, exp)

    def __truediv__(self, other):
        return NotImplementedError("Division is not implemented for FP8.")

    def __float__(self) -> float:
        """Convert the FP8 instance to a float.
        """
        return self.to_float()  
    
    def from_rep(self, sign: int, val: int, exp: int) -> 'FP8':
        """Constructs a FP8 instance from the sign, mantissa and exponent.
        Where sign is 0 for positive and 1 for negative.
        The mantissa is an integer
        and the exponent is an integer in the range [-9, 5].
        So val == (-1)^sign * mantissa * 2**exponent
        """
        # rescale so mantissa is in range [0,16) i.e. 0b0000 to 0b1111
        while val >= 16:
            val >>= 1
            exp += 1
        # rescale very small number so exponent in range
        if exp < -9:
            val >>= (-9-exp)
            exp = -9
        # unless subnormal rescale to get mantissa in range [8,16) i.e. 0b1000 to 0b1111
        while val < 8 and exp > -9:
            val <<= 1
            exp -= 1
        # check for overflow
        if exp >=5:
            return PosInf if sign == 0 else NegInf
        if exp < -9:
            return PosZero if sign == 0 else NegZero
        # adjust exponent for subnormal numbers
        if exp == -9 and val < 8:
                exp = -10
        # construct the byte representation
        byte = (sign << 7) | (exp + 10) << 3 | int(val) & 0b111
        res = FP8(byte)
        return res
      
PosZero= FP8(0b00000000)  # Positive 0 representation
PosMin = FP8(0b00000001)  # Minimum non zero positive
PosOne = FP8(0b00111000)  # Positive 1 representation
PosMax = FP8(0b01110111)  # Max Positive number representation
PosInf = FP8(0b01111000)  # Positive infinity representation
NaN1   = FP8(0b01111001)  # NaN representation
NaN2   = FP8(0b01111010)  # NaN representation
NaN3   = FP8(0b01111011)  # NaN representation
NaN4   = FP8(0b01111100)  # NaN representation
NaN5   = FP8(0b01111101)  # NaN representation
NaN6   = FP8(0b01111110)  # NaN representation
NaN7   = FP8(0b01111111)  # NaN representation

NegZero= FP8(0b10000000)  # Negative 0 representation
NegOne = FP8(0b10111000)  # Negative 1 representation
NegMin = FP8(0b00000001)  # Minimum non zero positive
NegMax = FP8(0b01110111)  # Positive max representation
NegInf = FP8(0b11111000)  # Negative infinity representation
NaN9   = FP8(0b11111001)  # NaN representation
NaNA   = FP8(0b11111010)  # NaN representation
NaNB   = FP8(0b11111011)  # NaN representation
NaNC   = FP8(0b11111100)  # NaN representation
NaND   = FP8(0b11111101)  # NaN representation
NaNE   = FP8(0b11111110)  # NaN representation
NaNF   = FP8(0b11111111)  # NaN representation
