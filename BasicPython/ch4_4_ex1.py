from random import randint

#1~45 사이의 서로 다른 번호 n 개 뽑음
def generate_numbers(n):
    list=[]
    for i in range(n):
        num=randint(1,45)
        if num in list:
            i=-1
            continue
        else:
            list.append(num)

    return list


#일반 당첨 번호 6개와 보너스 번호 1개가 포함된 리스트를 리턴합니다.
#일반 당첨 번호 6개는 정렬되어 있어야 하고, 보너스 번호는 마지막에 추가하면 됩니다.
def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]


#파라미터로 리스트 list_1과 리스트 list_2를 받고, 두 리스트 사이에 겹치는 번호 개수를 리턴합니다.
def count_matching_numbers(list1,list2):   #두번째가 정답쪽
    count=0
    for i in list1:
        if i in list2:
            count+=1

    return count

def check(numbers,winning_list):
    count = count_matching_numbers(numbers, winning_list[:6])
    bonus = count_matching_numbers(numbers, winning_list[6:])
    if count == 6:
        return 1000000000
    elif count == 5:
        if bonus == 1:
            return 50000000
        else:
            return 10000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0
    
numbers = generate_numbers(6)
winning_list = draw_winning_numbers()
print(check(numbers,winning_list))





