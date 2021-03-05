n = int(input())
a = list(map(int, input().split()))
k = int(input())

ans = 0

def dfs(i, s):
  if i == n:
    return  k == s
  if dfs(i+1, s):
    return True
  if dfs(i+1, s+a[i]):
    return True
  return False



res = dfs(0,0)
print(res)