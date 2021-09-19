with open('chicken.txt','r',encoding="utf-8") as f:
    day=0
    sum=0
    for line in f:
        sum+=int(line.split()[1])
        day+=1
    print(sum/day)