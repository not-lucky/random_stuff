d = {'R': 'G', 'G': 'B', "B": 'R'}

arr = list(input())
for i in range(int(input())):
    for j in range(len(arr)):
        arr[j] = d[arr[j]]


for i in arr:
    print(i, end='')