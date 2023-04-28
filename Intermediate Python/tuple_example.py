# Tuple: ordered, immutable, allows duplicate elements
# cannot be changed after creation
mytuple = ('Max', 28, 'Boston')
# parentheses optional
mytuple = 'Max', 28, 'Boston' # this is also valid tuple
# If there is only 1 element then have to put comma after it for tuple
# mytuple = tuple(['Max', 28, 'Boston'])
# mytuple[0] = 'Tim' this will result in error TypeError : tuple object does not support item assignment

# count number of occurences of a prticular element
# print(mytuple.count('l'))

# unpacking a tuple
mytuple = 'Max', 28, 'Boston'
name, age, city = mytuple
# if there is a mismatch between variables and # of tuple values then ValueError: too many values to unpack

mytuple = (0, 1, 2, 3, 4)
i1, *i2, i3 = mytuple

print(i1) # 0
print(i2) # list [1, 2, 3]
print(i3) # 4

# tuple more efficient than list since immutable so python can do more optimization internally
import sys
my_list = [0, 1, 2, 'hello', True]
my_tuple = (0, 1, 2, 'hello', True)
print(sys.getsizeof(my_list), 'bytes') # 120 bytes
print(sys.getsizeof(my_tuple), 'bytes') # 80 bytes

# time taken is also less for tuples compared to lists
