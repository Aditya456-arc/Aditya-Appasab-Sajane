def generate_odd_series(a):
    if a<3:
        print(1)
    else:
        result=[]
        for i in range(a):
            result.append(2*i+1)
        print(*result)
a = int(input("Enter a number: "))
generate_odd_series(a)
