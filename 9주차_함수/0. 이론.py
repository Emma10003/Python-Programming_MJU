'''
<이론 정리>

함수(function): 프로그램의 규모가 커질 때, 프로그램을 작은 단위로 나눈 것. 입력을 받고 출력을 내보낸다.
    인자: 입력값
        - 디폴트 인자: 매개변수의 기본값, msg=""로 설정. msg 자리에 입력값이 들어오지 않는 경우 기본적으로 출력하는 값.
        - 키워드 인자: 인수의 이름을 명시적으로 지정해서 전달. 이름으로 지정하므로 인자 순서대로 전달하지 않아도 O.
    리턴값: 함수를 실행했을 때 반환하는 값 (함수는 실행이 끝나면 호출된 지점으로 돌아가서 함수의 결과값(리턴값)을 전달한다.)
        - 리턴값을 여러 개 전달할 수 있다. 2-3개보다 많은 수의 리턴값을 반환하는 경우 리스트에 담음.
    - 내장함수: 파이썬에서 미리 구현해 둔 함수
    - 사용자 정의 함수: 사용자가 프로그램 작성 시 특정 기능을 구현한 함수

함수 정의
def 함수이름 (매개변수):  -> 헤더
    실행문1             -> 바디
    실행문2
    ...
함수 호출
함수이름(변수)

변수의 범위
    전역변수: 함수 외부에서 선언되는 변수
    지역변수: 함수 내부에서 선언되는 변수 -> 함수 내에서만 유효
        - global 변수명: 함수 내에서 선언되는 변수를 전역변수로 쓰기 위해서 global 키워드 작성.

모듈: 서로 관련있는 코드블럭을 모아둔 파일. 보통 함수가 들어있음. (종류: 표준모듈, 생성모듈, 서드파티 모듈)
    예) import random, import pandas, ...(파이썬 패키지의 표준모듈)
    용도별로 파일을 분리하고 import하여 사용.
    - 모듈 사용 방법
        import 모듈 -> 모듈 내의 전체 코드를 가져옴
        from 모듈 import 함수명 -> 모듈 내에서 호출한 함수만 가져옴
'''

# 함수 작성하고 호출하기
def print_address(name):
    print("서울시 서대문구 거북골로 34")
    print("명지대학교")
    print(name)

print_address("방목기초교육관")


# 여러 개의 인자
def get_sum(start, end):
    sum = 0
    for i in range(start, end+1):
        sum += i
    return sum

print(get_sum(1,10))


# 디폴트 인자
def greet(name, msg="좋은 아침!"):
    print(f"안녕 {name}, {msg}")

greet("유성")
greet("유성", "뭐해?")


# 키워드 인자
def calc(x, y, z):
    return (x+y)*z

result = calc(y=20, x=10, z=30)  # 함수에 정의 된 인자 순서가 아니라 이름을 지정해 인수 입력.
print(result)


# 여러 개의 리턴값
def BigSmall(a, b):
    if a > b:
        big = a
        small = b
    else:
        big = b
        small = a
    return big, small

print(BigSmall(3, 10))