class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def sumOfValues(node):
    if node is None:
        return 0
    else:
        # Рекурсивно обраховуємо суму всіх значень
        return node.val + sumOfValues(node.left) + sumOfValues(node.right)

# Створення прикладу дерева
root = Node(20)
root.left = Node(10)
root.left.left = Node(5)
root.left.right = Node(15)
root.right = Node(30)
root.right.right = Node(40)

# Вивід суми всіх значень у дереві
print("Сума всіх значень у дереві:", sumOfValues(root))
