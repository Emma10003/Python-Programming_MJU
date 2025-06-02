# list -> set
list1 = [1,2,3,4,5,1,2,4]
print(len(set(list1)))   # 5: {1,2,3,4,5}


# 두 리스트의 교집합 구하기
list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]

result = set(list1) & set(list2)   # set으로 변환해서 교집합 연산.
print(result)   #{3, 4, 5}