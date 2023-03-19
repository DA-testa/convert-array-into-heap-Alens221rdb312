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
        # input from keyboard
        n_input = input().strip()
        assert n_input.isnumeric()
        n = int(n_input)

        data_input = input().strip()
        data = list(map(int, data_input.split()))
        assert len(data) == n

        order_input = input().strip()
        assert order_input in ["I", "F"]
        order = order_input

        if order == "F":
            data = data[::-1]

        swaps = build_heap(data)

        if order == "F":
            swaps = [(n-1-i, n-1-j) for i,j in swaps[::-1]]



        assert len(swaps) <= 4*n
        print(len(swaps))


        for i, j in swaps:
            print(i, j)

    except (ValueError, AssertionError):
        print("Invalid input! Please enter valid input that meets the requirements.")

if __name__ == "__main__":
    main()

# Alens Ilgavižs 221RDB312 4.g