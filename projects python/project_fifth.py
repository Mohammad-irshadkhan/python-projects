def compare_first_last(numbers):
  """
  This function checks if the first and last elements of a list are equal.
  Args:
      numbers: A list of numbers.
  Returns:
      A string indicating if the first and last numbers are the same ("first and last numbers are same") 
      or not ("NOT same").
  """
  if not numbers:  
    return "List is empty"
  if numbers[0] == numbers[-1]:
    return "First and last numbers are same"
  else:
    return "NOT same"
my_list = [1, 2, 3, 1]
result = compare_first_last(my_list)
print(result) 
my_listy = [4, 5, 6]
result = compare_first_last(my_listy)
print(result)  
my_liste = []
result = compare_first_last(my_liste)
print(result)  
