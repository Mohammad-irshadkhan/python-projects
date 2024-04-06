def remove_first_n_chars(text, n):
  """
  This function removes the first n characters from a string and returns 
  a new string containing the remaining characters.
  Args:
      text: The original string.
      n: The number of characters to remove from the beginning.
  Returns:
      A new string with the first n characters removed.
  """
  if n < 0:
    raise ValueError("n must be non-negative")
  return text[n:]
text = "pynative"
new_text = remove_first_n_chars(text, 2)
print(new_text)  # Output: "tive"
