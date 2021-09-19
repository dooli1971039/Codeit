import random

chance=4
result=random.randint(1,20)
win=False
for i in range(4):
    num=int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요:".format(4-i)))
    if num==result:
        print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(i+1))
        win=True
    elif num>result:
        print("Down")
    else:
        print("Up")

if win==False:
    print("아쉽습니다. 정답은 {}입니다.".format(result))