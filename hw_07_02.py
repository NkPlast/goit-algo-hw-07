class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def findMin(node):
    current = node
  
    while(current.left is not None):
        current = current.left
    return current.val

# Створення прикладу дерева
root = Node(20)
root.left = Node(10)
root.left.left = Node(5)
root.right = Node(30)

# Вивід мінімального значення
print("Найменше значення в дереві:", findMin(root))
