# try except -> for exception handling
# it is use for handling the errors in our code
# if try block code contains error then except block code will run

v=18
try:
    print("10 devide by zero = ",v/0)
except Exception as e:
    print("error is == ",e)
    print("you cannot devided by zero ")