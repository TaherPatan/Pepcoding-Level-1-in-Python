from collections import deque


def slidingWindow(arr, k):
    queue = deque([0])
    for i in range(1, k):
        while queue and arr[queue[-1]] < arr[i]:
            queue.pop()
        queue.append(i)
    print(arr[queue[0]])
    for i in range(k, len(arr)):
        while queue and arr[queue[-1]] <= arr[i]:
            queue.pop()
        queue.append(i)
        if queue[0] <= i - k:
            queue.popleft()
        print(arr[queue[0]])


if __name__ == "__main__":
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    k = int(input())
    slidingWindow(arr, k)
