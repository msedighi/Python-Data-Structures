from collections import deque

class LL_Node_Single: # Singly Linked-List Node 
    next = None
    def __init__(self, val):
        self.value = val

class LL_Node_Double(LL_Node_Single): # Doubly Linked-List Node
    previous = None

class LinkedList_Single:
    count = 0
    def __init__(self, first_val=None):
        if first_val:
            self.first = LL_Node_Single(first_val)
            self.count = 1
        else:
            self.first = None

    def add(self, val):
        if self.first:
            node = self.first
            while node.next:
                node = node.next
            else:
                node.next = LL_Node_Single(val)
                self.count += 1
        else:
            self.first = LL_Node_Single(val)
            self.count = 1


    def attach(self, LL2):
        self.count += LL2.count
        node = self.first
        while node.next:
            node = node.next
        else:
            node.next = LL2.first

    def traverse(self, func):  
        node = self.first
        func(node.value)
        while node.next:
            node = node.next
            func(node.value)

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

    def LRootR(self, func):
        if self.left:
            self.left.LRootR(func)

        func(self.value)

        if self.right:
            self.right.LRootR(func)

    def LRRoot(self, func):
        if self.left:
            self.left.LRRoot(func)

        if self.right:
            self.right.LRRoot(func)

        func(self.value)

    def RootLR(self, func):
        func(self.value)

        if self.left:
            self.left.RootLR(func)

        if self.right:
            self.right.RootLR(func)

    def MaxHeight(self, height):
        if self.left:
            l_height = self.left.MaxHeight(height + 1)
        else:
            l_height = height

        if self.right:
            r_height = self.right.MaxHeight(height + 1)
        else:
            r_height = height

        if l_height > r_height:
            return l_height
        else:
            return r_height

    def MinHeight(self, height):
        if self.left:
            l_height = self.left.MinHeight(height + 1)
        else:
            l_height = height

        if self.right:
            r_height = self.right.MinHeight(height + 1)
        else:
            r_height = height

        if l_height < r_height:
            return l_height
        else:
            return r_height

class Binary_Tree:
    LevelOrder = []
    def __init__(self, root_val = None):
        if root_val:
            self.root = BT_Node(root_val)

    def LRootR_traverse(self, func): # I wanna do some action at each node and move to right & left
        self.root.LRootR(func)
            
    def RootLR_traverse(self, func):
        self.root.RootLR(func)

    def LRRoot_traverse(self, func):
        self.root.LRRoot(func)

    def Height(self):
        return (self.root.MinHeight(0), self.root.MaxHeight(0))

    def LevelOrder_List(self):
        OutList = LinkedList_Single()
        ThisLevel = LinkedList_Single(self.root)
        node = ThisLevel.first
        while node:
            OutList.attach(ThisLevel)
            ThisLevel = LinkedList_Single()
            while node.value:
                if node.value.left:
                    ThisLevel.add(node.value.left)

                if node.value.right:
                    ThisLevel.add(node.value.right)
                
                if node.next:
                    node = node.next
                else:
                    break

            node = ThisLevel.first

        return OutList

    def LevelOrder_Build(self, InList):
        i=0        
        self.root = BT_Node(InList[i])
        ThisLevel = LinkedList_Single(self.root)
        LL_node = None

        while True:
            if LL_node == None:
                LL_node = ThisLevel.first
                ThisLevel = LinkedList_Single()

            i += 1
            if i < len(InList):
                LL_node.value.left = BT_Node(InList[i])
                ThisLevel.add(LL_node.value.left)
            else:
                break

            i += 1
            if i < len(InList):
                LL_node.value.right = BT_Node(InList[i])
                ThisLevel.add(LL_node.value.right)
            else:
                break

            LL_node = LL_node.next


    def LevelOrder_traverse(self, func):
        ThisLevel = LinkedList_Single(self.root)
        node = ThisLevel.first
        func(node.value.value)
        while node:
            ThisLevel = LinkedList_Single()
            while node.value:
                if node.value.left:
                    ThisLevel.add(node.value.left)
                    func(node.value.left.value)

                if node.value.right:
                    ThisLevel.add(node.value.right)
                    func(node.value.right.value)
                
                if node.next:
                    node = node.next
                else:
                    break

            node = ThisLevel.first


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
        

class BST(Binary_Tree): # Binary Search Tree
    def __init__(self, root_val=None):
        self.root = BST_Node(root_val)

    def add(self, val):
        if self.root.value:
            self.root.add(val)
        else:
            self.root.value = val

class BH(Binary_Tree): # Binary Heap
    def __init__(self):
        self.root = None

    def Build(self, sorted_array):
        self.LevelOrder_Build(sorted_array)


class Vertex:
    def __init__(self, val):
        self.value = val
        self.neighbors = set()
        self.flag = False
    
    def add_Neighbors(self, *neighbors):
        self.neighbors.update(list(neighbors))

class Graph:
    def __init__(self):
        self.Vertices = set()
        
    def add_Vertex(self, *vertices):
        self.Vertices.update(list(vertices))

    def print_vertices(self):
        for v in self.Vertices:
            print(v.value)

    def reset_flags(self):
        for V in self.Vertices:
            V.flag = False

    def BFT(self, func, q):
        for v in q[0].neighbors:
            if not v.flag:
                q.append(v)
                v.flag = True
                
        func(q[0].value)
        q.popleft()

        if len(q) > 0:
            self.BFT(func, q)
    
    def BFTransverse(self, func):
        self.reset_flags()
        q = deque()
        for start_v in self.Vertices:
            if not start_v.flag:
                q.append(start_v)
                start_v.flag = True
                self.BFT(func, q)

    def DFT(self, func, s):
        func(s[0].value)
        s[0].flag = True
        for v in s[0].neighbors:
            if not v.flag:
                s.appendleft(v)
                self.DFT(func, s)
                                
        s.popleft()

    def DFTransverse(self, func):
        self.reset_flags()
        s = deque()
        for start_v in self.Vertices:
            if not start_v.flag:
                s.appendleft(start_v)
                self.DFT(func, s)

            
    
