s = input()
arr = []

cc = s[0]
n = 0

for i in range(len(s)):
    c = s[i]
    if cc == c:
        n += 1
    else:
        if n > 2:
            arr.append((i - n, i - 1))
        cc = c
        n = 1

if n > 2:
    arr.append((len(s) - n, len(s) - 1))

for i in arr:
    print(*i)
