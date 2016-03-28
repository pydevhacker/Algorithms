'''

'''

class TNode:
    def __init__(self):
        self.leaf = False
        self.t = {}

    def __str__(self):
        return str((self.leaf, self.t))

class Trie:
    def __init__(self):
        self.root = self.getNode()
        self.size = 0

    def getNode(self):
        return {'leaf':False, 'next':{}}

    def insert(self, key):
        key = list(key)
        node = self.root
        self.size += 1
        for k in key:
            if k not in node['next']:
                node['next'].setdefault(k, self.getNode())
            node = node['next'][k]
        node['leaf'] = True

    def search(self, key):
        key = list(key)
        node = self.root
        for k in key:
            if k not in node['next']:
                return False
            node = node['next'][k]
        return node and node['leaf']

    #key not present - do nothing
    #key present as unique - delete branch
    #key is prefix - mark leaf false
    #some other key is prefix - delete nodes after that key
    def delete(self, key):
        #check if key present
        if not self.search(key):
            return
        #check if any leaf true present in branch
        key = list(key)
        node = self.root
        leaf_count = 0
        last_prefix = None
        for k in key:
            node = node['next'][k]
            if node['leaf']:
                leaf_count += 1
                if len(node['next'])>0: last_prefix = node
        #unique key
        if leaf_count == 1 and len(node['next']) == 0:
            del self.root['next'][key[0]]
        elif len(node['next'])>0: #is prefix
            node['leaf'] = False
        else:
            last_prefix['next'] = {}

    def __str__(self):
        return str(self.root)


def test():
    keys = ['the', 'a', 'there', 'answer', 'any', 'by', 'bye', 'their','unique']
    trie = Trie()
    for k in keys:
        trie.insert(k)
    print(trie)
    print(trie.search('the'))
    print(trie.search('z'))
    print(trie.search('unique'))
    trie.delete('unique')
    print(trie.search('unique'))
    print(trie)


if __name__ == '__main__':
    test()