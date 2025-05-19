numbers=[]
n=10 

#숫자 10개를 중복없이 입력받아 numbers에 추가합니다!
#기존에 저장된 숫자는 추가하지 않습니다!
while(True) : 
    if(len(numbers)==n) : break
    num=int(input("숫자를 입력하세요 : "))
    if (num not in numbers ) : numbers.append(num)
    else : print("이미 저장된 숫자에요.")
    print(numbers)

print(numbers)


#정렬하기
print("===== 내림차순 정렬 =====")
numbers.sort(reverse=True)  #내림차순
print(numbers)  

print("===== 오름차순 정렬 =====")
numbers.sort() # 오름차순
print(numbers)