import math


# def triplets_with_sum(number):
#     triplets = []
#     c = number // 2
#     while c > number // 3:
#         remainder = number - c
#         for i in range(int(remainder / 2), 1, -1):
#             if i >= c or remainder - i >= c:
#                 break
#             if pow(i, 2) + pow(remainder - i, 2) == pow(c, 2):
#                 triplets.append([i, remainder - i, c])
#                 break
#             print(i, remainder - i, c)
#         c -= 1
#     return triplets

def triplets_with_sum(number):
    for a in range(int(number / 3) + 1, 1, -1):
        for b in range(a, 1, -1):
            c = math.sqrt(a ** 2 + b ** 2)
            # print(c, math.floor(c), math.ceil(c))
            if math.floor(c) == math.ceil(c) and int(c) == number - a - b:
                print(a, b, c)

print(triplets_with_sum(30000))