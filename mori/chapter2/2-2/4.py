n = int(input())
r = int(input())
x = list(map(int, input().split()))

cnt = 0
i = 0
while(i<n):
  s = x[i]
  while(i+1 < n and x[i+1] - s <= r):
    i+=1
  p = x[i]
  while(i < n and x[i] - p <= r):
    i+=1
  cnt += 1

print(cnt)  # print(i)
      