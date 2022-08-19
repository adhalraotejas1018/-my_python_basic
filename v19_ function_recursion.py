# function recursion --->> function which called itself

# def pp(a):
#     print("value of a == ",a)
#     a=a+1
#     pp(a)
#
# pp(1)

# -------------------------------------------------------


# Python utilizes a system, which is known as “Call by Object Reference” or “Call by assignment”.
# In the event that you pass arguments like whole numbers, strings or tuples to a function,
# the passing is like call-by-value because you can not change the value of the immutable objects being passed to the function.

# ----------------------------------------------------------------------------------------------------------


def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))