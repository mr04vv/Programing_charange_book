n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
t_tuples = []

for i in range(n):
  t_tuples.append((s[i], t[i]))

t_tuples = sorted(t_tuples, key=lambda t: t[1])

ans = 0
t_t = 0

for i in t_tuples:
  if (t_t < i[0]):
    t_t = i[1]
    ans += 1

print(ans)