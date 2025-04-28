# 세 개의 수를 입력받은 후 가장 큰 수를 출력.
num1 = int(input("첫 번째 숫자: "))
num2 = int(input("두 번째 숫자: "))
num3 = int(input("세 번째 숫자: "))

result = num1
if result < num2:
    result = num2
if result < num3:
    result = num3

print(f"입력하신 숫자 {num1}, {num2}, {num3} 중 가장 큰 수는 {result}입니다.")