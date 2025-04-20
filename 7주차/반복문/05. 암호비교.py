passwd = ""
myPasswd = "pythonisfun"

# while passwd != myPasswd:
#     passwd = input("암호를 입력하시오: ")

# 무한루프와 break를 사용한 while문
while True:
    passwd = input("암호를 입력하시오: ")
    if passwd == myPasswd: break

print("로그인 성공!")