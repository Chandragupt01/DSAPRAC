
def largest( arr, n):
    largest=arr[0]
    for i in range(len(arr)):
        if arr[i]>largest:
            largest=arr[i]
    return largest