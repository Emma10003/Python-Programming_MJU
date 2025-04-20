age = int(input("나이를 입력하시오: "))
height = int(input("키를 입력하시오(ex. 140): "))

if (age>=10) and (height>=140):
    print("놀이기구를 탈 수 있다.")   # 조건 둘 다 참인 경우
else:
    print("놀이기구를 탈 수 없다.")