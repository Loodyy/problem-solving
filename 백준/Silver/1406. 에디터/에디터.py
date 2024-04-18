import sys
input = sys.stdin.readline

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.left = self.tail
            self.tail.right = node
            self.tail = node

    def insert(self, target_node: Node, insert_node: Node):
        if target_node == self.tail:
            self.tail.right = insert_node
            insert_node.left = self.tail
            self.tail = insert_node
            return self.tail
        right_node = target_node.right
        right_node.left = insert_node
        target_node.right = insert_node
        insert_node.right = right_node
        insert_node.left = target_node
        return insert_node

    def delete(self, target_node):
        if target_node == self.head:
            return self.head # dummy
        if target_node == self.tail:
            left_node = self.tail.left
            left_node.right = None
            self.tail = left_node
            return self.tail
        left_node = target_node.left
        right_node = target_node.right
        right_node.left = left_node
        left_node.right = right_node
        return left_node
    
    def get_values(self):
        curr_node = self.head.right
        values = []
        while curr_node != None:
            values.append(curr_node.value)
            curr_node = curr_node.right
        return "".join(values)
    
linked_list = LinkedList()
linked_list.append(Node("dummy"))
for s in list(input().rstrip()):
    node = Node(s)
    linked_list.append(node)

N = int(input())
curr_node = linked_list.tail
for _ in range(N):
    temp = input().split()
    cmd = temp[0]
    if cmd == "L":
        curr_node = curr_node.left if curr_node.left else curr_node
    elif cmd == "D":
        curr_node = curr_node.right if curr_node.right else curr_node
    elif cmd == "B":
        curr_node = linked_list.delete(curr_node)
    else:
        val = temp[1]
        node = Node(val)
        curr_node = linked_list.insert(curr_node, node)

print(linked_list.get_values())