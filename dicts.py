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
