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


    # input from keyboard
    n = int(input().strip())
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

# Alens Ilgavižs 221RDB312 4.g