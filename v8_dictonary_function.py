#lets see some dictionary functions and features
dict1={
        10 :"Rutvuk",
        18:"Virat",
        7:"masd",
        1:"kl rahul",
            }

#printing the dictionary
print(dict1)

#printing value with the help of keys
print(dict1[18])

#deleting the record 1: kl rahul
del dict1[1]
print(dict1)

#copying the dictionary to another variable
dict2=dict1.copy()
print(dict2)

#printing only keys
print(dict2.keys())

#printing the only values
print(dict2.items())