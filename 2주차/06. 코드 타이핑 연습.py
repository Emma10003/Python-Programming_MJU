# 파일: 01.py_intro.pdf -- p.48

import turtle
colors = ["red", "purple", "blue", "green", "yellow", "orange"]
t = turtle.Turtle()

turtle.bgcolor("black")   # 배경색
t.speed(0)
t.width(3)   # 선 굵기
length = 10

while length < 1000:   #500
    t.forward(length)
    t.pencolor(colors[length%6])   # color 리스트 인덱싱해서 색상 변경.
    t.right(89)   # 회전각 89도.
    length += 5

input()