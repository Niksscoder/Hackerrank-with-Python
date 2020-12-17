'''
You are given a string and your task is to swap cases. In other words, convert all l
owercase letters to uppercase letters and vice versa.

For Example:
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
'''




#first program to solve this progran
s = input().split()
def new(s):
    result = ""
    for i in s:
        if i == i.upper():
            result += i.lower()
        else:
            result += i.upper()
    return result

print(new(s))

# solve this problem with lambda and map:
# if word in upper case we try to change this word to lower case:
print(*map(lambda word: word.lower() if word.isupper() else word.upper(), input()), sep="")

# solve this problem with swapcase:
def swap_case(s):
    return s.swapcase()

