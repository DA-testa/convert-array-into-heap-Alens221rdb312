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
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    try:
        # input from keyboard

        n = int(input().strip())
        assert n > 0
        data = list(map(int, input().split()))
        order = input().strip()

        # checks if length of data is the same as the said length
        assert len(data) == n

        assert order in ["I", "F"]

        if order == "F":
            data = data[::-1]

        swaps = build_heap(data)

        if order == "F":
            swaps = [(n-1-i, n-1-j) for i,j in swaps[::-1]]

        # TODO: output how many swaps were made, 
        # this number should be less than 4n (less than 4*len(data))

        assert len(swaps) <= 4*n
        print(len(swaps))

        # output all swaps
        for i, j in swaps:
            print(i, j)

    except ValueError:
        print("Invalid input! Please enter a valid integer.")

    except AssertionError:
        print("Invalid input! Please enter a valid value that meets the requirements.")


if __name__ == "__main__":
    main()

# Alens Ilgavižs 221RDB312 4.g