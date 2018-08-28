# 3つの棒を選んだときその３つの棒で三角形が作れるか判定
# 作れる場合、最大の周囲の長さを出力。なければ 0 を出力

bar_num = int(input())
bar_length_list = [int(input()) for i in range(bar_num)]

ans = 0

for i in range(bar_num-2):
    first = bar_length_list[i]
    for j in range(i+1,bar_num-1):
        second = bar_length_list[j]
        for k in range(j+1,bar_num):
            third = bar_length_list[k]
            if (first**2 == second**2 + third**2) or (second**2 == first**2 + third**2) or (third**2 == first**2 + second**2):
                ans = first+second+third
            
print(ans)