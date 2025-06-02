# 세트의 원소 개수
fruit_list = ['사과', '바나나', '포도', '사과', '바나나', '포도', '사과', '바나나', '포도']
fruit_set = {'사과', '바나나', '포도', '사과', '바나나', '포도', '사과', '바나나', '포도'}

print(len(fruit_list))   # 리스트 요소의 개수
print(len(fruit_set))   # 세트 요소의 개수


# 세트 요소 추가, 삭제: .add, .remove
fruit_set.add("딸기")
fruit_set.add("수박")
fruit_set.add("키위")


# 세트의 정렬
for x in sorted(fruit_set):   # 그냥 fruit_set으로 하면 실행할 때 마다 순서가 다르게 출력됨 -> sorted로 정렬.
    print(x, end=",")
    # 세트에 대해서는 sort함수를 지원하지 않으므로 sorted를 사용해야 한다.
    # 리스트는 sort함수 사용 가능.
print()

# 과일 이름을 입력받고, 세트에 있으면 삭제/없으면 추가
fruit = input("과일 이름을 입력하세요: ")

if fruit in fruit_set:
    fruit_set.remove(fruit)   # 있으면 삭제
    print("삭제되었습니다!")
else:
    fruit_set.add(fruit)   # 없으면 추가
    print("추가되었습니다!")

print(sorted(fruit_set))

# 세트 요소 전체 삭제: .clear()