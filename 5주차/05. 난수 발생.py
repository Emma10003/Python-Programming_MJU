import random
'''
random.randrange(3)   # 0, 1, 2 중 랜덤 수를 구함.
random.randint(0, 100)   # 0~100 사이의 랜덤한 정수.
'''
print("동전 던지기 게임을 시작합니다.")
coin = random.randrange(2)   # 0, 1 중 랜덤 수
if coin == 0:
    print("앞면입니다.")
else:
    print("뒷면입니다.")

print("게임이 종료되었습니다.")