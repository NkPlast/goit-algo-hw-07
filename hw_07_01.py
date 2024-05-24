class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def findMax(node):
    current = node
    
    while(current.right is not None):
        current = current.right
    return current.val

# Створення прикладу дерева
root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.right.right = Node(40)

# Вивід максимального значення
print("Найбільше значення в дереві:", findMax(root))
