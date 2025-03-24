# 네이버 금융계산기의 예금 기능 구현하기
# 입력: 예치금, 기간(월), 연이자율(%)
# 계산: 세전이자, 세후이자, 총 수령액

# 입력
money = int(input("예치금: "))
month = int(input("기간(월): "))
rate = float(input("연 이자율(%): "))

# 계산
before_tax = money * rate/100/12*month   # 세전이자
tax = before_tax * 15.4/100   # 세금
after_tax = before_tax - tax   # 세후이자
total = money + after_tax

print(f"예치금 {money}를 {month}개월동안 연이율{rate}로 저축하면")
print(f"총 {total}원을 수령하실 수 있습니다.")
print("-"*20)
print(f"원급합계: {money}")
print(f"세전이자: {before_tax:0f}원")
print(f"이자 과세(15.4%): {-tax:.0f}원")
print(f"세후이자: {after_tax}")
print("-"*20)
print(f"총 수령액: {total:.0f}원")