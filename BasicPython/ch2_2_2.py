#함수의 실행 순서
#함수를 정의한다고 해서 실행되는 것은 아니다.
def hello():
    print("Hello")
    print("World")

print("함수 호출 전")
hello()
print("함수 호출 후")

def square(x):
    return x*x      #return 문 뒤에 적힌 코드는 절대 실행되지 않는다.

print("함수 호출 전")
print(square(3)+square(4))
print("함수 호출 후")

# return 문의 역할
# 1. 함수 즉시 종료하기  2. 값 돌려주기