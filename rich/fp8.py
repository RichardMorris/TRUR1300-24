# class representing a floating point number in 8 bits
# with 1 sign bit, 4 exponent bits, and 3 mantissa bits

class FP8:
    def __init__(self, rep: int):
        self.bits = rep

    def get_sign(self) -> int:
        return (self.bits >> 7) & 0b1
    
    def get_exponent(self) -> int:
        return (self.bits >> 3) & 0b1111
    
    def get_mantissa(self) -> int:
        return self.bits & 0b111
    
    def get_bits(self) -> int:
        return self.bits
    
    def is_infinite(self) -> bool:
        return self.get_exponent() == 0b1111 and self.get_mantissa() == 0
    
    def is_nan(self) -> bool:
        return self.get_exponent() == 0b1111 and self.get_mantissa() != 0
    
    def is_zero(self) -> bool:
        return self.get_exponent() == 0 and self.get_mantissa() == 0
    
    def is_subnormal(self) -> bool:
        return self.get_exponent() == 0 and self.get_mantissa() != 0
    
    def get_normalised_mantissa(self) -> int:
        if self.get_exponent() == 0:
            return self.get_mantissa() / 8.0
        else:
            return 1 + (self.get_mantissa() / 8.0)

    def get_normalised_exponent(self) -> int:
        if self.get_exponent() == 0:
            return -6
        else:
            return self.get_exponent() - 7
        
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
    
    def structure_string(self) -> str:
        sign = self.get_sign()
        exponent = self.get_normalised_exponent()
        mantissa = self.get_normalised_mantissa()
        signstr = "-1" if sign else "1"
        return f"{signstr}*{mantissa:.3f}*2^{exponent}"
    
    def __str__(self) -> str:
        return self.to_float().__str__()
    
    def __repr__(self) -> str:
        return self.structure_string()