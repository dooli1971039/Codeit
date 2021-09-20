import random

dict={}
list=[]

with open("vocabulary.txt","r",encoding="utf-8") as f:
    for line in f:
        ans = line.strip().split(": ")[0] #영어
        kor = line.strip().split(": ")[1] #한국어
        dict[kor]=ans
        list.append(kor)

while True:
    i=random.randint(0,len(list)-1)
    eng = input("{}: ".format(list[i]))
    if eng=='q' :
        break
    if eng == dict[list[i]]:
        print("맞았습니다!")
    else:
        print("아쉽습니다. 정답은 {}입니다.".format(dict[list[i]]))



###################
import random

# 사전 만들기
vocab = {}
with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.strip().split(": ")
        english_word, korean_word = data[0], data[1]
        vocab[english_word] = korean_word

# 목록 가져오기
keys = list(vocab.keys())   ##### 이런 초방식 기억해두기

# 문제 내기
while True:
    # 랜덤한 문제 받아오기
    index = random.randint(0, len(keys) - 1)
    english_word = keys[index]
    korean_word = vocab[english_word]

    # 유저 입력값 받기
    guess = input("{}: ".format(korean_word))

    # 프로그램 끝내기
    if guess == 'q':
        break

    # 정답 확인하기
    if guess == english_word:
        print("정답입니다!\n")
    else:
        print("아쉽습니다. 정답은 {}입니다.\n".format(english_word))