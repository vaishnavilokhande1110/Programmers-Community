'''
The program is implemented to find minimum element in array
 
Time Complexity: O(n)
Space Complexity: O(1)
'''
l = list(int(i) for i in input().strip().split(' '))
length = len(l)
minimum = l[0]
i = 0
for i in range(length):
    if minimum > l[i]:
        minimum = l[i]
print(minimum)
