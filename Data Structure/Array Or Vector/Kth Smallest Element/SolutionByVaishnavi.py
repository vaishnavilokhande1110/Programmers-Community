def kthSmallest(arr, n, k): 
  
    
    arr.sort() 
  
    return arr[k-1] 
  

 
arrSize=int(input("Enter your array size:"))
arr=[]
print("Enter your array elements: ")
for i in range(arrSize):
    arr.append(int(input()))
k = int(input("Enter K:"))

n = len(arr) 
print("K'th smallest element is", 
          kthSmallest(arr, n, k)) 
