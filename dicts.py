monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

# Keys can only be strings, numbers, or tuples, but values can be any data type.

print(monthConversions["Nov"])
print(monthConversions.get("Nov"))
print(monthConversions.get("Leap", "Not Found!"))

print("--- --- --- --- --- --- ---")

dict1 = {"Maths":56,"Biology":78,"Physics":76,"Chemistry":23}
print("before clearing : ",dict1)

dict2  = dict1.copy()
print("copy dict1 to dict2 : ",dict2)

dict1.clear()
print("after clearing : ",dict1)

dict2.pop("Chemistry")
print("popping dict2 : ",dict2)

dict2.popitem()
print("popitem : ",dict2)

print("dict2.setdefault(\"Maths\",67) : ",dict2.setdefault("Maths",67))
print("before setdefault with new key value : ",dict2)
print("dict2.setdefault(\"English\",67) : ",dict2.setdefault("English",67))
print("after setdefault with new key value : ",dict2)

print("dict2 values : ",dict2.values())

print("dict2 keys : ",dict2.keys())

print("dict2.items() : ",dict2.items())

keys= ("key1","key2","key3")
values = 7
dict3 = dict.fromkeys(keys,values)
print("keys : ",keys)
print("values : ",values)
print("dict3 = dict.fromkeys(x,y) : ",dict3)

print("dict2.get(\"Maths\") : ",dict2.get("Maths"))

dict2.update({"History":45})
print("dict2.update() : ",dict2)
dict2.update({"Biology":45})
print("dict2.update() : ",dict2)