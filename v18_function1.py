#passing the multiple parameter
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("ram", "sham", "kalu")

# -------------------------------------------------------------------
#return value
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

