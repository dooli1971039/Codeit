wage = 5  # 시급 (1시간에 5달러)
exchange_rate = 1142.16  # 환율 (1달러에 1142.16원)

# "1시간에 5달러 벌었습니다." 출력
print("{}시간에 {}{} 벌었습니다.".format(1, wage * 1, "달러"))

# "5시간에 25달러 벌었습니다." 출력
print("{}시간에 {}{} 벌었습니다.".format(5,wage*5, "달러"))  # 코드를 채워 넣으세요.

# "1시간에 5710.8원 벌었습니다." 출력
print("{}시간에 {}{} 벌었습니다.".format(1,wage*exchange_rate, "원"))  # 코드를 채워 넣으세요.

# "5시간에 28554.0원 벌었습니다." 출력
print("{}시간에 {:.1f}{} 벌었습니다.".format(5,5*wage*exchange_rate, "원"))  # 코드를 채워 넣으세요.
