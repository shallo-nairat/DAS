import heapq

data =[20,24,30,15,21,7]
heapq.heapify(data)

print(data)

heapq.heappush(data,19)
print(data)

heapq.heappop(data)
print(data)