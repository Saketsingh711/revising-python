#Dictionary = collection of key-value pairs,unordered,mutable,indexed
a = {
"key": "value",
"harry": "code",
"marks": "100",
"list": [1, 2, 9]
}
print(a["key"])
print(a["list"])
print(a.items()) #to get all items
print(a.keys()) #to get keys
print(a.values()) #to get values
print(a.update({"friends":"Saket"})) #to add new values in dictionary
print(a.items()) 
print(a.get("marks"))


#sets = collection of non-repetitive elements,unordered,unindexed,no duplicate
s = set() #for empty set
s1 = {2,3,5,6} #non empty set
print(s1)
# print(len(s1)) #length of set
# s1.remove(3)  #removes the given element
# print(s1)
# s1.pop() #will delete random element
# print(s1)
#s1.clear()  empties the set s1
s2 = {6,7,8,9}
print(s1.union(s2))   #adds to sets
print(s1.intersection(s2))    #shows only common element in two sets