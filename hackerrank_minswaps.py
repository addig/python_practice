def swap(arr, loc1, loc2):
    temp = arr[loc2]
    arr[loc2]=arr[loc1]
    arr[loc1]=temp
    return arr

def minimumSwaps(arr):
    tot_len = len(arr)
    count = 0
    for i in range(tot_len):
        if arr[i]== min(arr):
            continue
        else:
            temp_min = min(arr[i::])
            ind = arr.index(temp_min)
            if arr[i]>temp_min:
                arr = swap(arr,ind,i)
                count += 1

    return count





def main():
    arr = [1,3,5,2,4,6,8]
    res = minimumSwaps(arr)
    print res


if __name__ == '__main__':
    main()