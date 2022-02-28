def get_common_elements(arr1, arr2):
    arr1_elements = {}
    for element in arr1:
        arr1_elements[element] = arr1_elements.get(element, 0) + 1
    for element in arr2:
        if arr1_elements.get(element):
            print(element)
            arr1_elements[element] -= 1
        if not arr1_elements.get(element):
            arr1_elements.pop(element, 0)


if __name__ == '__main__':
    get_common_elements([int(input()) for _ in range(int(input()))], [int(input()) for _ in range(int(input()))])
