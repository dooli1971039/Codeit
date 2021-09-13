money=50000000
year=1988

while year<2016:
    year += 1
    money=money*1.12

money2=1100000000

if money>money2:
    print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(int(money-money2)))
else:
    print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(int(money2 - money)))

###################################################################################################
# 상수 정의
INTEREST_RATE = 0.12
APARTMENT_PRICE_2016 = 1100000000

# 변수 정의
year = 1988
bank_balance = 50000000

while year < 2016:
    bank_balance = bank_balance * (1 + INTEREST_RATE)
    year += 1

if bank_balance > APARTMENT_PRICE_2016:
    print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(int(bank_balance - APARTMENT_PRICE_2016)))
else:
    print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(int(APARTMENT_PRICE_2016 - bank_balance)))