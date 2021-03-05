n = int(input())
m = int(input())

a=[list(list(input())) for i in range(n)]

def dfs(x,y):
  a[x][y] = "."
  for dx in [-1,0,1]:
    for dy in [-1,0,1]:
      nx = x + dx
      ny = y + dy
      if 0<=nx<n and 0<=ny<m and a[nx][ny] == "W":
        dfs(nx,ny)


count = 0
for i in range(n):
  for j in range(m):
    if a[i][j] == "W":
      dfs(i,j)
      count+=1

print(count)