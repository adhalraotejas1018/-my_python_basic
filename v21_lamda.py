# A lambda function can take any number of arguments, but can only have one expression(opration)
# Python Lambda Functions are anonymous function means that the function is without a name

# Example
# Add 10 to argument a, and return the result:
# : from here function starrt


myfunction = lambda a : a + 10
print(myfunction(5))

# Multiply argument a with argument b and return the result:
# lambda is keyword
# a,b araguments which htis function takes input
# : function starts
# a*b this is what function do

multi = lambda a, b : a * b
print(multi(5, 6))