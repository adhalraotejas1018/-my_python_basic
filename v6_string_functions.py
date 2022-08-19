#lets see some inbuilt function of string
name="Rutvik1018Virat"

#printing 0 to 4 character
print(name[0:5])
#skipping one element between 0 to 8 element
print(name[0:9:2])                          #0 for staring element and 8+1 for 8th element-----2 for skiiping 1 element

#reversed string
print(name[::-1])

#checking if string return with "at" return True --- otherwise return False
print(name.endswith("at"))

#checki hoe many times number comes in string
print(name.count("v"))

#make  string capitalize
print(name.capitalize())
print(name.upper())

#make string letter in small alphabates
print(name.lower())

#replacing the string letter
name.replace("Virat","Ruva")
print(name)

