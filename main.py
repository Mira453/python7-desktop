import numpy as np

# Функція для перевірки орієнтованості графа на основі матриці суміжності
def check_orientation(matrix):
    matrix = np.array(matrix)
    if (matrix == matrix.T).all():
        print("Граф є неорієнтованим.")
    else:
        print("Граф є орієнтованим.")

# Клас для вузла бінарного дерева
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Побудова бінарного дерева для арифметичного виразу
class ExpressionTree:
    def __init__(self, expression):
        self.expression = expression
        self.root = self._build_tree(expression)

    def _build_tree(self, expression):
        operators = {'+', '-', '*', '/'}
        stack = []
        postfix = self._to_postfix(expression)

        for char in postfix:
            if char not in operators:
                stack.append(TreeNode(char))
            else:
                node = TreeNode(char)
                node.right = stack.pop()
                node.left = stack.pop()
                stack.append(node)

        return stack.pop()

    def _to_postfix(self, expression):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        output = []
        stack = []

        for char in expression:
            if char.isnumeric():
                output.append(char)
            elif char in precedence:
                while stack and precedence.get(stack[-1], 0) >= precedence[char]:
                    output.append(stack.pop())
                stack.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()

        while stack:
            output.append(stack.pop())

        return output

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")

    def print_tree(self, node, level=0, prefix="Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.value))
            if node.left is not None or node.right is not None:
                self.print_tree(node.left, level + 1, prefix="L--- ")
                self.print_tree(node.right, level + 1, prefix="R--- ")

# Матриця суміжності (приклад з таблиці 3)
matrix = [
    [1, 0, 1, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1]
]

# Арифметичний вираз (приклад з таблиці 4)
expression = "((2+5)*4-7)/3"

# Перевірка орієнтованості графа
print("\nПеревірка орієнтованості графа:")
check_orientation(matrix)

# Побудова дерева та обходи
print("\nПобудова та обхід дерева для виразу:", expression)
expr_tree = ExpressionTree(expression)

print("\nСтруктура дерева:")
expr_tree.print_tree(expr_tree.root)

print("\nПрямий обхід дерева:")
expr_tree.preorder(expr_tree.root)

print("\n\nОбратний польський запис:")
expr_tree.postorder(expr_tree.root)

print("\n\nІнфіксна нотація (підтвердження):")
expr_tree.inorder(expr_tree.root)