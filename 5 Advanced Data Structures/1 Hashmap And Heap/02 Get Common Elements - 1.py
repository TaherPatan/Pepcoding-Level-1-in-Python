def get_common_elements(arr1, arr2):
    arr1_elements = set()
    for element in arr1:
        arr1_elements.add(element)
    for element in arr2:
        if element in arr1_elements:
            print(element)
            arr1_elements.remove(element)


if __name__ == '__main__':
    get_common_elements([int(input()) for _ in range(int(input()))], [int(input()) for _ in range(int(input()))])
