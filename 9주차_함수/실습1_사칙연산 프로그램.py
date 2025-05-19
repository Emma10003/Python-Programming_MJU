
# 실습 1: 사칙연산 기능 만들기
# 함수 정의
def menu():  #메뉴 함수
    print("="*60)
    print("1.입력받기 2.더하기 3.빼기 4.곱하기 5.나누기\t 0. 종료하기")
    print("="*60)
    return

def plus(x, y):  #더하기 함수
    print("더하기 함수를 실행합니다.")
    print(f"{x} + {y} = ", end="")
    return (x + y)

def minus(x, y):  # 빼기 함수
    print("빼기 함수를 실행합니다.")
    print(f"{x} - {y} = ", end="")
    return x - y

def multiply(x, y):  # 곱하기 함수
    print("곱하기 함수를 실행합니다.")
    print(f"{x} x {y} = ", end="")
    return x * y

def devide(x, y):
    print("나누기 함수를 실행합니다.")
    if(y==0):
        print("0으로는 나눌 수 없습니다.")
        return 0
    print(f"{x} / {y} = ", end="")
    return round(x / y, 2)

# 실행문
while True:
    menu()
    choose = int(input(">>> menu: "))
    if choose==0:
        print("프로그램을 종료합니다.")
        break
    elif choose==1:
        x = int(input(">>> 정수 1을 입력하세요: "))
        y = int(input(">>> 정수 2을 입력하세요: "))
        continue   # 반복문 맨 처음으로 이동
    elif choose==2:
        result = plus(x, y)
    elif choose==3:
        result = minus(x, y)
    elif choose==4:
        result = multiply(x, y)
    elif choose==5:
        result = devide(x, y)
    print(result)

print("종료!")