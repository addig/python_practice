from __future__ import print_function
import itertools
alist = []
for _ in range(int(raw_input())):
     name = raw_input()
     score = float(raw_input())
     row =[score, name]
     alist[len(alist):] = [row]
alist.sort(reverse=True)
flag = 0
a = alist.pop()
namelist = []
flag1= 1
end =0
while ((flag <=1) & (end != 1)):
    if (len(alist)>1):
        b = alist.pop()
    else:
        b = list(itertools.chain(*alist))
        end = 1
    if ((b[0] > a[0])):
        flag = flag + 1
        if (flag <=1):
            namelist.append(b[1])
        flag1 = 0
        a = b
    elif ((a[0] == b [0])& (flag1 == 0)):
        namelist.append(b[1])
        a = b
namelist.sort()
print(*namelist, sep ='\n')

