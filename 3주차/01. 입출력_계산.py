num1 = int(input("첫 번째 정수를 입력하시오: "))
num2 = int(input("두 번째 정수를 입력하시오: "))
print(f"{num1}과(와) {num2}의 합은 {num1+num2}입니다.")

num3 = float(input("첫 번째 실수를 입력하시오: "))
num4 = float(input("두 번째 실수를 입력하시오: "))
sum = num3 + num4
# 계산 결과를 소수점 이하 3자리까지 반올림.
print(f"{num3}과(와) {num4}의 합은 {sum :.3f}입니다.")   # {변수 : 자리수제어} -> 소수점 5번째까지 출력