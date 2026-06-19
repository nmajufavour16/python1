try:
    while True:
        a = int(input("Enter a number: "))
        b = int(input("Enter a second number: "))
        if a > b:
            print(a/b)
        elif b > a:
            print(a**(-b))
        elif a == b:
                print(a*b)
        pass
except ValueError:
    print("Only numbers nau")
except ZeroDivisionError:
    print("You wan divide with zero, ke?")