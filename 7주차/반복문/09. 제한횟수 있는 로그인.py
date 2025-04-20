id = "Yusung"
pw = "wannagohome"
chance = 5
login_try = 1

while True:   # for문을 사용하면 제한횟수 이상 입력했을 때 안내문구를 출력할 수 없음.
    if login_try > chance:   #제한횟수 이상으로 입력했을 땐 반복문 종료
        print("기회를 모두 사용하셨습니다.")
        break
    input_id = input("아이디: ")
    input_pw = input("패스워드: ")

    if input_id==input or input_pw==pw:
        print(f"로그인 성공!")
        break
    else:
        print(f"id 또는 password가 틀렸습니다. 다시 입력하세요. ({login_try}/{chance})")
        login_try += 1
    
print("로그인 시스템을 종료합니다.")
print("-" * 50)