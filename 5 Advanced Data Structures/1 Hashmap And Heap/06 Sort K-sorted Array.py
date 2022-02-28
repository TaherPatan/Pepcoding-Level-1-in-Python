import heapq


def sort_k_sorted(arr1, k):
    pq = arr1[:k]
    heapq.heapify(pq)
    for idx in range(k, len(arr1)):
        heapq.heappush(pq, arr1[idx])
        arr1[idx - k] = heapq.heappop(pq)
    while pq:
        idx += 1
        arr1[idx - k] = heapq.heappop(pq)
    for element in arr1:
        print(element)


if __name__ == '__main__':
    sort_k_sorted([int(input()) for _ in range(int(input()))], int(input()))
