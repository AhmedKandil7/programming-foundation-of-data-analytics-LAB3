def reverse_string(input_string):
    return input_string[::-1]

user_input = input("Insert your string: ")

reversed_string = reverse_string(user_input)

print(f"The reversed string is: '{reversed_string}'")
