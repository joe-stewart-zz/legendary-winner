def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])

def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n%base]

def binarySearch(lst, item):
    if len(lst) == 0:
        return False
    else:
        mid = len(lst) // 2
        if lst[mid] == item:
            return True
        else:
            if item < lst[mid]:
                return binarySearch(lst[:mid], item)
            else:
                return binarySearch(lst[mid+1:], item)

if __name__ == '__main__':
    #print(listsum([1,3,5,7,9]))
    #print(toStr(1453, 16))
    #print(toStr(10, 2))

    testlist = [0,1,2,8,13,17,19,32,42]
    print(binarySearch(testlist, 3))
    print(binarySearch(testlist, 13))
