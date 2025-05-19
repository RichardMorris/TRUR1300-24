# main class for fp8

from fp8 import FP8

# main function to test the fp8 module

def main():
    print("Values\tBinary\tFP8 Representation\tFloat Value")
    for i in range(0, 255):
        fp8_instance = FP8(i)
        val = fp8_instance.to_float()
        bin_repr = format(i, '08b')
        bin_repr = bin_repr[0:1] + " " + bin_repr[1:5] + " " + bin_repr[5:]
        print(f"{i}\t{bin_repr}\t{fp8_instance.__repr__()}\t{val}")
    
    codes = [0, 1, 8, 48, 56, 64, 112, 119, 120, 121]
    print()
    print("     +      |","".join([FP8(i).__repr__().ljust(12) for i in codes]))
    print("-"*120)
    for i in codes:
        fp8_instance = FP8(i)
        print(fp8_instance.__repr__().ljust(12), end="| ")
        for j in codes:
            fp8_instance2 = FP8(j)
            result = fp8_instance + fp8_instance2
            print(result.__repr__().ljust(12), end="")
        print()
    print()
    print("     *      |","  ".join([FP8(i).__repr__().rjust(11) for i in codes]))
    print("-"*120)
    for i in codes:
        fp8_instance = FP8(i)
        print(fp8_instance.__repr__().rjust(11), end=" | ")
        for j in codes:
            fp8_instance2 = FP8(j)
            result = fp8_instance * fp8_instance2
            print(result.__repr__().rjust(11), end="  ")
        print()

if __name__ == "__main__":
    main()
