
def change(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def exchange_sort(x):
    for i in range(len(x)):
        idx = i
        for j in range(idx+1, len(x)):
            if x[idx] > x[j]:
                change(x, idx, j)
            idx = j
    return x


if __name__ == '__main__':
    arr = [67, 16, 177, 214, 110, 316, 259]
    result = exchange_sort(arr)
    print(result)

