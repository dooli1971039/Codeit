#리스트 (list)
numbers=[2,3,5,7,11,13]
names=["윤수","혜린","태호","영훈"]

print(numbers)
print(names)

#인덱싱 (indexing)
print(names[1]) #인덱스는 0번부터 시작
print(numbers[1]+numbers[3])
print(numbers[-1])
print(numbers[-2])

#리스트 슬라이싱
print(numbers[0:4]) #인덱스 3까지
print(numbers[2:])
print(numbers[:3]) #인덱스 2까지

#리스트 함수
arr=[]
print(len(arr)) #리스트의 길이를 반환
arr.append(5)
arr.append(3)
print(arr)
print(len(arr))

aaa=[2,3,5,7,11,13,17,19]
del aaa[3]
print(aaa)

aaa.insert(4,37) #4번 인덱스 위치에 37을 추가해라
print(aaa)

#정렬
bb=[19,13,2,5,3,11,7,17]
cc=sorted(bb)  #bb는 바뀌지 않는다.
print(cc)

dd=sorted(bb,reverse=True)
print(dd)

print(bb)

print(bb.sort()) #None이 나온다. =>함수 자체는 아무것도 리턴하지 않아서
print(bb) #bb자체가 정렬된다초