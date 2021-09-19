with open("vocabulary.txt","r",encoding="utf-8") as f:
    for line in f:
        ans = line.strip().split(": ")[0]
        kor = line.strip().split(": ")[1]
        eng = input("{}: ".format(kor))
        if eng==ans:
            print("맞았습니다!")
        else:
            print("아쉽습니다. 정답은 {}입니다.".format(ans))



#####################
with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.strip().split(": ")
        english_word, korean_word = data[0], data[1]  #### 이렇게 간단하게 가능.

        # 유저 입력값 받기
        guess = input("{}: ".format(korean_word))

        # 정답 확인하기
        if guess == english_word:
            print("정답입니다!\n")
        else:
            print("아쉽습니다. 정답은 {}입니다.\n".format(english_word))