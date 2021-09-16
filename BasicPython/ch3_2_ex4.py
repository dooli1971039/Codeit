for i in range(1,400):
    for j in range(i,400):
        num=400-(i+j)
        if i**2+j**2==num**2:
            print(i*j*num)
            break