# Test cases for the fp8 module

import unittest
import math
from fp8 import *

class TestFP8(unittest.TestCase):
    
    values = [
        0.0, 0.001953125, 0.00390625, 0.005859375, 0.0078125, 0.009765625, 0.01171875, 0.013671875,
        0.015625, 0.017578125, 0.01953125, 0.021484375, 0.0234375, 0.025390625, 0.02734375, 0.029296875,
        0.03125, 0.03515625, 0.0390625, 0.04296875, 0.046875, 0.05078125, 0.0546875, 0.05859375,
        0.0625, 0.0703125, 0.078125, 0.0859375, 0.09375, 0.1015625, 0.109375, 0.1171875,
        0.125, 0.140625, 0.15625, 0.171875, 0.1875, 0.203125, 0.21875, 0.234375,
        0.25, 0.28125, 0.3125, 0.34375, 0.375, 0.40625, 0.4375, 0.46875,
        0.5, 0.5625, 0.625, 0.6875, 0.75, 0.8125, 0.875, 0.9375,
        1, 1.125, 1.25, 1.375, 1.5, 1.625, 1.75, 1.875,
        2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75,
        4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5,
        8, 9, 10, 11, 12, 13, 14, 15,
        16, 18, 20, 22, 24, 26, 28, 30,
        32, 36, 40, 44, 48, 52, 56, 60,
        64, 72, 80, 88, 96, 104, 112, 120,
        128, 144, 160, 176, 192, 208, 224, 240,
        float("Inf"), float("NaN"), float("NaN"), float("NaN"), 
        float("NaN"), float("NaN"), float("NaN"), float("NaN"),
        -0.0, -0.001953125, -0.00390625, -0.005859375, -0.0078125, -0.009765625, -0.01171875, -0.013671875,
        -0.015625, -0.017578125, -0.01953125, -0.021484375, -0.0234375, -0.025390625, -0.02734375, -0.029296875,
        -0.03125, -0.03515625, -0.0390625, -0.04296875, -0.046875, -0.05078125, -0.0546875, -0.05859375,
        -0.0625, -0.0703125, -0.078125, -0.0859375, -0.09375, -0.1015625, -0.109375, -0.1171875,
        -0.125, -0.140625, -0.15625, -0.171875, -0.1875, -0.203125, -0.21875, -0.234375,
        -0.25, -0.28125, -0.3125, -0.34375, -0.375, -0.40625, -0.4375, -0.46875,
        -0.5, -0.5625, -0.625, -0.6875, -0.75, -0.8125, -0.875, -0.9375,
        -1, -1.125, -1.25, -1.375, -1.5, -1.625, -1.75, -1.875,
        -2, -2.25, -2.5, -2.75, -3, -3.25, -3.5, -3.75,
        -4, -4.5, -5, -5.5, -6, -6.5, -7, -7.5,
        -8, -9, -10, -11, -12, -13, -14, -15,
        -16, -18, -20, -22, -24, -26, -28, -30,
        -32, -36, -40, -44, -48, -52, -56, -60,
        -64, -72, -80, -88, -96, -104, -112, -120,
        -128, -144, -160, -176, -192, -208, -224, -240,
        float("-Inf"), float("NaN"), float("NaN"), float("NaN"), 
        float("NaN"), float("NaN"), float("NaN"), float("NaN") ]

    def test_numbers(self):

        for i in range(0, 255):
            fp8 = FP8(i)
            val = fp8.to_float()
            if math.isnan(self.values[i]):
                self.assertTrue(math.isnan(val))
            else:
                self.assertEqual(val, self.values[i])

    def test_from_float(self):
        for i in range(0, 255):
            selval = self.values[i]
            fp8 = FP8.from_float(selval)
            val = fp8.to_float()
            if math.isnan(self.values[i]):
                self.assertTrue(fp8.is_nan())
                self.assertTrue(math.isnan(val))
            else:
                self.assertEqual(fp8.get_bits(), i)
                self.assertEqual(val, self.values[i])

    def test_from_float_edge_cases(self):
        v255 = 255.9
        f255 = FP8.from_float(v255)
        self.assertFalse(f255.is_infinite())
        self.assertEqual(f255.get_bits(), PosMax.get_bits())
        v256 = 256.0
        f256 = FP8.from_float(v256)
        self.assertTrue(f256.is_infinite())
        self.assertEqual(f256.get_bits(), PosInf.get_bits())
        vbigzero = 1.0/513
        fbigzero = FP8.from_float(vbigzero)
        self.assertEqual(fbigzero.get_bits(), PosZero.get_bits())
        vsmallestpos = 1.0/512
        fsmallestpos = FP8.from_float(vsmallestpos)
        self.assertEqual(fsmallestpos.get_bits(), PosMin.get_bits())

    def test_add(self):
        fp8_1 = FP8(0b00000001)
        fp8_2 = FP8(0b00000010)
        self.assertEqual(fp8_1.to_float(), 0.001953125)
        self.assertEqual(fp8_2.to_float(), 0.00390625)
        result = fp8_1 + fp8_2
        self.assertEqual(result, 0.001953125+0.00390625)