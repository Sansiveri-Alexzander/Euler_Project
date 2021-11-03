# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
num = int(input('Choose a number: '))
prime = []


def isPrime(n):

    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True


while True:
    if (isPrime(num)):
        num = int(input('This is a prime number. Input another number: '))
    else:
        break


for n in range(2, num):
    if num/n < 0:
        print('The greatest prime factor is:', max(prime))
        break
    elif num % n != 0:
        while (n**.5) % 1 != 0:
            n += 1
    else:
        num = num/n
        prime.append(n)
        print(n)
