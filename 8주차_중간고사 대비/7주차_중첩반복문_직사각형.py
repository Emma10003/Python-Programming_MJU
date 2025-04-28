# 직사각형 그리기
# 높이와 넓이 입력받기
'''
⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛
'''
height = int(input("높이: "))
width = int(input("넓이: "))
print(f"높이: {height}, 넓이: {width}")

#for i in range(height+1):
#    print(f"{i+1} : ", end="")
#    print("⬛"*width)

# 중첩반복문 사용
for i in range(height+1):
    print(f"{i+1}: ", end="")
    for j in range(width+1):
        print("⬛", end="")
    print()

print("직사각형 완성!")