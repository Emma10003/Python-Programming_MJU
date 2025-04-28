# 정삼각형
# 높이 입력받기
'''
  ★
 ★★
★★★
'''
print("-"*50)
print("정삼각형")
height = int(input("높이: "))

print(f"정삼각형의 높이: {height}")

for i in range(height):
    print(f"{i+1}: ", end="")
    print(" "*(height-i), end="")
    print("★ "*(i+1))