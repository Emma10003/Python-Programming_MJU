# 출력할 때는 print()
# 입력받을 때는 input()
# '=' 표시는 '같다'가 아니라, 저장해라.

# 이름과 나이, 좋아하는 색깔 입력받기
print("Hello, nice to meet you.")
name = input("What's your name? ")
age = input("How old are you? ")
color = input("What's your favorite color? ")

# 출력하기 1: '+' 이용
print(age + " years old " + name + " likes " + color + "!")

# 출력하기 2
print("-------------------------------------------")
print("name: " + name)
print("age: " + age)
print("favorite color: " + color)
print("-------------------------------------------")

# 출력하기 3 -- 추천: 문자열 포맷 사용하기(f-string)
print("-------------------------------------------")
print(f"name : {name}")
print(f"age: {age}")
print(f"favorite color: {color}")
print("-------------------------------------------")