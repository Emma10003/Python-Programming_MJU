import random

time = random.randint(1, 24)
sunny = random.choice([True, False])

# 시간
print(f"좋은 아침입니다. 현재 시각은 {time}시 입니다.")

# 날씨
if sunny:
    print("현재 날씨가 화창합니다.")
else:
    print("현재 날씨가 화창하지 않습니다.")

# 종달새
if (time>=6 and time<=9) and sunny:
    print("종달새가 노래합니다.")
else:
    print("종달새가 노래하지 않습니다.")