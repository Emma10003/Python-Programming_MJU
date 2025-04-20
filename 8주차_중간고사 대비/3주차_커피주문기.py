# 메뉴대로 개수를 입력받고 가격 계산 후
# 총 가격 표시
# 거스름돈 계산 추가

ame_price = 2000
latte_price = 3000
capp_price = 3500

ame = int(input("아메리카노 개수: "))
latte = int(input("카페라떼 개수: "))
capp = int(input("카푸치노 개수: "))

total_price = (ame_price*ame) + (latte_price*latte) + (capp_price*capp)

print(f"총 {total_price}원 입니다.")
print("-"*40)
money = int(input("투입한 돈: "))
change = money - total_price
print(f"투입한 돈: {money}")
print(f"거스름돈: {change}")
print("-"*40)

# 거스름돈 계산
# 10,000원
change_10000 = change // 10000
change = change % 10000
# 5,000원
change_5000 = change // 5000
change = change % 5000
# 1,000원
change_1000 = change // 1000
change = change % 1000
# 500원
change_500 = change // 500
change = change % 500
# 100원
change_100 = change // 100
change = change % 100

# 거스름돈 출력
print(f"10000원: {change_10000}장")
print(f"5000원: {change_5000}장")
print(f"1000원: {change_1000}장")
print(f"500원: {change_500}개")
print(f"100원: {change_100}개")