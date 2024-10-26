def binary_to_int(binary_str):
    return int(binary_str, 2)

binary_str = input("Enter a binary number: ")
result = binary_to_int(binary_str)
print("The integer value is:", result)
