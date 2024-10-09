marks = {
    "jiban" : 99,
    "pandey" : 98,
    "suresh" : 90,
    "khem" : 60,
    "nisan" : 87
} 
print(marks.keys())
print(marks.values())
print(marks)

print(marks.get("jiban")) ## get the value using key if key is not present it will show none
print(marks["jibacn"])  ## get the value using key if key is not present it will show error

