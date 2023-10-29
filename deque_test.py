# importing "collections" for deque operations
import collections

# initializing deque
de = collections.deque()

de.append(1)
de.append(2)
de.append(3)
print("deque: ", de)

# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4)

# printing modified deque
print("\nThe deque after appending at right is : ")
print(de)

popped_value = de.pop()
print("This should be the most recent added value to the Queue")
print(f"{popped_value}")

popped_value = de.popleft()
print("This should be the 1st added value to the Queue (or the left most)")
print(f"{popped_value}")


# using appendleft() to insert element at left end
# inserts 6 at the beginning of deque
#de.appendleft(6)

# printing modified deque
#print("\nThe deque after appending at left is : ")
#print(de)
