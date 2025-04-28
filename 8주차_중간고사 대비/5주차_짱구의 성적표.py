# 1. 성적을 숫자로 입력받는다.
# 2. 학점을 결정한다. if문에서는 학점을 저장만 함.
# 3. 출력한다.
print("-"*40)
print("짱구의 성적표")

# 성적 입력받기
score = int(input("성적을 입력하세요: "))

# 학점 결정하기
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

# 학점에 '+' 붙이기
if (score==100) or (score%10 >= 5):
    grade += '+'
else:
    grade += '0'

print(f"성적: {score}, 등급: {grade}")