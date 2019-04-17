class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.count = 0
        self.dataDict = {}
        self.kl = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dataDict.keys():
            self.kl.remove(key)
            self.kl = self.kl+[key]
            return self.dataDict[key]

        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        #if key not in self.dataDict.keys():
        if self.count >= self.capacity:
            self.dataDict.pop(self.kl[0])
            self.kl.remove(self.kl[0])
            self.count-=1
        else:
            pass

        self.dataDict[key] = value
        if key not in self.kl:
            self.kl = self.kl+[key]
            self.count +=1
        else:
            self.kl.remove(key)
            self.kl = self.kl + [key]
            #self.count += 1





"""
["LRUCache","put","put","get","put","get","put","get","get","get"]
[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
["LRUCache","put","get"]
[[1],[2,1],[2]]

["LRUCache","put","put","get","put","put","get"]
[[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]
"""
L=LRUCache(2)
L.put(2,1)
L.put(2,2)
print L.get(2)
L.put(1,1)
#print L.get(2)
L.put(4,1)
L.get(2)
"""
print L.get(1)
print L.get(3)
print L.get(4)
"""
print 1

