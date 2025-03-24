# 섭씨온도(C)를 입력받아 화씨온도(F)로 변환하기
ctemp = float(input("섭씨온도: "))
ftemp = (ctemp*9/5) + 32
print(f"화씨온도: {ftemp:.2f}")