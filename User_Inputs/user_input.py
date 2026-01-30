## User input program
user_input = input("Enter the value: ")

#convert user input to string
print("\nOriginal Value:", user_input)
print("Original Data Type:", type(user_input))

#convert string to integer
into_int = user_input
convert_int = sum(ord(chr) for chr in into_int)
print("\nOriginal Value:", convert_int)
print("Original Data Type:", type(convert_int))

# Convert the integer to float
convert_float = float(convert_int)
print("\nConverted Value:", convert_float)
print("Converted Data Type:", type(convert_float))

# Convert the float to complex
convert_complex = complex(convert_int)
print("-" * 20)
print("\nComplex Value:", convert_complex)
print("Complex Data Type:", type(convert_complex))

#convert complex to range
convert_range = range(convert_int)
print("\nRange Value:", convert_range)
print("Range Data Type:", type(convert_range))

#convert range to set
convert_set = set(user_input)
print("\nSet Value:", convert_set)
print("Set Data Type:", type(convert_set))

#convert set to frozenset
convert_frozenset = frozenset(user_input)
print("\nFrozenset Value:", convert_frozenset)
print("Frozenet Data Type:", type(convert_frozenset))

#convert frozenset to boolean
convert_bool = bool(user_input)
print("\nBoolean Value:", convert_bool)
print("boolean Data Type:", type(convert_bool))

#convert boolean to binary code(bits)
convert_bits = bytes(user_input, 'utf-8')
print("\nBytes Value: ", convert_bits)
print("Bytes Type: " ,type(convert_bits))

#convert binary code(bits) to binary array
convert_bitsArray = bytearray(user_input, 'utf-8')
print("\nBytearray Value: ", convert_bitsArray)
print("Bytearray Type: ", type(convert_bits))

#covert binary array to memory view
convert_bitsMemory = memoryview(convert_bits)
print("\nMemoryview: ", convert_bitsMemory)
print("Memoryview Type: ", type(convert_bitsMemory))
