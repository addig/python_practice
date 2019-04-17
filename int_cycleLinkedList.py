class ListNode(object):
    def __init__(self,node):
        self.value = node
        self.nextNode = None


def checkCycle(node):
    inst = node
    nextList = []
    while inst != None:
        if inst.nextNode !=None:
            if inst.nextNode not in nextList:
                nextList += [inst.nextNode]
            else:
                return True
        else:
            return False
        inst = inst.nextNode
    return False

def n_to_last(a,num):
    counter = 0
    inst = a
    # get length of Linked L list
    # get to the desired node
    while inst != None:
        inst = inst.nextNode
        counter +=1

    inst = a
    for i in range(0,counter-num):
        inst = inst.nextNode

    return inst



a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.nextNode = b
b.nextNode = c
c.nextNode = d
d.nextNode = e

nn= n_to_last(a,2)
print nn.value
#print checkCycle(a)