n = int(input())
m = int(input())
a = [list(input()) for i in range(n)]

print(a)

count = 0

def dfs(x,y):
  a[x][y] = "."
  for i in [-1,0,1]:
    for j in [-1,0,1]:
      dx = x + i
      dy = y + j
      if 0<=dx<n and 0<=dy<m and a[dx][dy] == "W":
        dfs(dx, dy)



for i in range(n):
  for j in range(m):
    if a[i][j] == "W":
      dfs(i,j)
      count+=1

print(count)