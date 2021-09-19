with open("vocabulary.txt","a",encoding="utf-8") as f:

    while True:
        eng = input("영어 단어를 입력하세요:")
        if eng=="q":
            break
        kor = input("한국어 뜻을 입력하세요:")
        f.write("{}: {}\n".format(eng,kor))

