c = list(map(int, input().split()))
a = int(input())
v = [1, 5, 10, 50, 100, 500]

ans = 0
for i in reversed(range(0,6)):
  t = min(a//v[i], c[i])
  a -= v[i] * t
  ans += t

print(ans)