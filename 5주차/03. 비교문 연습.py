# 1. 나이가 18세 이상이고 25세 이하이면 원래 물건값을 30% 할인.
age = int(input("나이를 입력하시오: "))
price = 10000

if (age>=18) and (age<=25):
    price = int(price*0.7)

print(f"{price}원")


# 2. 국어, 영어, 수학 성적이 모두 70점 이상이거나, 3과목 총합이 230점 이상이면 합격.
kor = int(input("국어 점수: "))
eng = int(input("영어 점수: "))
math = int(input("수학 점수: "))
total = kor + eng + math

if (kor>=70 and eng>=70 and math>=70) or (total >= 230):
    print("합격입니다.")
else:
    print("불합격입니다.")