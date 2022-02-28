import heapq


class ListAttributes:
    def __init__(self, data, list_index, data_index, list_size):
        self.data = data
        self.list_index = list_index
        self.data_index = data_index
        self.list_size = list_size - 1

    def __lt__(self, other):
        return True if self.data < other.data else False

    def __gt__(self, other):
        return False if self.data < other.data else True

    def __le__(self, other):
        return True if self.data <= other.data else False

    def __ge__(self, other):
        return False if self.data <= other.data else True

    def __eq__(self, other):
        return True if self.data == other.data else False

    def __ne__(self, other):
        return True if self.data != other.data else False


def merge_lists(lst):
    pq = []
    sorted_arr = []
    for i in range(len(lst)):
        heapq.heappush(pq, ListAttributes(lst[i][0], i, 0, len(lst[i])))
    while pq:
        min_element = heapq.heappop(pq)
        sorted_arr.append(min_element.data)
        if min_element.data_index < min_element.list_size:
            min_element.data_index += 1
            min_element.data = lst[min_element.list_index][min_element.data_index]
            heapq.heappush(pq, min_element)
    for element in sorted_arr:
        print(element, end=' ')
    print()


if __name__ == '__main__':
    lst = []
    for _ in range(int(input())):
        _ = int(input())
        lst.append(list(map(int, input().split())))
    merge_lists(lst)
