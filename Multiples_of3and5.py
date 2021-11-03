'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

w = 0
q = 0

for i in range(0, 1000, 3):
    if i in range(0, 1000, 15):
        w = w
    else:
        w = w+i
        print(w)

for x in range(0, 1000, 5):
    q = q+x
    print(q)

print(q+w)
