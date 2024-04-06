def combine_odd_even(list1, list2):
  """
  This function creates a new list containing odd numbers from the first list 
  and even numbers from the second list.
  Args:
      list1: The first list of numbers.
      list2: The second list of numbers.
  Returns:
      A new list containing odd numbers from list1 and even numbers from list2.
  """
  new_list = []
  for num in list1:
    if num % 2 != 0:  
      new_list.append(num)
  for num in list2:
    if num % 2 == 0: 
      new_list.append(num)
  return new_list
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
new_list = combine_odd_even(list1, list2)
print(new_list)  
