# 深さ優先探索

list_of_numbers = [int(i) for i in input().split()]
target_num = int(input())

def calc(i, target, sum = 0):
    sum_plus_i = sum + list_of_numbers[i]

    if sum_plus_i == target:
        return True

    if i < len(list_of_numbers)-1:
        return calc(i+1, target, sum) or calc(i+1, target, sum_plus_i)

    return False

print(calc(0, target_num))
