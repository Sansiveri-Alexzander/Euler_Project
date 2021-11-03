my_string = input('givme: ')
vowels = ["a", "e", "i", "o", "u"]
vowelcount = 0

for char in my_string:
    if char in vowels:
        vowelcount += 1
    else:
        vowelcount = 0
    if vowelcount == 2:
        print('Yes')
        break
else:
    print("No")
