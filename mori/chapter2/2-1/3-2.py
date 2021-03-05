import queue
INF = 1000000
n = int(input())
m = int(input())
a = [list(input()) for i in range(n)]
d = [[INF for i in range(n)] for i in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


class P:
  def __init__(self, x=0,y=0):
    self.x = x
    self.y = y

for i in range(n):
  for j in range(m):
    d[i][j] = INF
    if a[i][j] == "S":
      sx = i
      sy = j
      d[i][j]=0
    if a[i][j] == "G":
      gx = i
      gy = j

def bfs():
  q = queue.Queue()
  q.put(P(sx,sy))
  while q.qsize():
    p = q.get()
    if p.x == gx and p.y == gy:
      break
    for i in range(4):
      nx = p.x + dx[i]
      ny = p.y + dy[i]
      if 0<=nx<n and 0<=ny<m and a[nx][ny] != "#" and d[nx][ny] == INF:
        q.put(P(nx,ny))
        d[nx][ny] = d[p.x][p.y] + 1

  return d[gx][gy]

dd = bfs()

print(dd)

