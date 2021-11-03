'''
Find the difference between the sum of the squares of the first n natural numbers and the square of the sum.
'''

x = 0
y = 0
for n in range(101):
    x += n**2

q = []
for i in range(101):
    q.append(i)
y = sum(q)**2

print(y-x)
