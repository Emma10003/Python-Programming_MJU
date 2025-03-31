birth = input("생년월일을 yyyy/mm/dd 형식으로 입력하세요: ")

#인덱스를 이용한 문자열 슬라이싱
year = birth[0:4]
month = birth[5:7]
day = birth[8:10]

# 연도, 월, 일을 구분하여 출력
print(f"태어난 연도는 {year}년 입니다.")
print(f"태어난 월은 {month}월 입니다.")
print(f"태어난 일은 {day}일 입니다.")