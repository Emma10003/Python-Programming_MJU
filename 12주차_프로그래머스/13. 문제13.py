'''
두 개의 정수리스트 list1, list2를 인자로 받아서 공통된 원소들만 모은 후, 정렬된 리스트로 반환하는 함수 작성.
- 정렬 방법은 오름차순.
'''

def solution(list1, list2):
    answer = []

    list3 = set(list1) & set(list2)
    answer = list(sorted(list3))
    return answer

list1 = [1, 2, 3]
list2 = [2, 3, 4, 5]
solution(list1, list2)