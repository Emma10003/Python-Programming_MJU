'''
# 8~9번 문제
문자로 정삼각형 출력하기
'''
# 힌트2: 문자열을 이용한다
alphabet = "zyxwvutsrqpnmlkjihgfedcba"

n = int(input())
a = 0
# range를 감소형 또는 증가형으로 사용할 수 있다.
for i in range(1, n+1):
    print(" "*i, end="")
     
    for k in range(n-i+1, 0, -1):
        # alphabet 리스트의 처음부터 순서대로 끝까지 출력
        # 단, a 다음 z가 출력되게 하기 위해 인덱스를 0으로 재생성
        print(alphabet[a], end=" ")
        a += 1
        if (a==len(alphabet)):
            a = 0
    print()