#

dict1 = {
    "namaste" : "hello",
    "raho haste" : "keep smiling",
    "meetha" : "sweet"
}
print(dict1.keys())
inp = input("Enter the key: ")

if(inp == "namaste"):
    print(dict1.get("namaste"))
elif(inp == "raho haste"):
    print(dict1.get("raho haste"))
else:
    print(dict1.get("meetha"))

# to display unique numbers(once)
# numbers = []
# for i in range(8):
#     num = int(input("Enter 8 numbers: "))
#     numbers.append(num)
# unique = set(numbers)
# print(unique)


#
s2 = {18,'18'}
print(s2) #yes we can have a set with 18 as integer and 18 as string together

#
s = set()
s.add(20)
s.add(20.0)
s.add('20') 
length = len(s)
print(length)

#
dict2 = {}
dict2.update({"Saket" : "English","Prathamesh" : "Hindi","Kunal" : "Bhojpuri","Keshav":"Maithli"})
print(dict2)

#
s = {8,7,12,"Harry",[1,2]}
print(s)  #it will raise error

