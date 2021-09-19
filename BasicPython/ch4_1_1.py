# 모듈 쓰는 법
# import ~~~ as ALLIAS

# from ~~ import 함수명,함수명 ...

# from ~~ import *


# standard library (표준 라이브러리)
import math
print(math.log10(100))
print(math.cos(0))
print(math.pi)


import random
print(random.random()) #0~1
print(random.randint(1, 20)) #1~20 정수 리턴. 이건 양쪽을 다 포함함
print(random.uniform(0, 1))  #리턴하는 값이 소수. 양쪽을 다 포함함


import os
print(os.getcwd())
print(os.getlogin())


import datetime  #날짜와 시간을 다루기 위한 다양한 '클래스'를 갖추고 있다
pi_day = datetime.datetime(2020, 3, 14)  #2020년 3월 14일을 파이썬으로 어떻게 표현할 수 있을까
print(pi_day)
print(type(pi_day))


pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)  #시간은 자동으로 00시 00분 00초로 설정되었는데요. 우리가 시간까지도 직접 정할 수 있다.
print(type(pi_day))


today = datetime.datetime.now()  #우리가 날짜와 시간을 정해 주는 게 아니라, 코드를 실행한 '지금 이 순간'의 날짜와 시간을 받아 오고 싶다면?
print(today)
print(type(today))


today = datetime.datetime.now()  #두 datetime 값 사이의 기간을 알고 싶으면, 마치 숫자 뺄셈을 하듯이 그냥 빼면 됩니다.
pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(today - pi_day)
print(type(today - pi_day))


today = datetime.datetime.now()
my_timedelta = datetime.timedelta(days=5, hours=3, minutes=10, seconds=50)
print(today)
print(today + my_timedelta)


today = datetime.datetime.now()
print(today)
print(today.year)  # 연도
print(today.month)  # 월
print(today.day)  # 일
print(today.hour)  # 시
print(today.minute)  # 분
print(today.second)  # 초
print(today.microsecond)  # 마이크로초


today = datetime.datetime.now()
print(today)
print(today.strftime("%A, %B %dth %Y"))


# %a	요일 (짧은 버전)	Mon
# %A	요일 (풀 버전)	Monday
# %w	요일 (숫자 버전, 0~6, 0이 일요일)	5
# %d	일 (01~31)	23
# %b	월 (짧은 버전)	Nov
# %B	월 (풀 버전)	November
# %m	월 (숫자 버전, 01~12)	10
# %y	연도 (짧은 버전)	16
# %Y	연도 (풀 버전)	2016
# %H	시간 (00~23)	14
# %I	시간 (00~12)	10
# %p	AM/PM	AM
# %M	분 (00~59)	34
# %S	초 (00~59)	12
# %f	마이크로초 (000000~999999)	413215
# %Z	표준시간대	PST
# %j	1년 중 며칠째인지 (001~366)	162
# %U	1년 중 몇 주째인지 (00~53, 일요일이 한 주의 시작이라고 가정)	35
# %W	1년 중 몇 주째인지 (00~53, 월요일이 한 주의 시작이라고 가정)	35