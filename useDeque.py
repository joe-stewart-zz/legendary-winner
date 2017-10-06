from deque import Deque

def palindrome(string):
    d = Deque()

    for ch in string:
        d.addRear(ch)

    stillEqual = True

    while d.size() > 1 and stillEqual:
        first = d.removeFront()
        last = d.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

print(palindrome("lsdkjfskf"))
print(palindrome("radar"))
print(palindrome("x"))
