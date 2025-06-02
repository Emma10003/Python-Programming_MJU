myList = [1,2,3,4,1,2,3,4]
mySet = set(myList)   # myList를 set으로 형변환
print(mySet)   #{1, 2, 3, 4}

letters = set("abcabc")   # 문자열을 분해하여 세트로 변환.
print(letters)   #{'a', 'b', 'c'}