'''
result = {x for x in aList if x%2==0}
: x가 aList에 있고(in aList) 짝수이면(if x%2==0) 그 x를 세트에 추가하는 명령을 반복(for문).
'''

fruit_list = ['사과', '바나나', '포도', '사과', '바나나', '포도', '사과', '바나나', '포도']
fruit_set = {'사과', '바나나', '포도', '사과', '바나나', '포도', '사과', '바나나', '포도'}

# fruit_set에서 과일 이름이 3자리 이상인 것만 리스트에 담은 후 출력하기.
# 원래 하던 방법
result = []
for x in fruit_set:
    if (len(x) >= 3):
        result.append(x)
print(result)

# 함축연산으로 같은 연산 하기.
result = [x for x in fruit_set if len(x)>=3]
print(result)