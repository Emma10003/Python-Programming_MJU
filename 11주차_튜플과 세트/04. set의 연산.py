A = {'apple', 'banana', 'grape'}
B = {'apple', 'banana', 'kiwi'}
# 합집합
C = A | B   # A.union(B)
print(C)

# 교집합
D = A & B   # A.intersection(B)
print(D)

# 차집합
E = A - B   # A.difference(B)
print(E)

# 부분집합
if A < B:
    print("A는 B의 부분집합입니다.")
else:
    print("A는 B의 부분집합이 아닙니다.")

if A == B:
    print("A와 B는 같습니다.")
else:
    print("A와 B는 다릅니다.")