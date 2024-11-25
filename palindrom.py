# Function to check if a string is a palindrome
def is_palindrome(string):
    # Remove spaces and convert to lowercase for uniformity
    string = string.replace(" ", "").lower()
    # Check if the string is the same when reversed
    return string == string[::-1]

# Input from the user
input_string = input("Enter a string: ")

# Check and display the result
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome!")
else:
    print(f"'{input_string}' is not a palindrome.")
