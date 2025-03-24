'''
1. 기사 포맷 작성하기:
00월 00일 0요일
오늘의 최고 온도는 00도, 최저 온도는 00도로 일교차는 00도가 되겠습니다.
오늘은 대기질 지수가 000 정도로 00이겠습니다.
이번 주는 대체로 따뜻한 날씨가 이어지겠습니다.

2. 필요한 변수 선언하기
month (00월)
day (00일)
week (0요일)
max_temp (최고 온도)
min_temp (최저 온도)
range (일교차)
air_quality (대기질 지수)
air_quality_index (나쁨/보통/좋음)
'''
month = input("오늘이 몇 월인가요? (ex. 3): ")
day = input("오늘이 몇 일인가요? (ex. 24): ")
week = input("오늘이 무슨 요일인가요? (ex. 월): ")
max_temp = int(input("오늘의 최고 온도는? : "))
min_temp = int(input("오늘의 최저 온도는? : "))
range = max_temp - min_temp
air_quality = input("오늘의 대기질 지수는? (ex. 114): ")
air_quality_index = input("오늘의 대기질 지수는? (좋음/보통/나쁨 중 택1): ")
# 출력
print("-------------------------------")
print(f"{month}월 {day}일 {week}요일")
print(f"오늘의 최고 온도는 {max_temp}도, 최저 온도는 {min_temp}도로 일교차는 {range}도가 되겠습니다.")
print(f"오늘은 대기질 지수가 {air_quality}정도로 {air_quality_index}이겠습니다.")
print("이번 주는 대체로 따뜻한 날씨가 이어지겠습니다.")