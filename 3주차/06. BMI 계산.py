# 신장과 체중을 입력받아서 BMI 값을 출력
weight = float(input("몸무게를 kg 단위로 입력하시오: "))
height = float(input("키를 미터 단위로 입력하시오 (ex. 1.87): "))
bmi = weight / (height**2)
print(f"BMI값: {bmi:.2f}")