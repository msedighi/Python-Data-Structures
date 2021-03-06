import data_structures as ds
import random

LL1 = ds.LinkedList_Single("hasan")
LL1.add("tagji")
LL1.add("hashem")
LL2 = ds.LinkedList_Single(45)
LL2.add(32)
print("Linked List 1: ")
LL1.traverse(print)
print("Linked List 2: ")
LL2.traverse(print)
print("Combined Linked List : ")
LL1.attach(LL2)
LL1.traverse(print)



Tree = ds.Binary_Tree(1)
Tree.root.left = ds.BT_Node(2)
Tree.root.right = ds.BT_Node(3)
Tree.root.left.left = ds.BT_Node(4)
Tree.root.left.right = ds.BT_Node(5)

print("\nLRootR : ")
Tree.LRootR_traverse(print)
print("\nRootLR : ")
Tree.RootLR_traverse(print)
print("\nLRRoot : ")
Tree.LRRoot_traverse(print)
print("\nLevelOrder : ")
Tree.LevelOrder_traverse(print)
print("\nHeight : ")
print(Tree.Height())

Tree2 = ds.Binary_Tree()
input_list = [1,2,3,4,5,6,7]
Tree2.LevelOrder_Build(input_list)

print("\nLRootR : ")
Tree2.LRootR_traverse(print)
print("\nRootLR : ")
Tree2.RootLR_traverse(print)
print("\nLRRoot : ")
Tree2.LRRoot_traverse(print)
print("\nLevelOrder : ")
Tree2.LevelOrder_traverse(print)
print("\nHeight : ")
print(Tree2.Height())

BSTree = ds.BST()
for i in range(5):
    r = random.randint(1,20)
    print("random number: ", r)
    BSTree.add(r)

print("\nLRootR : ")
BSTree.LRootR_traverse(print)
print("\nRootLR : ")
BSTree.RootLR_traverse(print)
print("\nLRRoot : ")
BSTree.LRRoot_traverse(print)
print("\nLevelOrder : ")
BSTree.LevelOrder_traverse(print)
print("\nHeight : ")
print(BSTree.Height())


G = ds.Graph()
v1 = ds.Vertex(1)
v2 = ds.Vertex(2)
v3 = ds.Vertex(3)
v4 = ds.Vertex(4)
v5 = ds.Vertex(5)
v6 = ds.Vertex(6)
G.add_Vertex(v1, v2, v3, v4, v5, v6)

v1.add_Neighbors(v2, v3)
v2.add_Neighbors(v1, v4, v5)
v3.add_Neighbors(v1, v5)
v4.add_Neighbors(v2, v5, v6)
v5.add_Neighbors(v2, v3, v4, v6)
v6.add_Neighbors(v4, v5)

G.print_vertices()
print("\n")
G.BFTransverse(print)
print("\n")
G.DFTransverse(print)

UG = ds.Undirected_Graph(5)
UG.add_edge(0, 1)
UG.add_edge(0, 4)
UG.add_edge(1, 2)
UG.add_edge(1, 3)
UG.add_edge(1, 4)
UG.add_edge(2, 3)
UG.add_edge(3, 4)

UG.print_graph()

Tree3 = ds.Binary_Tree(20)
Tree3.root.left = ds.BT_Node(8)
Tree3.root.right = ds.BT_Node(22)
Tree3.root.left.left = ds.BT_Node(4)
Tree3.root.left.right = ds.BT_Node(12)
Tree3.root.left.right.left = ds.BT_Node(10)
Tree3.root.left.right.right = ds.BT_Node(14)

print("Least Common Ancestors: ")
print(Tree2.Least_Common_Ancestor(4,5)) # Should be: 2
print(Tree2.Least_Common_Ancestor(4,6)) # Should be: 1
print(Tree2.Least_Common_Ancestor(3,4)) # Should be: 1
print(Tree2.Least_Common_Ancestor(2,4)) # Should be: 2
print(Tree3.Least_Common_Ancestor(10,14)) # Should be: 12
print(Tree3.Least_Common_Ancestor(14,8)) # Should be: 8
print(Tree3.Least_Common_Ancestor(10,22)) # Should be: 20
print(Tree3.Least_Common_Ancestor(11,12)) # Should be: None
print(Tree3.Least_Common_Ancestor(11,2)) # Should be: None

print(Tree2.Least_Common_Ancestor0(4,5)) # Should be: 2
print(Tree2.Least_Common_Ancestor0(4,6)) # Should be: 1
print(Tree2.Least_Common_Ancestor0(3,4)) # Should be: 1
print(Tree2.Least_Common_Ancestor0(2,4)) # Should be: 2
print(Tree3.Least_Common_Ancestor0(10,14)) # Should be: 12
print(Tree3.Least_Common_Ancestor0(14,8)) # Should be: 8
print(Tree3.Least_Common_Ancestor0(10,22)) # Should be: 20
print(Tree3.Least_Common_Ancestor0(11,12)) # Should be: None -> FAILS!
print(Tree3.Least_Common_Ancestor0(11,2)) # Should be: None
