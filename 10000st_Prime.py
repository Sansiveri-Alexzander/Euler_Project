"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?"""
x = 23
prime = [2, 3, 5, 7]
limit = 3

for n in range(10002):
    q = prime[0]
    for i in range(prime[2]+prime[3]):
        for x in range(len(prime)+1):
            if (i/q) % 1 != 0:
                if q == prime[limit]:
                    prime.append(i)
                    limit += 1
                    print(i)
                    break
                q = prime[+1]
            elif (i/q) % 1 == 0:
                break
        if q == prime[limit]:
            break
