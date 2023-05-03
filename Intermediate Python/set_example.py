# set : unordered, mutable, no duplicate
# myset = {1, 2, 3}
# myset = set([1, 2, 3])
# myset = set('Hello')
# initialize empty set : myset = set()

# add items
# myset.add(1)

# remove elements
# myset.remove(3)
# if we want to remove an element which is not present then KeyError
# discard method will not throw KeyError, if element doesn not exist then nothing will happen

# empty set
# myset.clear()

# myset.pop()

# iterate over set
# for i in myset:
#       print(i)

# union and intersection
# odds = {1, 3, 5, 7, 9}
# evens = {0, 2, 4, 6, 8}
# primes = {2, 3, 5, 7}

# u = odds.union(evens) # combine without duplication
# print(u)

# i = odds.intersection(primes)
# print(i)

# difference
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)
print(diff) # all elements of setA that are not in setB

# update method in place
# setA.update(setB) will add elements of B to A if not already in A
# setA.intersection_update(setB) only keep intersection elements in setA
# setA.difference_update(setB)
