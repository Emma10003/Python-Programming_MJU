# 메뉴대로 개수를 입력받고 가격 계산 후
# 총 가격 표시
# 거스름돈 계산 추가
ame_price = 2000
latte_price = 3000
capp_price = 3500

americano = int(input("아메리카노 개수: "))
latte = int(input("카페라떼 개수: "))
cappuccino = int(input("카푸치노 개수: "))
total = (americano*ame_price) + (latte*latte_price) + (cappuccino*capp_price)

print(f"총 {total}원입니다.")
print("------------------------------")
# 거스름돈 계산
money = int(input("투입한 돈: "))
change = money - total
print(f"거스름돈: {change}원")

# 10000원
coin_10000 = change // 10000
change = change % 10000
# 5000원
coin_5000 = change // 5000
change = change % 5000
# 1000원
coin_1000 = change // 1000
change = change % 1000
# 500원
coin_500 = change // 500
change = change % 500
# 100원
coin_100 = change // 100

# 거스름돈 프린트
print(f"10,000원 지폐: {coin_10000}개")
print(f"5,000원 지폐: {coin_5000}개")
print(f"1,000원 지폐: {coin_1000}개")
print(f"500원 동전: {coin_500}개")
print(f"100원 동전: {coin_100}개")