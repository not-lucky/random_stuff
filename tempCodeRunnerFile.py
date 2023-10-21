
_, *a = input(), Counter(map(int, input().split()))
# print(a[0])
money = 0
for i in range(int(input())):
    x = list(map(int, input().split()))
    if a[x[0]] != 0:
        money += a[x[0]]
        a[x[0]] = a.get(x[0], 1) - 1

print(money)
