"""
sample input txt

10 12
W........WW.
.WWW.....WWW
....WW...WW.
.........WW.
.........W..
..W......W..
.W.W.....WW.
W.W.W.....W.
.W.W......W.
..W.......W.
"""

from pprint import pprint
# -- INPUT ---
n, m = [int(i) for i in input().split()]
water_pool_map = []
water_pool_map.append(['-' for _ in range(m+2)])
for i in range(n):
    row = list("-"+input()+"-")
    if len(row) == m+2:
        water_pool_map.append(row)
    else:
        print("len() of line", i, "doesn't match with", m)
water_pool_map.append(['-' for _ in range(m+2)])

pprint(water_pool_map)

# -- PROCESSING --
def look_around(i, j, count, map):
    for k in range(i-1, i+2):
        for l in range(j-1, j+2):
            if k == i and l == j:
                pass
            elif map[k][l] == "-":
                pass
            elif map[k][l] == ".":
                map[k][l] = "-"
            elif map[k][l] == "W":
                map[k][l] = str(count)
                look_around(k, l, count, map)
            elif map[k][l].isdecimal():
                if str(map[k][l]) == count:
                    print("something wrong! check your program!")
    return

count = 0
for i in range(1, n+2):
    for j in range(1,m+2):
        if water_pool_map[i][j] == 'W':
            count += 1
            print("\nLAKE 1")
            water_pool_map[i][j] = str(count)
            look_around(i, j, count,water_pool_map)
            pprint(water_pool_map)

print("Num of Lakes =", count)
