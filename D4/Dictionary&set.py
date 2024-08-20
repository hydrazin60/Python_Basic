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
print(students)
print(students["jiban"]) ## accessing the value using key
students["jiban"] = 100 ## updating the value using key
print(students["jiban"])
 
