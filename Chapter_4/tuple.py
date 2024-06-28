# a = (1,2,5,6) # tuple with four elements
# a = () # empty tuple
# a = (1) # number which is enclosed within the parentheses, so it's type will of <class 'int'>
# a = (1,) # tuple with only one element
a = (1,45,342,3424,False,45,"Rohan","Shivam")
# a[0] = 453 # TypeError: 'tuple' object does not support item assignment
# print(type(a))
# print(a)

no = a.count(45)
print(no)

i = a.index(45)
print(i)

print("Length of the tuple is:",len(a))