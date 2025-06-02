'''
이름이 문자열 리스트로 주어질 때, 각 이름의 가운데 글자를 *로 바꾸는 함수 작성
ex)
['홍길동', '신짱구'] -> ['홍*동','신*구']
'''

def solution(stdList):
    answer = []
    #필요한 코드를 작성하세요
    # for i in range(len(stdList)):
    #     name = list(stdList[i])
    #     name[1] = "*"
    #     name = ''.join(name)
    #     answer.append(name)

    for name in stdList:
        answer.append(name[0]+'*'+name[2])

    return answer

sList = ['홍길동', '신짱구']
print(solution(sList))