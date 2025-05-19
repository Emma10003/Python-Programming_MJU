# 실습 2: 사각형, 삼각형 그리기
def draw_line(w):
    for i in range(w):
        print("■ ", end="")   # 넓이만큼 한 줄로 반복, 문자 뒤에 띄어쓰기!!
    print()   # 줄바꿈

def triangle(h):
    print("="*60)
    print("직각삼각형 그리기 프로그램")
    for i in range(h):
        draw_line(i+1)

def rectangle(h, w):
    print("직사각형 그리기 프로그램")
    for i in range(h):
        draw_line(w)

def e_triangle(h):
    print("정삼각형 그리기 프로그램")
    for i in range(h):
        for j in range(h-i, 0, -1):
            print(" ", end="")
        draw_line(i+1)

height = int(input("높이를 입력하세요: "))
width = int(input("넓이를 입력하세요: "))
triangle(height)
rectangle(height, width)
e_triangle(height)