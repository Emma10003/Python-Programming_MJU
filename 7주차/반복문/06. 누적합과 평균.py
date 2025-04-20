total = 0   # 누적합
count = 0   # 횟수

while True:
    print(f"😋 {count}번째 반복문")
    num = int(input("정수를 입력하세요: "))
    if num < 0:   # 음수인 경우 누적하지 않고 다시 반복문 실행.
        continue

    total += num  # 음수가 아닌 경우 이 코드가 실행됨.
    count += 1
    
    if total >= 1000: break

print("-"*30)
print("✅ 반복문 완료!")
print(f"입력된 수: {count}개")
print(f"총합: {total}")
print(f"평균: {total/count:.2f}")
