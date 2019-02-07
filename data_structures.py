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

    def LCA(self, node, v1, v2): # Least_Common_Ancestor
        if node.left:
            t_left = self.LCA(node.left, v1, v2)
        else:
            t_left = (0, None)
        if node.right:
            t_right = self.LCA(node.right, v1, v2)
        else:
            t_right = (0, None)

        if t_left[0]==0 and t_right[0]==0 and node.value!=v1 and node.value!=v2:
            return (0, None)
        else:
            if (t_left[0]==1 and t_right[0]==0 and node.value!=v1 and node.value!=v2) or (t_left[0]==0 and t_right[0]==1 and node.value!=v1 and node.value!=v2) or (t_left[0]==0 and t_right[0]==0 and (node.value==v1 or node.value==v2)):
                return (1, None)
            else:
                if (t_left[0]==1 and t_right[0]==1) or ((t_left[0]==1 or t_right[0]==1) and (node.value==v1 or node.value==v2)):
                    return(2, node.value)
                else:
                    if t_left[0]==2:
                        return t_left
                    elif t_right[0]==2:
                        return t_right
                    else:
                        print("This should NOT happen!!")

    def Least_Common_Ancestor(self, v1, v2):
        result = self.LCA(self.root, v1, v2)
        return result[1]






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


class Adj_Vertex:
    def __init__(self, val):
        self.value = val
        self.next = None

class Undirected_Graph:
    def __init__(self, num_v):
        self.num_vertices = num_v
        self.vertices = [None] * self.num_vertices

    def add_edge(self, v1, v2):
        V1 = Adj_Vertex(v1)
        V2 = Adj_Vertex(v2)
        V1.next = self.vertices[v2]
        V2.next = self.vertices[v1]
        
        self.vertices[v1] = V2
        self.vertices[v2] = V1

    def print_graph(self):
        for i in range(self.num_vertices):
            print("for ", i, " neighbors are: ")
            temp = self.vertices[i]
            while temp:
                print(temp.value)
                temp = temp.next





    
