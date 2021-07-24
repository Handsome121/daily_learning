n = int(input())
list01 = []
for i in range(n):
    word = input()
    list01.append(word)
list01.sort()
for j in list01:
    print(j)
