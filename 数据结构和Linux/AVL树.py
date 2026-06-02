class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # 初始节点高度定义为 1


class AVLTree:
    def __init__(self):
        self.root = None

    # 获取节点高度
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    # 计算平衡因子
    def get_balance_factor(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # 左旋转
    def rotate_left(self, z):
        y = z.right
        T2 = y.left
        
        # 旋转
        y.left = z
        z.right = T2
        
        # 更新高度
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    # 右旋转
    def rotate_right(self, z):
        y = z.left
        T3 = y.right
        
        # 旋转
        y.right = z
        z.left = T3
        
        # 更新高度
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    # 插入节点并检测失衡
    def insert(self, node, key):
        # 第一步：普通的 BST 插入
        if not node:
            return Node(key)
        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        else:
            return node

        # 第二步：更新当前节点的高度
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # 第三步：计算平衡因子，检测失衡
        balance_factor = self.get_balance_factor(node)

        # LL 型
        if balance_factor > 1 and key < node.left.key:
            print(f"发生 LL 失衡，在节点 {node.key} 调整")
            return self.rotate_right(node)
        # RR 型
        if balance_factor < -1 and key > node.right.key:
            print(f"发生 RR 失衡，在节点 {node.key} 调整")
            return self.rotate_left(node)
        # LR 型
        if balance_factor > 1 and key > node.left.key:
            print(f"发生 LR 失衡，在节点 {node.key} 调整")
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        # RL 型
        if balance_factor < -1 and key < node.right.key:
            print(f"发生 RL 失衡，在节点 {node.key} 调整")
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    # 中序遍历
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.key, end=" ")
            self.inorder_traversal(node.right)

    # 打印树（递归实现）
    def print_tree(self, node, level=0, prefix="Root: "):
        if node:
            print(" " * (level * 4) + prefix + str(node.key) + f" (平衡因子: {self.get_balance_factor(node)})")
            if node.left or node.right:
                self.print_tree(node.left, level + 1, "L--- ")
                self.print_tree(node.right, level + 1, "R--- ")

    # 构造 AVL 树
    def build_avl_tree(self, values):
        for value in values:
            print(f"\n插入 {value}:")
            self.root = self.insert(self.root, value)
            self.print_tree(self.root)

# 测试代码
if __name__ == "__main__":
    values = [30, 20, 10, 25, 40, 35, 50]
    avl_tree = AVLTree()
    
    print("构造 AVL 树:\n")
    avl_tree.build_avl_tree(values)

    print("\n最终中序遍历：")
    avl_tree.inorder_traversal(avl_tree.root)