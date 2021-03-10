n = int(input())
s = input()
t = ""

for i in range(n):
  for i in range(n//2):
    idx = len(s)-(i+1)
    if s[i] == s[idx] and i != idx:
      continue
    if s[i] < s[idx]:
      t += s[0]
      s = s[1:]
      break
    else:
      t += s[len(s)-1]
      s = s[0:len(s)-1]
      break


print(t)