previous = None  
for i in range(1, 11):  
  if previous is not None:
    print(f"{i} + {previous} = {i + previous}")
  previous = i

