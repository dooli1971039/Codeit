#문자열 포맷팅

year=2021
month=10
day=29

print("오늘은 2019년 10월 29일 입니다.")
print("오늘은 "+str(year)+"년 "+str(month)+"월 "+str(day)+"일 입니다.")
print("오늘은 {}년 {}월 {}일 입니다.".format(year,month,day))

date_string="오늘은 {}년 {}월 {}일 입니다."
print(date_string.format(year,month,day))
print(date_string.format(year,month,day+1))

print("저는 {},{},{}를 좋아합니다.".format("박지성","유재석","빌게이츠"))
print("저는 {0},{1},{2}를 좋아합니다.".format("박지성","유재석","빌게이츠"))
print("저는 {1},{0},{2}를 좋아합니다.".format("박지성","유재석","빌게이츠"))

num1=1
num2=3
print("{0} 나누기 {1}은 {2}입니다.".format(num1,num2,num1/num2))
print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num1,num2,num1/num2))
# .2f 는 소수 두번째 자리까지 나타내라 (3번째 자리에서 반올림 해라)


#1번
name = "최지웅"
age = 32
print("제 이름은 %s이고 %d살입니다." % (name, age))

#2번
name = "최지웅"
age = 32
print("제 이름은 {}이고 {}살입니다.".format(name, age))

#3번 - 파이썬 버전 3.6부터 새롭게 나온 방식
name = "최지웅"
age = 32
print(f"제 이름은 {name}이고 {age}살입니다.")