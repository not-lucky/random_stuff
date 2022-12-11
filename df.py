input()
arr = list(map(int, input().split()))
x = int(input())

l = len(arr)
dic = {}

for i in range(l):
    for j in range(i + 1, l):
        for k in range(j + 1, l):

            dic[abs(x - (arr[i] + arr[j] + arr[k]))] = arr[i] + arr[j] + arr[k]
print(dic[sorted(dic.keys())[0]])
