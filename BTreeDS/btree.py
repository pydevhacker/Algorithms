'''
- all leafs are at same level
- min degree 't'
- every node except root must contain t-1 keys
- root may contain min 1 key
- every node must contain at most 2t-1 keys
- no of children of a node is equal to number of keys + 1
- All keys of node are stored in increasing order
- the child between k1 and k2 contains all keys in range from k1 and k2
- Time complexity is O(logn)
'''

class BTreeNode:
    def __init__(self, keys=list(), t=0, children=list(), n=0, leaf=True):
        self.keys = keys
        self.t = t #min degree
        self.children = children
        self.n = n
        self.leaf = leaf

    # i is the index of child y in children list and y is the node that is full and need to be split
    def splitChild(self, i, y):
        #create a node which will store t-1 keys
        z = BTreeNode(t=self.t, n=self.t-1, leaf=self.leaf)
        for i in range(self.t-1):
            z.keys.append(self.keys[i])