# 11주차 수업
import random
from datetime import date

menu = []
menu.append("마라탕")
menu.append("마라샹궈")
menu.append("즉석떡볶이")
menu.append("샤브샤브")
menu.append("닭가슴살")
menu.append("배추찜")
menu.append("피자")
menu.append("마라엽떡")

recommend_menu = random.choice(menu)   # quotes 리스트 내에서 랜덤하게 선택
today = date.today().strftime("%m월 %d일")   # 오늘 날짜 저장

print("#"*50)
print(f"👍 {today}의 점메추👍")
print(f"{recommend_menu}, 추천!")
print("#"*50)
