# main class for fp8

import fp8

# main function to test the fp8 module

def main():
    for i in range(0, 255):
        fp8_instance = fp8.FP8(i)
        val = fp8_instance.to_float()
        bin_repr = format(i, '08b')
        bin_repr = bin_repr[0:1] + " " + bin_repr[1:5] + " " + bin_repr[5:]
        print(f"{i}\t{bin_repr}\t{fp8_instance.__repr__()}\t{val}")
        
if __name__ == "__main__":
    main()
