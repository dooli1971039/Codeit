from random import randint


def generate_numbers():
    numbers = []
    i=1
    # 코드를 작성하세요.
    while i<=3:
        num=randint(0,9)
        if num not in numbers:
            numbers.append(num)
            i += 1


    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    i = 1
    # 코드를 작성하세요.
    while i <= 3:
        num=int(input("{}번째 숫자를 입력하세요: ".format(i)))
        if num<0 or num>9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif num in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(num)
            i+=1

    return new_guess

def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    for i in range(0,3):
        if guess[i]== solution[i]:
            strike_count+=1
        elif guess[i] in solution:
            ball_count+=1
        else:
            continue

    return strike_count, ball_count


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

# 코드를 작성하세요.
while True:
    list = take_guess()
    a,b=get_score(list,ANSWER)
    print("{}S {}B".format(a,b))
    tries+=1
    if a==3:
        break


print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
