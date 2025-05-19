phonebook = {"홍길동":"010-1234-5678",
             "짱구":"010-2134-5596",
             "코난":"010-8829-3215",
             "미란이":"010-3349-9215"}

# 모든 key값 출력하기
print(phonebook.keys())

# 모든 value값 출력하기
print(phonebook.values())

# 이름으로 검색하기. 단, 해당 이름이 키에 있을 때만 찾는다.
# print(phonebook["흰둥이"])
if '흰둥이' in phonebook.keys():
    print(phonebook['흰둥이'])
else:
    print("그런 이름은 없습니다.")
    print("'흰둥이'를 딕셔너리에 추가합니다.")
    phonebook['흰둥이'] = input("전화번호를 입력하세요: ")
    print(phonebook['흰둥이'])