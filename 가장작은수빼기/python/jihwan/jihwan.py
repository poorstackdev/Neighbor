def solution(arr):
    min = arr[0]
    if(len(arr) == 1):
            return [-1]
    for i in range(len(arr)):
        if(arr[i] < min):
            min = arr[i].value
    arr.remove(min)
    print(arr)

arr = [1,2,3,4,5]
solution(arr)