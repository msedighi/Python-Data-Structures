class LL_Node_Single: # Singly Linked-List Node 
    next = None
    def __init__(self, val):
        self.value = val

class LL_Node_Double(LL_Node_Single): # Doubly Linked-List Node
    previous = None

class LinkedList_Single:
    count = 0
    def __init__(self, first_val):
        self.first = LL_Node_Single(first_val)
        self.position = self.first
        self.count = 1

    def add(self, val):
        node = self.first
        while node.next:
            node = node.next
        else:
            node.next = LL_Node_Single(val)
            self.position = node
            self.count += 1

    def traverse(self): # I wanna do some action at each node then move so I can 
        node = self.first
        print(node.value)
        while node.next:
            node = node.next
            print(node.value)

class LinkedList_Double(LinkedList_Single):
    def __init__(self, first_val):
        self.first = LL_Node_Double(first_val)
        self.count = 1

    def add(self, val):
        node = self.first
        while node.next:
            node = node.next
        else:
            node.next = LL_Node_Double(val)
            node.next.previous = node
            self.count += 1


class BT_Node: # Binary Tree Node 
    right = None
    left = None
    def __init__(self, val):
        self.value = val

    def LRootR(self):
        if self.left:
            self.left.LRootR()

        print(self.value)

        if self.right:
            self.right.LRootR()

    def LRRoot(self):
        if self.left:
            self.left.LRRoot()

        if self.right:
            self.right.LRRoot()

        print(self.value)

    def RootLR(self):
        print(self.value)

        if self.left:
            self.left.RootLR()

        if self.right:
            self.right.RootLR()

class Binary_Tree:
    def __init__(self, root_val):
        self.root = BT_Node(root_val)

    def LRootR_traverse(self): # I wanna do some action at each node and move to right & left
        self.root.LRootR()
            
    def RootLR_traverse(self):
        self.root.RootLR()

    def LRRoot_traverse(self):
        self.root.LRRoot()


class BST_Node(BT_Node): # Binary Search Tree Node 

    def add(self, val):
        if val <= self.value:
            if self.left:
                self.left.add(val)
            else:
                self.left = BST_Node(val)
        else:
            if self.right:
                self.right.add(val)
            else:
                self.right = BST_Node(val)
        

class BST(Binary_Tree):
    def __init__(self, root_val=None):
        self.root = BST_Node(root_val)

    def add(self, val):
        if self.root.value:
            self.root.add(val)
        else:
            self.root.value = val

