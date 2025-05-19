english_dict = dict()
num = int(input("입력할 단어의 개수: "))

i = 0
while i < num:
    english_word = input(f"추가할 영단어를 입력하시오 ({i+1}/{num}): ")
    if english_word in english_dict:
        print("이미 사전에 존재하는 단어입니다. 다시 입력하세요.")
        continue
    else:
        korean_word = input("영단어의 뜻을 입력하시오: ")
        english_dict[english_word] = korean_word
        print("✅ 추가되었습니다.")
        i += 1
        print()

print(english_dict)

word = input("검색할 단어를 입력하시오: ")
print(english_dict[word])