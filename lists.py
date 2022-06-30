from audioop import reverse


lucky_numbers = [4,8,15,16,23,42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Tom"]

# extend
friends.extend(lucky_numbers)
print(friends)

# append
friends.append("Creed")
print(friends)

# insert
friends.insert(1, "Kelly")
print(friends)

# remove
friends.remove("Jim")
print(friends)

#clear
friends.clear()
print(friends)

# pop
friends = ["Kevin", "Karen", "Jim", "Oscar", "Tom"]
print(friends)
friends.pop(2)
print(friends)

# sort
friends = ["Kevina", "Karen", "Jim", "Oscar", "Tom7"]
print(friends)
friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)
def myfunc(e):
    return len(e)
friends.sort(key=myfunc)
print(friends)
friends.sort(key=myfunc, reverse=True)
print(friends)

print(lucky_numbers)
lucky_numbers.sort(reverse=True)
print(lucky_numbers)
lucky_numbers2 = lucky_numbers.copy()
print(lucky_numbers2)