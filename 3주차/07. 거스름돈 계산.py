# 자동판매기는 사용자로부터 투입한 돈과 물건값을 입력받는다
# 물건값은 100원 단위
# 자판기는 동전 500원, 100원짜리만 가지고 있다고 가정.
# 프로그램은 잔돈을 계산하여 출력한다.
# % 연산자 활용할 것

ins = int(input("투입한 돈: "))
price = int(input("물건값: "))
change = ins - price
# 1000원
coin_1000 = change // 1000
change = change % 1000   # 1000원을 계산하고 남은 나머지를 다시 change에 넣기
# 500원
coin_500 = change // 500   # 500원 동전의 개수
change = change % 500
# 100원
coin_100 = change // 100   # 100원 동전의 개수

print(f"거스름돈: {change}")
print(f"1000원 지폐의 개수 {coin_1000}")
print(f"500원 동전의 개수: {coin_500}")
print(f"100원 동전의 개수: {coin_100}")