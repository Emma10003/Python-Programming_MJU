num = int(input("정수를 입력하시오: "))
fact = 1   # 누적곱

print(f"{num}!은")

for i in range(1, num+1):
    if i == num:   # i가 마지막 수와 같은 경우
        fact *= i   # 누적곱
        print(i, end=" = ")   # 프린트
    else:
        fact *= i
        print(i, end = " * ")

print(f"{fact}입니다.")
    