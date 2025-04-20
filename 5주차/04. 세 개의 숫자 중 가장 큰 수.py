# 세 개의 수를 입력받은 후 가장 큰 수를 출력.
num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))
num3 = int(input("세 번째 숫자를 입력하세요: "))

if num1 > num2:
    if num1 > num3:   # num1이 가장 큰 경우
        print(num1)
    else:   # num3이 가장 큰 경우
        print(num3)
else:
    print(num2)   # num2가 가장 큰 경우

# num1이 가장 크다고 가정 -> 더 단순한 알고리즘.
result = num1
if result < num2:
    result = num2   # num2가 더 큰 경우 result값을 num2로 변경.
if result < num3:
    result = num3   # num3이 더 큰 경우 result값을 num3으로 변경.