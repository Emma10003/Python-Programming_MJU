# 정수를 입력받아 누적합을 구하고, 누적합이 1000 이상이 되면 반복문을 종료.
# 음수인 경우 누적합을 구하지 않는다.
# 입력된 수의 개수, 누적합, 평균을 구한다.
# 평균 = 누적합 / 입력된 수의 개수

total = 0
count = 0

while True:
    print(f"{count}번째 반복문")
    num = int(input("정수를 입력하시오: "))
    
    if num < 0:
        print("음수는 누적되지 않습니다.")
        continue

    total += num
    count += 1
    print(f"입력하신 숫자 {num}이(가) 누적되었습니다!")
    print()

    if total > 1000:
        break

print("-"*40)
print("<결과>")
print(f"입력한 수의 개수: {count}개")
print(f"누적합: {total}")
print(f"평균: {total / count:.2f}")