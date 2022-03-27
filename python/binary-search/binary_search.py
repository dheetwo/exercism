def find(search_list, value):
    low = 0
    high = len(search_list) - 1
    found = False
    while low <= high and not found:
        mid = (low + high) // 2
        if search_list[mid] == value:
            found = True
            return mid
        else:
            if value < search_list[mid]:
                high = mid - 1
            else:
                low = mid + 1
    if not found:
        raise ValueError("value not in array")
