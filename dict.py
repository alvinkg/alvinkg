# a key-value pair using unique keys {}
monthConversions = {
    "Jan": "January",
    "Feb": "February",
}
print(monthConversions)
print(monthConversions["Jan"])
print(monthConversions["Feb"])
print(monthConversions.get("Mar", "Not a valid key."))