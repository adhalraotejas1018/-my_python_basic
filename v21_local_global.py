# local variable - a variable available for only that function or loop
# global variable - a variable which available anywhere


var1=1
def my_fun():
    var=20
    print("  value in the  function is = ",var)
    print("  value in the  function is = ",var1)

my_fun()
print("  value  outside the function is = ",var1)
print("  value  outside the function is = ",var)

# error because
# here we see the value of var in function is 20
# we cannot print var value outside the function

