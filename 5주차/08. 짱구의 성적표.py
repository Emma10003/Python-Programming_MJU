# 1. 성적을 숫자로 입력받는다.
# 2. 학점을 결정한다. if문에서는 학점을 저장만 함.
# 3. 출력한다.

print("-"*40)
print("짱구의 성적표")

score = int(input("성적을 입력하시오: "))

if score>=90 and score<=100:
    grade = 'A'
elif score>=80 and score<90:
    grade = 'B'
elif score>=70 and score<80:
    grade = 'C'
elif score>=60 and score<70:
    grade = 'D'
elif score<60:
    grade = 'F'
else:
    print("0~100 사이의 점수를 입력하시오.")

# 학점에 + 붙이기.
if score>=60:
    if score==100 or score%10>=5:   # 100, 99~95, 89~85, 79~75, 69~65점에 대해서는 +를 붙임.
        grade += "+"
    else:
        grade += "0"


try: 
    print  (f"점수: {score},학점: {grade}")
except:
    print("다시 입력하세요.")