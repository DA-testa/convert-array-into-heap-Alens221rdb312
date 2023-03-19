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



    try:
        # read input
        n = int(input().strip())
        assert n > 0

        data = list(map(int, input().split()))
        assert len(data) == n

        order = input().strip().upper()
        assert order in ["I", "F"]

        # build heap
        swaps = build_heap(data)

        # reverse array if order is "F"
        if order == "F":
            data = data[::-1]
            swaps = [(n-1-i, n-1-j) for i,j in swaps[::-1]]

        # check if resulting array is a valid heap
        is_heap = all(data[i] <= data[(i-1)//2] for i in range(1, n))

        # output swaps if heap is not valid
        if not is_heap:
            assert len(swaps) <= 4*n
            print(len(swaps))
            for i, j in swaps:
                print(i, j)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()

# Alens Ilgavižs 221RDB312 4.g