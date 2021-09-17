def mask_security_number(security_number):
    # 코드를 입력하세요.
    st=security_number[0:-4]
    st=st+"****"
    return st

# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))



#################
def mask_security_number(security_number):
    # security_number를 리스트로 변환
    num_list = []
    for i in range(len(security_number)):
        num_list.append(security_number[i])

def mask_security_number(security_number):
    # security_number를 리스트로 변환
    num_list = list(security_number)

    # 마지막 네 값을 *로 대체
    for i in range(len(num_list) - 4, len(num_list)):
        num_list[i] = "*"

        # 리스트를 문자열로 복구
        total_str = ""
        for i in range(len(num_list)):
            total_str += num_list[i]

        return total_str


#################################
units = ["cm", "m", "yard"]
units_to_string = ', '.join(units)

print(type(units_to_string))
print(units_to_string)


def mask_security_number(security_number):
    num_list = list(security_number)

    # 마지막 네 값을 *로 대체
    for i in range(len(num_list) - 4, len(num_list)):
        num_list[i] = '*'

    # 리스트를 문자열로 복구하여 반환
    return ''.join(num_list)