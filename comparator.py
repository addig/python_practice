# Enter your code here. Read input from STDIN. Print output to STDOUT
class Player(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        return "%s, %d" % (self.name, self.score)
    def comparator(a, b):
        print a
        print b
        print "next"
        if a.score > b.score:
            print 1
            return 1

        elif a.score == b.score:
            print 0
            return 0
        else:
            print -1
            return -1

#return "Point3D(%d, %d, %d)" % (self.x, self.y, self.z)
# Main

n = int(raw_input())
data = []
for i in range(n):
    name, score = raw_input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data1 = sorted(data, cmp=Player.comparator, reverse = True)
for i in data:
    print i
#    print i.name, i.score

print 1
