# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

f = True

for n in range(19, 1000000000000, 19):
    for i in range(2, 20):
        if (n/i) % 1 == 0:
            if i == 19:
                print(n)
                f = False
                break
        else:
            break
    if f == False:
        break


print('This is the number: ', n)

"""
One of the better solutions
i = 1
for k in (range(1, 21)):
    if i % k > 0:
        for j in range(1, 21):
            if (i*j) % k == 0:
                i *= j
                break
print i
"""
