# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

n = 13  # The Prime number

prime = [2, 3, 5, 7, 11, 13]  # list of prime numbers

while len(prime) != 10001:
    n += 1
    q = True  # print(n)
    for x in prime:
        if (float(n/x)/int(n/x)) == 1:
            q = False
            break
    if q == True:
        print(n)
        prime.append(n)


print("This is the 10001st prime number", n)
