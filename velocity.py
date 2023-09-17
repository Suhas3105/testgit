def velocity(time):
    k=int(input("constant in the function: "))
    n= int(input("Degree of time: "))
    a = k*pow(time,n)
    v=(k*pow(time,n+1)/(n+1))
    print(a)
    print(v)


velocity(5)
