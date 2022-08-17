
def bucket_sort(arr):
    # 2. create buckets
    bucket = create_bucket(min(arr), max(arr))
    # 3. insert element into buckets
    bucket = insert_into_bucket(arr, bucket)
    # 4. sort the elements of each bucket
    bucket = sort_bucket(bucket)
    # 5. get the sorted elements
    answer = gather(bucket)
    return answer


def create_bucket(min_element, max_element):
    min_quotient = min_element // 10
    max_quotient = max_element // 10
    len_bucket = (max_quotient - min_quotient + 1) * 2
    bucket = [[] for i in range(len_bucket)]
    return bucket


def insert_into_bucket(arr, bucket):
    for i in arr:
        quotient = i // 10
        remainder = i % 10
        bucket_index = quotient * 2
        if remainder > 5:
            bucket_index += 1
        bucket[bucket_index].append(i)
    return bucket


def sort_bucket(bucket):
    for i in range(len(bucket)):
        bucket[i] = sorted(bucket[i])
    return bucket


def gather(bucket):
    answer = []
    for a in bucket:
        for e in a:
            answer.append(e)
    return answer


if __name__ == '__main__':
    # 1. suppose input array (size = 12)
    arr = [4, 14, 27, 3, 19, 22, 26, 6, 15, 8, 16, 11]
    sorted_arr = bucket_sort(arr);
    print(f'sorted arr : {sorted_arr}')