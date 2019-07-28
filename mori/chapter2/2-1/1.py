n = int(input())
a = list(map(int, input().split()))
k = int(input())
def dfs(i, sum):
  if i == n:
    if sum == k:
      print("Yes")
      exit(0)
  else:
    dfs(i+1, sum+a[i])
    dfs(i+1, sum)
dfs(0,0)
print("No")