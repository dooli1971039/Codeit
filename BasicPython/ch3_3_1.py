#사전 : dictionary
#key-value pair
#순서는 상관 없다.
dict={
    5:25,  #키는 5, 값은 25
    2:4,
    3:9
}

print(type(dict))
print(dict[5]) #사전의 key를 쓰면 value가 나옴

dict[9]=81 #없으면 추가됨
dict[5]=1 #있으면 바뀜
print(dict)