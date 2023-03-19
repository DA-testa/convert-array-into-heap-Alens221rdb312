# python3


def build_heap(data):
    swaps = []
    n = len(data)

    for i in range(n//2 - 1, -1, -1):
        swaps += sift_down(i, data)

    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    return swaps

def sift_down(i, data):
    swaps = []
    n = len(data)

    min_child = i
    left_child = 2*i + 1
    right_child = 2*i + 2

    if left_child < n and data[left_child] < data[min_child]:
        min_child = left_child

    if right_child < n and data[right_child] < data[min_child]:
        min_child = right_child

    if i != min_child:
        swaps.append((i, min_child))
        data[i], data[min_child] = data[min_child], data[i]

        swaps += sift_down(min_child, data)

    return swaps


def main():


    text = input("Enter 'I' for input or 'F' for file")
    if "F" in text:
        file_name = input("Enter file name: ")
        if "a" not in file_name:
            path = './tests/' + file_name
            with open(path, 'r', encoding='utf-8') as file:
                n = int(file.readline())
                data = list(map(int, file.readline().split()))
    elif "I" in text:
        n = int(input())
        data = list(map(int, input().split()))

    assert data is not None and len(data) == n

    swaps = build_heap(data)

    assert len(swaps) <= n*4

    print(len(swaps))
    for i, j in swaps:
        print(i, j)
 
if __name__ == "__main__":
    main()

# Alens Ilgavižs 221RDB312 4.g