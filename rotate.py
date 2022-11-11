def rotate_array(arr,d,p):
    if d == 0 :
        arr = arr[p:]+arr[:p]
    else:
        arr = arr[-p:]+arr[:p-1]
    return arr

arr = list(map(int,input().split()))
d = int(input())
p = int(input())
print(rotate_array(arr,d,p))
print(rotate_array(arr,1,p))