def binarySearch(lst, item):
    first = 0
    last = len(lst) - 1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if lst[mid] == item:
            found = True
        else:
            if item < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

if __name__ == '__main__':
    testlist = [0,1,2,8,13,19,32,42]
    print(binarySearch(testlist, 3))
    print(binarySearch(testlist, 13))
