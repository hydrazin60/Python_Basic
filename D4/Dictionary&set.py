######  Dictionary in Python ####### ( similar to object in javascript) 
### :- Dictionaries are used to store data values in key:value pairs
### :-  They are unordered, mutable(changeable) & don’t allow duplicate keys

students = {
    "jiban": 95.3,
    "subject" : ["python", "javascript", "C++"],
    "favrit" : ("Javascript" , "python"),
    "pandey": 85.6, 
    "khem": {
"first-name": "karuna",
"second-name": "karki",
"Age" : 20,
"marks" : [95.3, 85.6, 75.9, 65.4, 55.9, 45.2],
"location": {
    "permanant": "sindhuli",
    "current" : "dharan"
}

    },
    "karuna": 65.4, 
    "nisan": True, 
    "samir":  "giri"
}
# print(students)
# print(students["jiban"]) ## accessing the value using key
# students["jiban"] = 100 ## updating the value using key
# print(students["jiban"])
 
######### Dictionary Methods  ##############
## Dictionary.keys()  # return all the keys
# print(students.keys())  # return all the keys
# print(len(students.keys())) # return the number of keys
## Dictionary.values()  # return all the values
#print(students.values()) # return all the key and values 
## Dictionary.items()  # return all the keys and values
# print(students.items()) # return all the key and values
## Dictionary.get(key)  # return the value of the key 
# print(students.get("jiban")) # return the value of the induvisial key
# print(students["jiban"]) #  return the value of the induvisial key
## Dictionary.update()  # update the dictionary
# students.update({"jiban": 100}) # update the value of the key
# print(students)
 
########## Set in Python  ###########
### : Set is the collection of the unordered items.
### : Each element in the set must be unique & immutable.

set1 = {"jiban", "pandey",   100, 200, 300,   "samir", "pandey" }
set2 = {"jiban" , "pandey" , 200 , "karuna"}
# # print(set1)
# #########  Set Methods  ############
# ## set.add( el )
# set1.add("bipana") # add the element ## bipana is add in the set
# # print(set1)
# ## set.remove( el )
# set1.remove( "bipana") # remove the element
# # print(set1)
# ## set.clear()
# # set1.clear() # clear the set
# # print(set1)
# ## set.pop()
# set1.pop() # remove the last element
# # print(set1)
# ## set.union( sset2) # return the union of two sets
# # print(set1.union(set2))   # return the union of two sets but is not change the orginal set
# ## set.intersection( sset2) # return the intersection of two sets but is not change the orginal set
# print(set1.intersection(set2))