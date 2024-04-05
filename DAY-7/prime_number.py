def prime_checker(number):
    is_prime = True

# Number 2 Indicates Number Starts From 2
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a Prime Number")
    else:
        print("It,s Not a Prime Number")

number = int(input("Check This Number\n"))
prime_checker(number)
