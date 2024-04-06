def is_palindrome(number):
  """
  This function checks if a given number is a palindrome.
  Args:
      number: The integer to check.
  Returns:
      True if the number is a palindrome, False otherwise.
  """
  original_number = number
  reversed_number = 0
  while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10
  return original_number == reversed_number
number = 121
if is_palindrome(number):
  print(f"{number} is a palindrome number")
else:
  print(f"{number} is not a palindrome number")
number = 545
if is_palindrome(number):
  print(f"{number} is a palindrome number")
else:
  print(f"{number} is not a palindrome number")
number = 1234
if is_palindrome(number):
  print(f"{number} is a palindrome number")
else:
  print(f"{number} is not a palindrome number")
