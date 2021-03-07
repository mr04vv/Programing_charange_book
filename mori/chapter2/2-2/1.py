c1, c5, c10, c50, c100, c500 = map(int, input().split())
a = int(input())

a1 = 0
a5 = 0
a10 = 0
a50 = 0
a100 = 0
a500 = 0

while(a != 0):
  while(a - 500 >= 0 and c500 > 0):
    a500+=1
    c500 -= 1
    a -= 500
  while(a - 100 >= 0) and c100 > 0:
    a100+=1
    c100 -= 1
    a -= 100
  while(a - 50 >= 0 and c50 > 0):
    a50 += 1
    c50 -= 1
    a -= 50
  while(a - 10 >= 0 and c10 > 0):
    a10 += 1
    c10 -= 1
    a -= 10
  while(a - 5 >= 0 and c5 > 0):
    a5 +=1
    c5 -= 1
    a -= 5
  while(a - 1 >= 0 and c1 > 0):
    a1 += 1
    c1 -= 1
    a -= 1

print(a500, a100, a50, a10, a5, a1)
