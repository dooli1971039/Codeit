a=1 #앞에꺼
b=1 #뒤에꺼
i=1 #반복문 변수

print(a)
while i<50:
    print(b)
    tmp=a
    a=b
    b=b+tmp
    i+=1

##########################초
previous = 0
current = 1
i = 1

while i <= 50:
    print(current)
    temp = previous  # previous를 임시 보관소 temp에 저장
    previous = current
    current = current + temp  # temp에는 기존 previous 값이 저장돼 있음
    i += 1

#########################
previous = 0
current = 1
i = 1

while i <= 50:
    print(current)
    previous, current = current, current + previous
    i += 1