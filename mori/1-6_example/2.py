l = int(input())
n = int(input())
x = list(map(int, input().split()))
minT = 0
maxT = 0
for x_i in x:
  minT = max(minT, min(x_i, l - x_i))
  maxT = max(maxT, max(x_i, l - x_i))

print(minT,maxT)