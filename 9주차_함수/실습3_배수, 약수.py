# 실습 3: x가 y의 배수인가?
def checkNumber(x, y):
    if(x==0):
        return "Yes"
    if(x!=0 and y==0):
        return "No"
    if(x%y==0):
        return "Yes"
    
num1 = int(input("정수1: "))
num2 = int(input("정수2: "))
print(checkNumber(num1, num2))