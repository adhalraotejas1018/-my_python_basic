# file IO basic
"""
"r"- open file for reading
"w" - open file for writing
"x"-creates file if not exists(created)
"a"- add more content to a file
"t"-open file in text mode
"b"-open file in binary mode
"+"- open file in read and write

"""


# reading the file all file content
f=open("zRutvik.txt")
content=f.read()
print(content)
f.close()

# reading  file lines one by one of file
f=open("zRutvik.txt")
print(f.readline())
print(f.readline())

# reading the file 3 character
f=open("zRutvik.txt")
content=f.read(3)
print(content)
f.close()

#


