def solution(M):
    answer = 0

    # i의 분해합을 구한 후,
    # i의 생성자가 M이라면, 즉 M과 i의 분해합이 같으면 i를 리턴.

    for i in range(1, 1000001):
        result = i
        # 문자열을 이용해 분해합 구하기: 숫자를 문자열로 변환 후 각 자리수 누적합
        values = str(i)
        for v in values:   # v로 문자열 values의 자리를 읽어옴
            result += int(v)
        if (result==M):
            return i
    
    # 아래는 위와 같은 방법으로 sum 합수와 반복문의 함축표현 사용.
    # for i in range(1, 1000001):
    #     values = str(i)
    #     result = sum(int(v) for v in values) + i
        
    #     if (result==M):
    #         return i
    
    return answer