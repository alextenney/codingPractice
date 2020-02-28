class Node:
    def __init__(self, value): 
        self.left = None
        self.right = None
        self.value = value
        self.parent = None

class BST:

    def __init__(self, root): 
        self.root = root

    def search(self, node, key): 
        if (node.value == key):
            return key
        elif (node.value > key):
            return self.search(node.left, key)
        elif (node.value < key):
            return self.search(node.right, key)
        else:
            raise Exception

    def insert(self, node, key):
        try:
            search(self.root, key)
        except Exception as e:
            if (self.root is None):
                self.root = Node(key)
            elif (node.value > key):
                if (node.left is None):
                    node.left = Node(key)
                else:     
                    self.insert(node.left, key)
            else:
                if (node.right is None):
                    node.right = Node(key)
                else:    
                    self.insert(node.right, key)

    def delete(self, key):
        try: 
            toDelete = self.search(root, key)

            if (toDelete.left is None and toDelete.right is None):
                if (toDelete.parent.left == toDelete):
                    toDelete.parent.left = None
                    toDelete.parent = None
                    toDelete.value = None
                    toDelete = None
                else:
                    toDelete.parent.right = None
                    toDelete.parent = None
                    toDelete.value = None
                    toDelete = None
            elif(toDelete.left is not None and toDelete.right is None):
                if (toDelete.parent.right == toDelete):
                    toDelete.parent.right = toDelete.left 
                    toDelete.left.parent = toDelete.parent 
                    toDelete.parent = None
                    toDelete.left = None
                    toDelete.value = None
                else: 
                    toDelete.parent.left = toDelete.left 
                    toDelete.left.parent = toDelete.parent 
                    toDelete.parent = None
                    toDelete.left = None
                    toDelete.value = None 
            elif(toDelete.left is None and toDelete.right is not None): 
                if (toDelete.parent.right == toDelete):
                    if (toDelete.right.left is not None):
                        toDelete.parent.right = toDelete.right.left 
                        toDelete.right.left.parent = toDelete.parent
                        toDelete.parent = None
                        toDelete.right.parent = toDelete.right.left
                        toDelete.right.left.right = toDelete.right
                        toDelete.right = None
                        toDelete.value = None
                    else:
                        toDelete.parent.right = toDelete.right
                        toDelete.right.parent = toDelete.parent
                        toDelete.parent = None
                        toDelete.right = None
                        toDelete.value = None
                else:
                    if (toDelete.right.left is not None):
                        toDelete.parent.left = toDelete.right.left 
                        toDelete.right.left.parent = toDelete.parent
                        toDelete.parent = None
                        toDelete.right.parent = toDelete.right.left
                        toDelete.right.left.right = toDelete.right
                        toDelete.right = None
                        toDelete.value = None
                    else:
                        toDelete.parent.left = toDelete.right
                        toDelete.right.parent = toDelete.parent
                        toDelete.parent = None
                        toDelete.right = None
                        toDelete.value = None
            else:
                if (toDelete.parent.right == toDelete):
                    if (toDelete.right.left is not None):
                        toDelete.parent.right = toDelete.right.left 
                        toDelete.right.left.parent = toDelete.parent
                        toDelete.parent = None
                        toDelete.right.parent = toDelete.right.left
                        toDelete.right.left.right = toDelete.right
                        toDelete.left.parent = toDelete.right.left
                        toDelete.right.left.left = toDelete.left
                        toDelete.left = None
                        toDelete.right = None
                        toDelete.value = None
                    else:
                        toDelete.parent.right = toDelete.right
                        toDelete.right.parent = toDelete.parent
                        toDelete.right.left = toDelete.left
                        toDelete.left.parent = toDelete.right
                        toDelete.parent = None
                        toDelete.right = None
                        toDelete.left = None
                        toDelete.value = None
                else:
                    if (toDelete.right.left is not None):
                        toDelete.parent.left = toDelete.right.left 
                        toDelete.right.left.parent = toDelete.parent
                        toDelete.parent = None
                        toDelete.right.parent = toDelete.right.left
                        toDelete.right.left.right = toDelete.right
                        toDelete.left.parent = toDelete.right.left
                        toDelete.right.left.left = toDelete.left
                        toDelete.left = None
                        toDelete.right = None
                        toDelete.value = None
                    else:
                        toDelete.parent.left = toDelete.right
                        toDelete.right.parent = toDelete.parent
                        toDelete.right.left = toDelete.left
                        toDelete.left.parent = toDelete.right
                        toDelete.parent = None
                        toDelete.right = None
                        toDelete.left = None
                        toDelete.value = None
        except Exception as e:
            return "No Node Found"
            
def main():
    testTree = BST(Node(100))
    testTree.insert(testTree.root, 75)
    testTree.insert(testTree.root, 25)
    testTree.delete(25)
    
main()