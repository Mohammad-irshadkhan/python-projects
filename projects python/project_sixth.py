def display_divisible_by_5(numbers):
  """
  This function iterates through a list of numbers and prints only those 
  divisible by 5.
  Args:
      numbers: A list of numbers.
  """
  for number in numbers:
    if number % 5 == 0:
      print(number)
my_list = [10, 12, 15, 20, 22, 25,30,35,40,45]
display_divisible_by_5(my_list)
