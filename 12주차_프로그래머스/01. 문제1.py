'''
이름의 가운데 글자를 *으로 바꾸어 반환하는 함수 만들기
ex) 신짱구 -> 신*구
'''

def solution(name):
    #필요한 코드를 작성하세요
    # name = list(name)
    # name[1] = '*'
    # answer = ''.join(name)
    answer = name[0] + '*' + name[2]
    
    return answer

print(solution("신짱구"))