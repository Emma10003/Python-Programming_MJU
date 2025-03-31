# 화씨온도(F)를 입력받아 섭씨온도(C)로 변환하기
ftemp = float(input("화씨온도: "))
ctemp = (ftemp-32)*5/9
# print(f"섭씨온도: {ctemp}")

# 좀 더 세심한 출력양식 - 소수점 둘째자리까지 반올림
print("섭씨온도: %.2f" %(ctemp))
print(f"섭씨온도: {ctemp:.2f}")