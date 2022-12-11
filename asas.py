nnum = input()  # Reading input from STDIN
a = []
even = True if len(nnum) % 2 == 0 else False
if even:
    for i in range(len(nnum) // 2):
        a.append(nnum[i] + nnum[-1 - i])
else:
    for i in range(len(nnum) // 2):
        a.append(nnum[i] + nnum[-1 - i])
    a.append(nnum[len(nnum) // 2])
b = [int(i) for i in a]
print(sum(b))
