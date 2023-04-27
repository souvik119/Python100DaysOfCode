# Lists : ordered, mutable, allows duplicate elements, con contain different data types
# IndexError : list index out of range for very large or small index
# len() print size
# append()
# insert(<index>, item)
# pop() this returns and removes last item
# remove specific element remove(<item>), if we specify a value which is not in list then ValueError
# remove all elements with clear() method
# reverse the list reverse()
# sort using sort() in place (changes original list)
# new list with sorted values sorted() (does not affect original list)
# new list with same elements initialize
mylist = [0] * 5
print(mylist)

# concat 2 lists
mylist2 = [1, 2, 3, 4, 5]
new_list = mylist + mylist2
print(new_list)

# slicing
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = mylist[1:5]
print(a)

# reverse a list
a = mylist[::-1]

# copying a list
list_org = ['banana', 'cherry', 'apple']
list_cpy = list_org

# both point to same mem location
# if list_cpy is now modified it will also modify list_org

list_cpy.append('lemon')
print(list_cpy)
print(list_org)

# if we want copy then use .copy() method or use list() or use slicing [:]

# list comprehension
a = [1, 2, 3, 4, 5, 6]
b = [i*i for i in a]
print(b)

