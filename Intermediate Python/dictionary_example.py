# Dictionary : key-value pairs, unordered, mutable
# mydict = {'name': 'max', 'age': 28, 'city': 'new york'}

# mydict2 = dict(name='souvik', age='27', city='boston')
# if key is not present in dictionary then KeyError

# del mydict[<key>]
# mydict.pop(<key>)
# mydict.popitem() # last inserted item
# if <key> in mydict:
# try:
#   print(mydict[<key>])
# except:
#   print('Error')
# mydict.keys()  mydict.values()  mydict.items()

# mydict_copy = mydict not correct way since both point to same mem location
# mydict_copy = mydict.copy()
# mydict_copy = dict(mydict)

# merge dictionaries
# mydict.upadte(mydict2)

# key can be any immutable type string, numbers, tuples
# mytuple = (8, 7)
# mydict = {mytuple: 15}
# list cannot be keys
