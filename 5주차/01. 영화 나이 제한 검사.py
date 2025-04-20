limit = 15
print(f"{limit}세 이상만 관람이 가능한 영화입니다.")
age = int(input("나이를 입력하시오: "))

if age>=limit:
    print("이 영화를 보실 수 있습니다.")
else:
    print("이 영화를 보실 수 없습니다.")