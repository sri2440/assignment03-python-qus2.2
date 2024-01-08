# string_manipulator.py

def reverse_string(input_str):
    return input_str[::-1]

def count_occurrences(input_str, char):
    return input_str.count(char)

def is_palindrome(input_str):
    cleaned_str = ''.join(char.lower() for char in input_str if char.isalnum())
    return cleaned_str == cleaned_str[::-1]

# main_script_string_manipulation.py
from string_manipulator import reverse_string, count_occurrences, is_palindrome

# Example usage
input_string = "level"
char_to_count = "l"

# Reverse a string
reversed_str = reverse_string(input_string)
print(f"Reversed String: {reversed_str}")

# Count occurrences of a character
occurrences = count_occurrences(input_string, char_to_count)
print(f"Occurrences of '{char_to_count}' in '{input_string}': {occurrences}")

# Check if a string is a palindrome
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")
