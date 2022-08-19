# tell()-->> this function is use to check where is your pointer reading file
# means cheaking the pointer poisition where we read the file

# seek()  -->>> this function is use to reset the pointer in file

f=open("z5Rutvik")
print("position of pointer ",f.tell())       #pointer is at 0th position so it print 0
print(f.readline())
print(f.readline())
print(f.readline())
print(" current position of pointer ",f.tell())     # it print cuurent positiin of your pointer

f.seek(0)    #setting pointer position at 0
print(f.readline())