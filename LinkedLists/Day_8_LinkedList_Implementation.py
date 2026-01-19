# Problems: Implement a singly linked list with insert and delete operations.
# Learning Objectives: Node creation, pointers, linked list traversal.

class Node:
    def __init__(self, data):
        self.data = data  # Node.data is the data stored at the particular node
        self.next = None  # Node.next is the pointer to the next node, initialized to none

class LinkedLists:
    def __init__(self):
        self.head = None # Initialize an empty list

    def append(self, data):
        new_node = Node(data)   # A new class item is made new_node with a data value and a next pointer value
        if not self.head:       # If self.head is none then store new value into head
            self.head = new_node
            return
    
        last_node = self.head   # last node is given the value of the current head which is None
        while last_node.next:   # Iterate over the nodes until it is at the end
            last_node = last_node.next
        
        last_node.next = new_node   # Store the new value into the last_node
    
    def deletion(self, data):
        # 1. Empty List Case
        if not self.head:
            print("Empty list.")
            return

        # 2. Deleting the Head Case
        if self.head.data == data:
            self.head = self.head.next  # Move head to the next node
            return

        # 3. Deleting from Middle or End
        current = self.head
        # Look ahead to see if the NEXT node is the one we want to delete
        while current.next:
            if current.next.data == data:
                current.next = current.next.next  # Link current node to the one after the target
                return
            current = current.next

        print(f"Data {data} not found in the list.")        

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

my_list = LinkedLists()

my_list.append(10)
my_list.append(20)
my_list.append(30)

my_list.display()

# --- COMPLEXITY ANALYSIS ---
# TIME COMPLEXITY:
# .append()  : O(n) - Must traverse the whole list to find the end.
# .deletion(): O(n) - In the worst case, the item is at the end or not there.
# .display() : O(n) - Must visit every single node once.
# Note: If we kept a 'tail' pointer, append would become O(1).

# SPACE COMPLEXITY:
# Overall    : O(n) - We store 'n' nodes in memory.
# Per operation: O(1) - Adding or deleting only uses a few temporary variables.