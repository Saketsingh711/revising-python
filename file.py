# open() function
# open("filename", "mode of opening(read mode by default)")
f = open("practice 3.py","r")
text = f.read()
print(text)
print(f.readline())   # read one line from the file
f.close()

# r - open for reading
# w - open for writing
# a - open for appending
# + - open for updating.
# ‘rb’ will open for read in binary mode.
# ‘rt’ will open for read in text mode.

# make(if not alrdy made) and Open the file in write mode
f = open("this.txt", "w")
# Write a string to the file
f.write("this is nice , also")
# Close the file
f.close()


#best way is to open and close the file automatically is the "with" Statement

with open("this.txt","r") as f:
    text = f.read()

print(text)
