'''
요리를 팔았을 때 얻는 이익 계산하는 함수

ex) 빵을 만들기 위한 '밀가루, 우유, 달걀, 버터'의 재료비가 [100,100,100,100]이라면 재료비는 400원,
판매 가격이 500원이라면 이익은 100원

- ingredients: 요리에 필요한 재료의 가격 정보를 담은 정수 배열
- cost: 요리 판매 가격
- cost는 언제나 재료비보다 큰 값으로 주어짐.
'''

def solution(ingredients, cost):
    answer = 0
    # sum = 0
    # for i in ingredients:
    #     sum += ingredients[i]
    answer = cost - sum(ingredients)   # sum()함수를 이용하면 반복문을 사용하지 않아도 된다!

    return answer