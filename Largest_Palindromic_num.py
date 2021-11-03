"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""
"""
num=[]

for n in range(998001,1,-1):
  num.clear
  num=[int(x) for x in str(n)]
  if num == num[::-1]:
    num=[str(x) for x in str(n)]
    i=int("".join(num))
    for x in range(1000,900,-1):
      if (i/x)%1==0:
        print(i)
        break"""

num = []

for n in range(999, 900, -1):
    for x in range(999, 900, -1):
        num.clear()
        i = n*x
        num = [int(x) for x in str(i)]
        if num == num[::-1]:
            if i > 900000:
                print(i)
