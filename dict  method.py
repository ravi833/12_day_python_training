'''dict is a empty set'''
'''dict is a key value pair'''


# a={1: 'ravi',2:245,3:456,4:876,5:'shadd'}
# print(a,type(a))  # {1: 'ravi', 2: 245, 3: 456, 4: 876, 5: 'shadd'} <class 'dict'>

# print(dir(dict))   ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

# a={1: 'ravi',2:245,3:456,4:876,5:'shadd'}
# a.clear()
# print(a)  #  {}
  
# a=[1,2,3,45]
# print(dict.fromkeys(a,'pass'))   # {1: 'pass', 2: 'pass', 3: 'pass', 45: 'pass'}


# a={1: 'ravi',2:245,3:456,4:876,5:'shadd'}
# print(a.get(2))  # 245
# print(a.get(45))  #None
# print(a.items())   #dict_items([(1, 'ravi'), (2, 245), (3, 456), (4, 876), (5, 'shadd')])

# print(a.keys())  # dict_keys([1, 2, 3, 4, 5])

# print(a.values())  #dict_values(['ravi', 245, 456, 876, 'shadd'])

# print(a.pop(45))  #keyerror
# print(a.pop(3))   #456
# print(a.popitem())  # (5,'shadd')


# a={1: 'ravi',2:245,3:456,4:876,5:'shadd'}
# a.setdefault(4,56) # {1: 'ravi', 2: 245, 3: 456, 4: 876, 5: 'shadd'}
# print(a)
# a.setdefault(56,'ravi')
# print(a) # {1: 'ravi', 2: 245, 3: 456, 4: 876, 5: 'shadd', 56: 'ravi'}


# a={1: 'ravi',2:245,3:456,4:876,5:'shadd'}
# a.update({3:'kumar'})
# print(a) #  {1: 'ravi', 2: 245, 3: 'kumar', 4: 876, 5: 'shadd'}
# a.update({45:456})
# print(a)  # {1: 'ravi', 2: 245, 3: 'kumar', 4: 876, 5: 'shadd', 45: 456}