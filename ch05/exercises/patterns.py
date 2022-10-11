def star_pyramid():
  "This is a function that prints a pyramid of asterisks with a certain number of rows based on user input"
rows= int(input("How many rows would like?"))
for i in range(rows+1):
  print("*"*i,"\n")
  star_pyramid()