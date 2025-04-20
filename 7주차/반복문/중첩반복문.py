# 직사각형 그리기
    # 넓이와 높이 입력받기.
print("직사각형")
width = int(input("넓이: "))
height = int(input("높이: "))
print(f"넓이: {width}, 높이: {height}")
    # 반복문 실행
for i in range(height):
    print(f"{i+1}: ", end = " ")
    for j in range(width):
        print("⬛", end=" ")
    print()


# 오른쪽 직각삼각형
    # 높이 입력받기
print("-" * 50)
print("오른쪽 직각삼각형")
tri_height = int(input("높이: "))
print(f"높이: {tri_height}")
    # 반복문 실행
for i in range(tri_height):
    print(f"{i+1} : ", end=" ")
    print("★" * (i+1))


# 정삼각형
    # 높이 입력받기
print("-" * 50)
print("정삼각형")
tri_height2 = int(input("높이: "))
print(f"높이: {tri_height2}")
    # 반복문 실행
for i in range(tri_height2):
    print(f"{i+1} : ", end=" ")
    print(' '*(tri_height2-(i+1)), end="")
    print("★ " * (i+1))   # 뒤에 공백이 있어야 함! 공백이 없으면 왼쪽 직각삼각형