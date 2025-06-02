'''
2개의 문자열을 입력받아 두 문자열이 얼마나 유사한지 측정하는 프로그램 작성.
- 표절률은 반올림하여 소수점 셋째자리까지 나타낸다.
- 단, 영문일 경우 모두 소문자/대문자로 변경한 후 비교한다.
    - lower() 혹은 upper() 함수 사용할 것.
- 표절률: (고유 단어 개수) / (전체 단어 개수)
'''
# 입력
s1 = input("첫 번째 문장: ")
s2 = input("두 번째 문장: ")


# 문자열 소문자로 바꾸기
s1 = s1.lower()
s2 = s2.lower()


# 띄어쓰기로 구분해서 문자열 분리 후 리스트에 저장
s1_list = s1.split(" ")
s2_list = s2.split(" ")


# 각 리스트에서 온점은 제거하기
s1_words = []
for x in s1_list:
    if '.' in x:
        x = x.rstrip('.')
    s1_words.append(x.strip())

s2_words = []
for x in s2_list:
    if '.' in x:
        x = x.rstrip('.')
    s2_words.append(x.strip())


# 고유한 단어 구하기
s1_unique = set(s1_words)
s2_unique = set(s2_words)

# 일치하는 단어 구하기: 교집합 연산
same_words = s1_unique & s2_unique

# 표절률 구하기 (s1 기준)
plagiarism_rate = len(same_words) / len(s1_list)
print(f"✅ 표절률: {plagiarism_rate:.3f}")