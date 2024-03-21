from collections import deque
class Bird:
    def __init__(self,type,rate,wing):
        self.type=type
        self.rate=rate
        self.wing=wing
class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def f0():
        return "HE182474"
    def f1(self,type,rate,wing):
        if type[0]=='B' or rate>10:
            pass
        if self.root is None:
            self.root=Node(Bird(type,rate,wing))
        cur=self.root
        while cur:
            if cur.key.rate==rate:
                return
            else:
                father=cur
                if cur.key.rate<rate:
                    cur=cur.right
                else:
                    cur=cur.left
        if father.key.rate<rate:
            father.right=Node(Bird(type,rate,wing))
        else:
            father.left=Node(Bird(type,rate,wing))
    def f2(self,tree):
        if tree==None:
            return
        if 4<=tree.key.wing<=10:
            print(f"({tree.key.type,tree.key.rate,tree.key.wing})")

        self.f2(tree.left)
        self.f2(tree.right)
    def f3(self, tree):
        if tree is None:
            return
        queue = deque()
        queue.append(tree)
        odd_position = True
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if odd_position:
                    print(f"({node.key.type},{node.key.rate},{node.key.wing})")
                odd_position = not odd_position
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
    def f4(self,tree):
        if tree is None:
            return
        self.f4(tree.left)
        self.f4(tree.right)
        if tree.key.wing<=4 and tree.key.rate>6:
            print(f"({tree.key.type},{tree.key.rate},{tree.key.wing})")
    def f5(self,tree):
        if tree is None:
            return
        self.f5(tree.left)
        if tree.key.type[0] in ('A','C'):
            print(f"({tree.key.type},{tree.key.rate},{tree.key.wing})")
        self.f5(tree.right)
    def f6(self, tree):
        def find_in_order_successor(node):
            while node.left:
                node = node.left
            return node

        def delete_node(root, key):
            if not root:
                return root

            if key < root.key.rate:
                root.left = delete_node(root.left, key)
            elif key > root.key.rate:
                root.right = delete_node(root.right, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left

                in_order_successor = find_in_order_successor(root.right)
                root.key = in_order_successor.key
                root.right = delete_node(root.right, in_order_successor.key.rate)

            return root

        count = [0]
        target = [None, None]

        def find_third_node(root, parent=None):
            if not root:
                return

            find_third_node(root.left, root)
            count[0] += 1
            if count[0] == 3:
                target[0] = parent
                target[1] = root
                return
            find_third_node(root.right, root)

        find_third_node(self.root)

        if target[0] and target[1]:
            if target[0].left and target[0].left.key.rate == target[1].key.rate:
                target[0].left = delete_node(target[0].left, target[1].key.rate)
            else:
                target[0].right = delete_node(target[0].right, target[1].key.rate)

        self.inorder(tree)

    def inorder(self, tree):
        if tree is None:
            return
        self.inorder(tree.left)
        print(f"({tree.key.type},{tree.key.rate},{tree.key.wing})")
        self.inorder(tree.right)
    def f7(self, tree):
        def find_post_order_successor(node):
            if node.right:
                return find_post_order_successor(node.right)
            elif node.left:
                return find_post_order_successor(node.left)
            else:
                return node

        def delete_node(root, key):
            if not root:
                return root

            if key < root.key.rate:
                root.left = delete_node(root.left, key)
            elif key > root.key.rate:
                root.right = delete_node(root.right, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left

                post_order_successor = find_post_order_successor(root.left if root.left else root.right)
                root.key = post_order_successor.key
                if root.left and root.left.key.rate == post_order_successor.key.rate:
                    root.left = delete_node(root.left, post_order_successor.key.rate)
                else:
                    root.right = delete_node(root.right, post_order_successor.key.rate)

            return root

        count = [0]
        target = [None]

        def find_sixth_node(root):
            if not root:
                return

            find_sixth_node(root.left)
            find_sixth_node(root.right)
            count[0] += 1
            if count[0] == 6:
                target[0] = root
                return

        find_sixth_node(self.root)

        if target[0]:
            self.root = delete_node(self.root, target[0].key.rate)

        self.postorder(tree)

    def postorder(self, tree):
        if tree is None:
            return
        self.postorder(tree.left)
        self.postorder(tree.right)
        print(f"({tree.key.type},{tree.key.rate},{tree.key.wing})")
    def f8(self, tree):
        count = [0]
        target = [None]

        def find_fourth_node(root):
            if not root:
                return

            count[0] += 1
            if count[0] == 4:
                target[0] = root
                return

            find_fourth_node(root.left)
            find_fourth_node(root.right)

        find_fourth_node(self.root)

        if target[0]:
            target[0].key.wing = self.height(target[0])

        self.preorder(tree)

    def height(self, node):
        if node is None:
            return -1
        else:
            return 1 + max(self.height(node.left), self.height(node.right))

    def preorder(self, tree):
        if tree is None:
            return
        print(f"({tree.key.type},{tree.key.rate},{tree.key.wing})")
        self.preorder(tree.left)
        self.preorder(tree.right)
    def f9(self, tree):
        count = [0]
        target = [None]

        def find_sixth_node(root):
            if not root:
                return

            find_sixth_node(root.left)
            count[0] += 1
            if count[0] == 6:
                target[0] = root
                return
            find_sixth_node(root.right)

        find_sixth_node(self.root)

        if target[0]:
            target[0].key.wing = self.height(target[0])

        self.inorder(tree)

    def height(self, node):
        if node is None:
            return -1
        else:
            return 1 + max(self.height(node.left), self.height(node.right))
    def f10(self, tree):
        target = [None]

        def find_target_node(root):
            if not root:
                return

            find_target_node(root.left)
            find_target_node(root.right)

            if root.left and root.right and root.key.rate < 5:
                target[0] = root
                return

        find_target_node(self.root)

        if target[0]:
            self.right_rotate(target[0])

        self.postorder(tree)

    def right_rotate(self, node):
        y = node.left
        node.left = y.right
        if y.right is not None:
            y.right.parent = node
        y.parent = node.parent
        if node.parent is None:
            self.root = y
        elif node == node.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y
        y.right = node
        node.parent = y
    def f11(self, tree):
        target = [None]

        def find_target_node(root):
            if not root:
                return

            find_target_node(root.left)
            if root.right and root.key.rate > 7:
                target[0] = root
                return
            find_target_node(root.right)

        find_target_node(self.root)

        if target[0]:
            self.left_rotate(target[0])

        self.inorder(tree)

    def left_rotate(self, node):
        y = node.right
        node.right = y.left
        if y.left is not None:
            y.left.parent = node
        y.parent = node.parent
        if node.parent is None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node
        node.parent = y


