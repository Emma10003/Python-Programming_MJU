total = 0   # 누적합
num = 1

print("1부터 10까지의 합계는 ")
for num in range(1, 11, 1):
    if num == 10:   # num이 10인 경우에만 끝에 = 을 붙임
        total += num   # 누적
        print(num, end=" = ")
        break   # num이 10이면 반복문 종료
    total += num   # 누적
    print(num, end=" + ")

print(f"{total}입니다.")