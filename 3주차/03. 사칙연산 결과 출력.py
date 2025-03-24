# 변수를 이용하여 사칙연산 만들기
# 변수에 대입하기
# num1 = 1000
# num2 = 2000

# 입력 받기
num1 = int(input("첫번째 정수를 입력하세요: "))
num2 = int(input("두번째 정수를 입력하세요: "))

addition = num1 + num2   # 덧셈
subtraction = num1 - num2   # 뺄셈
multiplication = num1 * num2   # 곱셈
division = num1 / num2   # 나눗셈
quotient = num1 // num2   # 몫
remainder = num1 % num2   # 나머지

# 출력하기
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")
print(f"{num1} // {num2} = {quotient}")
print(f"{num1} % {num2} = {addition}")