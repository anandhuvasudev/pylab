from palindrome import is_palindrome, longest_palindromic_substring

#test_string = "racer"
#if is_palindrome(test_string):
#   print(f"{test_string} is a palindrome")
#else:
#   print(f"{test_string} is not a palindrome")

input_string =input("Enter a String")
longest_palindrome = longest_palindromic_substring(input_string)
print(f"The longest palindromic substring in \"{input_string}\" is \"{longest_palindrome}\"")
