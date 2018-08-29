# 3つの棒を選んだときその３つの棒で三角形が作れるか判定
# 作れる場合、最大の周囲の長さを出力。なければ 0 を出力

bar_num = int(input())
bar_length_list = [int(input()) for i in range(bar_num)]

ans = 0

for i in range(bar_num-2):
    for j in range(i+1,bar_num-1):
        for k in range(j+1,bar_num):
            length = bar_length_list[i] + bar_length_list[j] + bar_length_list[k]
            max_length = max(bar_length_list[i],bar_length_list[j],bar_length_list[k])
            rest = length - max_length
            if rest > max_length:
                ans = max(ans,length)

print(ans)