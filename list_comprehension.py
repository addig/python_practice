# if __name__ == '__main__':
#     n = int(raw_input())
#     arr = map(int, raw_input().split())
#     arr.sort()
#     flag = 1
#     a = arr.pop()
#     while (flag == 1):
#         b = arr.pop()
#         if (b< a):
#             flag = 0
#             print (b)
#         else:
#             a= b
#
#     #print (max(arr))


alist = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    row =[score, name]
    #plist = plist.append(5)
    alist[len(alist):] = [row]
alist.sort(reverse=True)
print (alist)
flag = 1
init = 1
a = alist.pop()
print(a)
while (flag == 1):
    b = alist.pop()
    if (init ==1) :
    #print (b)
        if (b[0]>a[0]):
            init = 0
            print (b[1])
    elif(init == 0):
        if (b[0]==a[0]):
            print (b[1])
        elif (b[0]>a[0]):
                print (b[1])
    a = b