def print_even_index_chars(user_string):
  """
  This function takes a string as input and prints the characters present 
  at even indexes (0, 2, 4, etc.).
  Args:
      user_string: The string entered by the user.
  """
  for i in range(0, len(user_string), 2):
    print(user_string[i], end="")
user_string = input("Enter a string: ")
print_even_index_chars(user_string)
