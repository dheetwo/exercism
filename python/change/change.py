def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")
    remainder = target
    coins_list = sorted(coins)
    target_list = []
    while remainder >= 0:
        if remainder == 0:
            return target_list
        while len(coins_list) > 0:
            if coins_list[-1] <= remainder:
                target_list.append(coins_list[-1])
                remainder -= coins_list[-1]
            else:
                coins_list.pop(-1)








find_fewest_coins([3, 4, 8], 10)

