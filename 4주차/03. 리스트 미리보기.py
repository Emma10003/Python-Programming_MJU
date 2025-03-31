# to_do 리스트 3개 이상 입력받아서 리스트에 저장하기
tobuy=[]   # 리스트 선언

goods = input("구매해야 하는 물품을 입력하세요: ")
tobuy.append(goods)   # goods를 tobuy 리스트에 추가
print(tobuy)   # 추가된 값 확인

goods = input("구매해야 하는 물품을 입력하세요: ")
tobuy.append(goods)
print(tobuy)   # 추가된 값 확인

goods = input("구매해야 하는 물품을 입력하세요: ")
tobuy.append(goods)
print(tobuy)   # 추가된 값 확인


# 반복문으로 같은 기능 구현하기
tobuy = []
n = 3
for i in range(n):
    goods = input("구매해야 하는 물품을 입력하세요: ")
    tobuy.append(goods)
    print(f"구매예정 목록: {tobuy}")
print("반복문 완료!")