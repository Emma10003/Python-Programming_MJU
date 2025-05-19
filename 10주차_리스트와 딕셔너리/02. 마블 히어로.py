#마블 히어로 인원을 입력받아서 리스트에 추가하고 출력하기!
n = int(input("마블 히어로 인원 : "))

#n만큼 이름을 입력받아 heroes에 추가합니다.!
heroes=[]

for i in range(n) :    
    name= input("히어로 이름 ["+ str(i+1) +"] : ")
    heroes.append(name)
    print(heroes)

print(heroes)