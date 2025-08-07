def generate_odds(a):
    for i in range(1, a * 2, 2):
        print(i, end=" ")
a = int(input("Enter a number: "))
generate_odds(a)
