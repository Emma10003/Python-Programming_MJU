# 미리 id와 pw를 설정한다.
# 로그인 기회는 다섯 번.
# 아이디와 패스워드를 입력받는다.
# 로그인 기회를 모두 사용했을 때는 "기회를 모두 사용하셨습니다." 라는 문구 출력.
# 기회 내에 로그인을 성공한 경우에는 "로그인 성공!"을 출력.
# 아이디 혹은 패스워드가 틀린 경우 "id 혹은 password가 틀렸습니다. 다시 입력하세요. (남은 횟수/로그인 기회)"를 출력.
# 반복문이 끝나면 "로그인 시스템을 종료합니다." 출력.

id = "오유성"
pw = "장르를 가지고 싶어"
chance = 5
login_try = 1

while True:    
    if login_try <= chance:
        print("-"*40)
        print(f"{login_try}번째 시도!")
        input_id = input("ID: ")
        input_pw = input("PW: ")
    else:
        print("기회를 모두 사용하셨습니다.")
        break

    if (input_id==id) and (input_pw==pw):
        print("로그인 성공!")
        break
    else:
        print(f"id 혹은 password가 틀렸습니다. 다시 입력하세요. ({login_try}/{chance})")
        login_try += 1

print("로그인 시스템을 종료합니다.")
print("="*40)