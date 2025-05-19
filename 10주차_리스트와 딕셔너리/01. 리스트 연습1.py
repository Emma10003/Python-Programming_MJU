aa= []   # 빈 리스트 생성! 1차구조. 리스트의 첫번째 인덱스는 0 입니다!
#bb= [ [1,2,3], [4,5,6] ] 2행3열의 2차구조. b[0][0] 은 1, bb[0][2]는 3입니다. 
letters = ['A','B','C','D','E','F']  #문자 리스트 생성과 세팅
food = ["떡볶이", "콜라","사이다","라면", "커피"]  #문자열 리스트 생성과 세팅
numbers =[1,2,3,4,5,6,7,8,9,10]  #정수 리스트 생성과 세팅!

#리스트 이름으로 출력하기
print(aa)
print(letters)
print(food)
print(numbers)

#반복문으로 리스트 항목 방문하며 출력하기
#리스트에 있는 항목의 개수만큼 반복하기 : len(food)  
for i in range(0,len(food)) :    
    print(food[i]) 
#슬라이싱!
print(numbers[3:7])
print(food[1:3])