numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
# 코드를 입력하세요.
for i in range(int(len(numbers)/2)):
    tmp=numbers[i]
    numbers[i]=numbers[len(numbers)-1-i]
    numbers[len(numbers)-1-i]=tmp

print("뒤집어진 리스트: " + str(numbers))