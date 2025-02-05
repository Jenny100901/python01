def filter_list(lst):
    result = []
    for x in lst:
        if isinstance(x, int):
            result.append(x)
    return result

def filter_list1(lst):
    return [x for x in lst if isinstance(x, int)]

def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))