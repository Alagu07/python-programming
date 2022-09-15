arr = [100, 69, 1, 36, 7, 20, 8]
mini = arr[0]
maxi = arr[0]

for i in range(len(arr)):
  if arr[i] < mini: mini = arr[i] 
  
if arr[i] > maxi: maxi = arr[i]

print (mini)
print (maxi)
