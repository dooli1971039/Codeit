#리스트 안에 리스트가 올 수 있다
# 세 번의 시험을 보는 수업
grades = [[62, 75, 77], [78, 81, 86], [85, 91, 89]]

# 첫 번째 학생의 성적
print(grades[0])

# 세 번째 학생의 성적
print(grades[2])

# 첫 번째 학생의 첫 번째 시험 성적
print(grades[0][0])

# 세 번째 학생의 두 번째 시험 성적
print(grades[2][1])

# 첫 번째 시험의 평균
print((grades[0][0] + grades[1][0] + grades[2][0]) / 3)

#정렬
# 1. sorted(list) , sorted(list,reverse=True)  <= list가 변하지는 않는다
# 2. list.sort() 리스트 자체가 변한다.
numbers = [5, 3, 7, 1]
numbers.sort()
print(numbers)


# list.reverse() 는 리스트의 앞뒤를 뒤집어 배치한다.
numbers = [5, 3, 7, 1]
numbers.reverse()
print(numbers)


#index 메소드
#list.index(X) 는 X의 인덱스를 리턴한다.
members = ["영훈", "윤수", "태호", "혜린"]
print(members.index("윤수"))
print(members.index("태호"))


#remove메소드
# list.remove(X)는 list에서 첫번째로 X의 값을 갖고 있는 원소를 삭제해준다.
fruits = ["딸기", "당근", "파인애플", "수박", "참외", "메론"]
fruits.remove("파인애플")
print(fruits)