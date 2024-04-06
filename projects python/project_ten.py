def extract_digits_reversed(number):
  """
  This function extracts each digit from an integer in the reverse order 
  and returns a string with the digits separated by spaces.
  Args:
      number: The integer from which to extract digits.

  Returns:
      A string containing the digits of the number in reverse order, 
      separated by spaces.
  """
  digits = ""
  while number > 0:
    digit = number % 10
    digits = str(digit) + " " + digits  
    number //= 10
  return digits.rstrip()  
number = 7536
reversed_digits = extract_digits_reversed(number)
print(reversed_digits) 
