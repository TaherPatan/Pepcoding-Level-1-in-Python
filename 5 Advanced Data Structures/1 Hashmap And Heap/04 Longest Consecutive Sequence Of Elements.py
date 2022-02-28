def longest_sequence_of_elements(arr1):
    sequence_of_elements = {}
    for element in arr1:
        sequence_of_elements[element] = True
    max_start = max_length = 0
    for element in sequence_of_elements:
        if not sequence_of_elements.get(element - 1):
            i = element + 1
            sequence_of_elements[element] = 0
            while i in sequence_of_elements:
                sequence_of_elements[element] += 1
                i += 1
            if max_length < sequence_of_elements[element]:
                max_start, max_length = element, sequence_of_elements[element]
    for i in range(max_start, max_start + max_length + 1):
        print(i)


if __name__ == '__main__':
    longest_sequence_of_elements([int(input()) for _ in range(int(input()))])
