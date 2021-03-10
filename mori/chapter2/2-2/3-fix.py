# 入力
N = int(input())
S = input()

# S[a], S[a+1], ..., S[b]が残っている文字列
a = 0
b = N - 1

T = ''    # 文字列T

while a <= b:
    # 左からみた場合と右から見た場合を比較
    left = False
    for i in range(b - a + 1):    # 0 <= i <= b - a
        if S[a + i] < S[b - i]:
            left = True
            break
        elif S[a + i] > S[b - i]:
            left = False
            break
    # 文字列Tに文字を追加する
    if left:
        T += S[a]
        a += 1
    else:
        T += S[b]
        b -= 1

print(T)