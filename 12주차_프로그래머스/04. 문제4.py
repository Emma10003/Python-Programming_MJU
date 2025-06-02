'''
좌석 10개
- 좌석의 예약상태가 주어진 reservation 리스트와 좌석번호 n을 인자로 받기
- 해당 공간이 빈자리여서 예약이 가능하다면 '가능' 리턴
- 해당 공간이 이미 예약된 자리여서 불가능하다면 '불가능' 리턴
* reservation 리스트는 0과 1로 저장됨, 0:예약안됨 1:예약됨
ex)
[0,0,0,0,0,0,0,0,0,0], 1 -> '가능'
'''

def solution(reservation, n):
    answer = ''
    #필요한 코드를 작성하세요
    if reservation[n-1] == 0:
        answer = '가능'
    else:
        answer = '불가능'
    
    return answer