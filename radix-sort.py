
def radix_sort(arr):
    max1 = max(arr)
    len_max = len(str(max1))

    exp = 1
    while max1 / (10 ** (exp-1)) >= 1:
        arr = counting_sort(arr, exp, len_max)
        exp += 1

    return [j for i in arr for j in i]


def counting_sort(arr, exp, len_max):
    bucket = [[], [], [], [], [], [], [], [], [], []]
    for i in arr:
        if isinstance(i, list):
            for j in i:
                idx = str(j).zfill(len_max)[-1 * exp]
                bucket[int(idx)].append(j)
        else:
            idx = str(i)[-1 * exp]
            bucket[int(idx)].append(i)

    return bucket


if __name__ == '__main__':
    arr = [754, 114, 27, 300, 99, 22, 226, 346, 145, 458, 917, 30]
    result = radix_sort(arr)
    print(result)

    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    result = radix_sort(arr)
    print(result)