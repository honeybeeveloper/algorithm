
def countingSort(arr, exp1):
    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    for i in range(0, len(arr)):
        arr[i] = output[i]


# Method to do Radix Sort
def radixSort(arr):
    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp >= 1:
        countingSort(arr, exp)
        exp *= 10

    return arr


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

    arr = [754, 114, 27, 300, 99, 22, 226, 346, 145, 458, 917, 30]
    result = radixSort(arr)
    print(result)