a_list = [1,2,3,4,5,1,2,4]

result1 = {x for x in a_list if x%2==0}
print(result1)   # {2, 4}
print(type(result1))   # <class 'set'>

result2 = [x for x in a_list if x%2==0]
print(result2)   # [2, 4, 2, 4]
print(type(result2))   # <class 'list'>