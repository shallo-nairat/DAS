# DAS
Heaps

Heaps are special tree structures in which the parent node is less than or equal to its child node (min-heap) when the parent node is greater or equal to its child node (max-heap)
 
Advantages

Efficient insertion and deletion
Efficient priority queue
Space efficiency
Guaranteed access to  the maximum or minimum element

Disadvantages
Lack of flexibility 
Memory management
Not ideal for searching

Properties
-The heap property says that the value of the Parent is either greater than or equal to (in a max heap) or less than or equal to (in a min-heap) the value of the child.

Application of binary trees
Sorting algorithms
Database systems
File systems
Decision trees

Accessing items in a heap
Adding items to a Heap
Increase the heap size by 1, so that it can store the new element
Insert the new element at the end of the heap
The newly inserted element may distort the properties of the heap for its parents and heapify.

Removing items in a Heap
Replace the root or element to be deleted with the last element
Delete the last element from the heap
Since the last element is replaced Heapify.

