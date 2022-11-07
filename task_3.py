def is_prime(n):
    if (n<2):
        return False
    else:
        for i in range(n//2):
            if (n%i == 0):
                return False
            else:
                return True


def is_diabolic(n):
    x = str(n)
    if ('666' in x):
        return True


def all_of_them():
    numer = 0
    for i in range(1, 10000):
        if (is_prime(i) and is_diabolic(i)):
            print(i)
            number += 1
    print("ilosc: " + numer)
    
all_of_them()
