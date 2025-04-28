# 정수를 입력받아 해당 정수까지의 누적곱을 구하기.
# 1 * 2 * ... * n = 누적곱
# 위의 형태로 출력할 것.
num = int(input("정수를 입력하시오: "))
fact = 1

print(f"{num}!은")
# for i in range(1, num+1, 1):
#     if i == num:
#         fact *= i
#         print(i, end=" = ")
#         break
#     print(i, end=" * ")
#     fact *= i
#     i += 1

for i in range(1, num+1):
    if i == num:
        fact *= i
        print(i, end=" = ")
    else:
        fact *= i
        print(i, end=" * ")

print(f"{fact}입니다.")