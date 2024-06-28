friends = ["Apple","Orange",5,345.06,False,"Akash","Rohan"]

print(friends[0])

name = "Harry"

# name[3] = 'y' # TypeError: 'str' object does not support item assignment

friends[0] = "Grapes"   # Unlike strings, lists are mutable.

print(friends[0])

print(friends[1:4])

friends.append("Harry")

print(friends)

l1 = [1,34,62,2,6,11]
# l1.sort()
# l1.reverse()
# l1.insert(3,333333) # Insert 333333 such that it's index in the list is 3
# l1.pop(3)
# value = l1.pop(3)
# print(value)
l1.remove(11)
print(l1)


