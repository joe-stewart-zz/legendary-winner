def sequentialSearch(lst, item):
    idx = 0
    found = False

    while idx < len(lst) and not found:
        if lst[idx] == item:
            found = True
        else:
            idx += 1
    return found

if __name__ == '__main__':
    testlist = [1,2,32,8,17,19,42,13,0]
    print(sequentialSearch(testlist, 3))
    print(sequentialSearch(testlist, 13))
