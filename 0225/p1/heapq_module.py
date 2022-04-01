import heapq
arr = [(45, 'Z'), (17, 'X'), (6, 'A'), (93, 'Y')]

heapq.heapify(arr)

print(arr)
'''
       6
   17    45
93
'''
heapq.heappush(arr, (4, 'T'))
print(arr)
'''
       4
   6     45
93   17
'''
print(heapq.heappop(arr))
print(arr)
print(heapq.heappop(arr))
print(arr)

arr.append((0, 'A'))
print(arr)
print(heapq.heappop(arr))
print(arr)
print(heapq.heappop(arr))
print(arr)