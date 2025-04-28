# 오른쪽 직각삼각형
# 높이 입력받기
'''
★
★★
★★★
★★★★
'''
print("-"*50)
print("직각삼각형")
height = int(input("높이: "))

print(f"오른쪽 직각삼각형 높이: {height}")

for i in range(height):
    print(f"{i+1}: ", end="")
    print('★'*(i+1))