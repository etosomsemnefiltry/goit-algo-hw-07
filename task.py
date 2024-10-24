class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_maximum(root):
    if root is None:
        return None  
    current = root
    # Двигаемся вправо до конца дерева, так как максимальное значение находится в правом поддереве
    while current.right is not None:
        current = current.right
    return current.val

def find_minimum(root):
    if root is None:
        return None  
    current = root
    # Двигаемся влево до конца дерева, так как минимальное значение находится в левом поддереве
    while current.left is not None:
        current = current.left
    return current.val

def total(root):
    if root is None:
        return 0  
    # Рекурсивно суммируем значения узлов
    return root.val + total(root.left) + total(root.right)


root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(15)
root.right.left = Node(25)
root.right.right = Node(35)
root.left.left.left = Node(2)
root.left.left.right = Node(7)
root.left.right.left = Node(12)

max_value = find_maximum(root)
min_value = find_minimum(root)
total_value = total(root)

print(f"Максимальное значение в дереве: {max_value}")
print(f"Минимальное значение в дереве: {min_value}")
print(f"Сумма значений в дереве: {total_value}")