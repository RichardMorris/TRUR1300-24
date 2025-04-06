# class representing a floating point number in 8 bits
# with 1 sign bit, 4 exponent bits, and 3 mantissa bits
import math

class FP8:
    
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
        if self.get_sign() == 0:
            return 1
        else:
            return -1
    
    def get_exponent(self) -> int:
        return (self.bits >> 3) & 0b1111
    
    def get_mantissa(self) -> int:
        return self.bits & 0b111
    
    def get_extended_mantissa(self) -> int:
        """Gets the extended mantissa value, in the range [0, 16).
        """
        if self.get_exponent() == 0:
            return self.get_mantissa()
        else:
            return self.get_mantissa() + 0b1000

    def get_extended_exponent(self) -> int:
        if self.get_exponent() == 0:
            return -3
        else:
            return self.get_exponent() -10

    def get_normalised_mantissa(self) -> float:
        """Gets floating point rep of the mantissa adjusted for subnormal numbers.
        """
        if self.get_exponent() == 0:
            return self.get_mantissa() / 8.0
        else:
            return 1 + (self.get_mantissa() / 8.0)

    def get_normalised_exponent(self) -> int:
        if self.get_exponent() == 0:
            return -6
        else:
            return self.get_exponent() - 7
    
    def is_infinite(self) -> bool:
        return self.get_exponent() == 0b1111 and self.get_mantissa() == 0
    
    def is_nan(self) -> bool:
        return self.get_exponent() == 0b1111 and self.get_mantissa() != 0
    
    def is_zero(self) -> bool:
        return self.get_exponent() == 0 and self.get_mantissa() == 0
    
    def is_subnormal(self) -> bool:
        return self.get_exponent() == 0 and self.get_mantissa() != 0
    
        
    def to_float(self) -> float:
        if self.is_infinite():
            return float('inf') if self.get_sign() == 0 else float('-inf')
        if self.is_nan():
            return float('nan')
        #if self.is_zero():
        #    sign = self.get_sign()
        #    return float('-0.0') if sign else float('0.0')
        
        sign = self.get_sign()
        exponent_value = self.get_normalised_exponent()
        mantissa_value = self.get_normalised_mantissa()
        return (-1) ** sign * (mantissa_value) * (2 ** exponent_value)
    
    def __repr__(self) -> str:
        if self.is_nan():
            return "NaN"
        if self.is_infinite():
            return "Inf" if self.get_sign() == 0 else "-Inf"
        sign = self.get_sign()
        exponent = self.get_normalised_exponent()
        mantissa = self.get_normalised_mantissa()
        signstr = "-1" if sign else "1"
        return f"{signstr}*{mantissa:.3f}*2^{exponent}"
    
    def __str__(self) -> str:
        return self.to_float().__str__()
    
    def __eq__(self, other) -> bool:
        if isinstance(other, FP8):
            if self.is_nan() and other.is_nan():
                return False
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
        if self.is_nan  () or other.is_nan():
            return NaN1 # NaN representation
        if self.is_zero():
            return other
        if other.is_zero():
            return self
        if self.is_infinite() and other.is_infinite():
            if  self.get_sign() != other.get_sign():
                return NaN1   # NaN representation
            else:
                return self
        if self.is_infinite():
            return self
        if other.is_infinite():
            return other         
        # now numbers 
        sm = self.get_extended_mantissa()
        se = self.get_normalised_exponent()
        om = other.get_extended_mantissa()
        oe = other.get_normalised_exponent()

        exp = min(se,oe)
        # give both mantissa the same scale
        ss = (sm <<(se - exp)) * self.get_sign_val()
        os = (om <<(oe - exp)) * other.get_sign_val()
        # add mantissas
        sum = ss + os
        if sum == 0:
            return PosZero
        # extract sign
        (sign, sum) = (0, sum) if sum > 0 else (1, -sum)
        # rescale so mantissa is in range [0,16)
        while sum >= 16:
            sum >>= 1
            exp += 1
        # unless subnormal resale to get mantissa in range [8,16)
        while exp > -6 and sum < 8:
            sum <<= 1
            exp -= 1
        # check for overflow
        if exp ==8:
            return PosInf if sign == 0 else NegInf
        # adjust exponent for subnormal numbers
        if exp == -6 and sum < 8:
                exp = -7
        # construct the byte representation
        byte = (sign << 7) | (exp + 7) << 3 | int(sum) & 0b111
        res = FP8(byte)
        return res
    
    @classmethod
    def staticValues(cls,rep : int) -> 'FP8':
        return FP8(rep) 
    
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
