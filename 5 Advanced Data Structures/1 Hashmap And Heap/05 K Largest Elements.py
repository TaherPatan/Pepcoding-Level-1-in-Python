from queue import PriorityQueue


def k_largest_elements(arr1, k):
    pq = PriorityQueue()
    for i in range(k):
        pq.put(arr1[i])
    for i in range(k, len(arr1)):
        pq.put(max(pq.get(), arr1[i]))
    printer = ''
    for i in range(k):
        printer = f'{pq.get()} {printer}'
    print(printer)


if __name__ == '__main__':
    n = int(input())
    k_largest_elements(list(map(int, input().split())), int(input()))
