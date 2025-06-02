'''
1차 문자배열과 비교문, 반복문을 이용하는 문제.

문제의 결과가 O/X로 주어질 때 점수를 구하여 출력하는 함수 작성

규칙 1)
10개의 문자가 'OOXXOXXOOO'같이 주어졌을 때 O는 문제를 맞은 것, X는 틀린 것.

규칙2)
연속하여 맞춘 경우에 점수가 1점씩 올라가고, 문제를 틀리면 해당 문제는 0점이고 점수는 초기화 됨.

OOXXOXXOOO -> 1 + 2 + 0 + 0 + 1 + 0 + 0 + 1 + 2 + 3 = 10점
'''

def solution(s):
    answer = 0
    score = 0
    for x in s:
        if (x=="O"):
            score += 1
        else:
            score = 0
        
        answer += score
    return answer