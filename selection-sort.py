

def change(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                change(arr, i, j)
                continue


if __name__ == '__main__':
    arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
    selection_sort(arr)
    print(arr)