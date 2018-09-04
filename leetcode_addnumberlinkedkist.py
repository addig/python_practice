# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

        #return self.val

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        """
        return l1


def stringToIntegerList(input):
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input

    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"



def main():
    import sys

    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()

    while True:
        try:
            line = lines.next()
            l1 = stringToIntegerList(line)
            line = lines.next()
            l2 = stringToIntegerList(line)

            ret = Solution().addTwoNumbers(l1, l2)
            print ret
        except StopIteration:
            break
    print 1

if __name__ == '__main__':
    main()
