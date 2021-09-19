with open('chicken.txt','r',encoding="utf-8") as f:
    for line in f:
        print(line.strip())

#strip : 화이트 스페이스 지워줌
print("           abd             fwe         ".strip())

#split
str="1. 2. 3. 4. 5. 6." # . 으로 끝나서
print(str.split("."))  #['1', ' 2', ' 3', ' 4', ' 5', ' 6', ''] 이렇게 나옴옴

print("    \n\n    2   \t 3         \n dsd      ".split())


with open("new_file.txt","w") as f:   # w대신 a를쓰면 append이므로 수정, a는 파일이 없을땐 새로 만들어줌
    f.write("Hello!!\n")
