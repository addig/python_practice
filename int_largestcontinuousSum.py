"""

def large_cont_sum(arr):


    :param arr:
    :return:

    L = len(arr)
    tarSum = arr[0]
    arrSum = arr[0]
    start = 0
    end =0
    for i in range(1,L):
        for j in range(i,L):
            arrSum = arrSum  + arr[j]

            if arrSum > tarSum:
                tarSum = arrSum
                start, end = arr[i], arr[j]
        arrSum = 0
    print tarSum ,(start,end)
    return tarSum
"""

def large_cont_sum(arr):
    # Check to see if array is length 0
    if len(arr) == 0:
        return 0

    # Start the max and current sum at the first element
    max_sum = current_sum = arr[0]

    # For every element in array
    for num in arr[1:]:
        # Set current sum as the higher of the two
        current_sum = max(current_sum + num, num)

        # Set max as the higher between the currentSum and the current max
        max_sum = max(current_sum, max_sum)

    return max_sum
sumnm = large_cont_sum([-1,-2,-1,3,4,-1,15])