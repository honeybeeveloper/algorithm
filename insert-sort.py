
def insert_sort(x):
    for i in range(1, len(x)):
        value = x[i]
        idx = i
        while idx > 0 and x[idx-1] > value:
            x[idx] = x[idx-1]
            idx -= 1
        x[idx] = value
    return x


if __name__ == '__main__':
    arr = [67, 16, 177, 214, 110, 316, 259]
    result = insert_sort(arr)
    print(result)
