

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid

    return -1


k = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 2)
if k == -1:
    print("not found")
else:
    print("element found at postion:", k+1)
