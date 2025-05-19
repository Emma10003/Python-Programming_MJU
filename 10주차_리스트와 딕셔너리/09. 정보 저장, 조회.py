phone = {}   # 딕셔너리 선언

for i in range(5):   # 5번 반복
    # 학번을 정수로 입력받아 저장
    id = int(input(f"{str(i+1)}번째 학생의 학번 입력: "))
    # 전화번호는 문자열로 입력받아 저장
    phone_num = input(f"{str(i+1)}번째 학생의 전화번호: ")
    # 딕셔너리에 추가
    phone[id] = phone_num
    print("추가되었습니다.")
    print()

print("학생 전화번호부가 완성되었습니다.")


id = int(input("검색할 학생의 학번 입력: "))

if id in phone:
    print(f"입력한 학생의 전화번호: {phone[id]}")
else:
    print("입력한 학생의 전화번호가 없습니다.")