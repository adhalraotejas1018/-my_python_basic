# set is use to store multiple data item in single variable
# it is the built in data type in python
# it is collectoion unchangeable ,unordered and unindexed
# no duplication allowed

set1={"apple","banana","cherry","mango","mango"}
print(set1)
print(type(set1))



# ___--------------------------------------
# **************************************
set2=set()                   #creating the empty set

set2.add(10)                # adding the element into set
set2.add(18)
set2.add(10)

print(set2)
# it print the 10,18 only because no duplication allowed in the set