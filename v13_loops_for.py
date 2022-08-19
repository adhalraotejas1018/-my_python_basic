# loops - sequance of instructions that is continually repeated untill a certain condition is reached
# we use loops for doing same taks multiple times

#printin hi 10 times
print("\n 1----------printing hi  10 timess")
for i in range(10):
    print("hi",end=" ")

#loop 10 to 20
print("\n\n 2----------printing  10 to 20")
for i in range(10,20):
    print(i,end=" ")

#loop in list
print("\n\n3-----------printing the list items")
list1=["Virat",1018,"Rutvik",10,"Tejas",18]
for i in list1:
    print(i,end=" ")

#looop in string
print("\n\n4 --------printing the string single character ")
for x in "Virat1018":
    print(x,end=" ")

#loops range 3
print("\n\n5---------printing the j while range have 3 number input")
for j in range(1,30,3):
    print(j,end=" ")
