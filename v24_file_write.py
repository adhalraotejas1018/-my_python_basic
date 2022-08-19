#writting in the file
# here all file data erase and clean file then add your text
# f=open("z2Rutvik.txt",'w')
# f.write("happy new year\n broo")
# f.close()


#here it cannot erase the file old data
#it add your text after old text of file
# f=open("z3Rutvik.txt",'a')
# f.write("\nViRat18")
# f.write("\nrutvik")
# f.close()


#handling read and write
#open file for both read and write
f=open("z4Rutvik.txt",'r+')
print(f.read())
f.write("\nthank you .....")
f.close()