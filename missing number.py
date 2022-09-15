def MissingNumber(arr):
 
    n = len(arr)
 
    m = n + 1

    total = m * (m + 1) // 2

    return total - sum(arr)
 
if __name__ == '__main__':
 
    arr = [1, 2, 3, 4, 5, 7, 8, 9, 10]
 
    print('The missing number is',MissingNumber(arr))
