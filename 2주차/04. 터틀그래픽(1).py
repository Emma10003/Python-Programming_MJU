# 거북이를 그리기 위한 패키지 불러오기
import turtle
t = turtle.Pen()   # 거북이를 그려주는 연필.
t.shape("turtle")   # 연필 모양을 거북이 모양으로 하는 듯

# 거북이로 그림 그리기

# 앞으로 움직이기기
t.forward(100)   # 연필이 앞으로 100칸. (연필이 거북이 모양이니까 거북이가 앞으로 100칸 움직임)
# 다른 방법
# t.fd(100)

# 오른쪽으로 90도 회전
t.right(90)


# 네모 만들기 -> 위의 코드를 4번 반복.
t.forward(100)
t.right(90)   # 2번

t.color("red")   # 거북이와 선 색상을 변경
t.forward(100)
t.right(90)   # 3번

t.color("black")
t.forward(100)
t.right(90)   # 4번

input()   # 화면을 클릭해야 꺼지도록 설정.