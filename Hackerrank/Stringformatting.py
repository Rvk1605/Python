 # #Python oct()
 # #returns the octal representation of an integer

#  #Python hex()
#  Converts to Integer to Hexadecimal

# Python bin()
# converts integer to binary string


                              ##FORMAT SPECIFIER
# s – strings
# d – decimal integers (base-10)
# f – floating point display
# c – character
# b – binary
# o – octal
# x – hexadecimal with lowercase letters after 9
# X – hexadecimal with uppercase letters after 9
# e – exponent notation

# def print_formatted(number):
#     for i in range(1,number+1):
#         # print(f"{i:d}", end=" ")
#         # print(f"{i:o}", end=" ")
#         # print(f"{i:X}", end=" ")
#         # print(f"{i:b}", end=" ")
#         # print()
def print_formatted(number):
    for i in range(1, number + 1):
        print(f"{i:>3d} {i:>3o} {i:>3X} {i:>3b}")




if __name__ == '__main__':
    n = int(input())
    print_formatted(n)