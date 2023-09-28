# Creating Listnode or Node class
class Listnode:
    def __init__(self, data):
        self.data = data
        self.next = None


# Creating Linked list
class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


# Creating Queue using linked list
class Queue:
    def __init__(self):
        self.linkedlist = Linkedlist()

    def __str__(self):
        values = [str(node.data) for node in self.linkedlist]
        return '->'.join(values)

    def isEmpty(self):
        if self.linkedlist.head is None:
            return True
        return False

    def enQueue(self, nodeValue):
        newNode = Listnode(nodeValue)
        if self.isEmpty():
            self.linkedlist.head = newNode
            self.linkedlist.tail = newNode
        else:
            self.linkedlist.tail.next = newNode
            self.linkedlist.tail = newNode

    def deQueue(self):
        if self.isEmpty():
            return 'BST does not exist to deQueue first element!'
        else:
            tempNode = self.linkedlist.head
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next
            return tempNode


# Creating Binary Search Tree (BST)
class BSTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


# Inserting node value into BST
def insertNode(rootnode, nodeValue):
    if not rootnode:
        rootnode.data = nodeValue
    else:
        if nodeValue < rootnode.data:
            if rootnode.leftchild is None:
                rootnode.leftchild = BSTreeNode(nodeValue)
            else:
                insertNode(rootnode.leftchild, nodeValue)
        else:
            if rootnode.rightchild is None:
                rootnode.rightchild = BSTreeNode(nodeValue)
            else:
                insertNode(rootnode.rightchild, nodeValue)


# Searching any node value in BST
def searchNode(rootnode, nodeValue):
    if not rootnode:
        print('No such node in BST!')
    else:
        if rootnode.data == nodeValue:
            print('Found!')
        elif nodeValue < rootnode.data:
            if rootnode.leftchild == nodeValue:
                print('Found!')
            else:
                searchNode(rootnode.leftchild, nodeValue)
        else:
            if rootnode.rightchild == nodeValue:
                print('Found!')
            else:
                searchNode(rootnode.rightchild, nodeValue)


newBST = BSTreeNode(100)

insertNode(newBST, 150)
insertNode(newBST, 90)
insertNode(newBST, 180)
insertNode(newBST, 130)
insertNode(newBST, 10)
insertNode(newBST, 200)
insertNode(newBST, 50)


searchNode(newBST, 50)

# BST traversal using level order traversal
def levelOrderTraversal(rootNode):
    print('Level order traversal')
    if not rootNode.data:  # if rootNode value is 0 / None: return BST does not exist!
        return 'BST does not exist!'
    else:
        customQueue = Queue()
        customQueue.enQueue(rootNode)
        while not customQueue.isEmpty():
            temp_root = customQueue.deQueue()
            print(temp_root.data.data)
            if temp_root.data.leftchild is not None:
                customQueue.enQueue(temp_root.data.leftchild)
            if temp_root.data.rightchild is not None:
                customQueue.enQueue(temp_root.data.rightchild)


newDST = BSTreeNode(None)  # BST does not exist!
print(levelOrderTraversal(newDST))
levelOrderTraversal(newBST)
