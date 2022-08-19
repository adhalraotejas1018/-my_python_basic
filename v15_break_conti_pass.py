# The break statement is used inside the loop to exit out of the loop.
numbers = [10, 40, 120,100,89,43, 230]
for i in numbers:
    if i == 100:
        break
print('number found ', i)


# The continue statement skip the current iteration and move to the next iteration.
print('\nlets see the use of the break statement  ')
numbers = [2,1,3,5,4,6,7,8,9,0]
for i in numbers:
    # skip below statement if number is greater than 10
    if i %2!=0:
        continue
    else:
      print('number is odd ',i)



# The pass is the keyword In Python, which won’t do anything.
# we use 'pass' keyword in ---> loops ,function            -----means empty fuction or loops
months = ['January', 'June', 'March', 'April']
for mon in months:
    pass
 