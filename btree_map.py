from BTrees.OOBTree import OOBTree

class BTree:

    bt = OOBTree()

    @staticmethod
    def add_Node(key, value):
        BTree.bt[key] = value


    @staticmethod
    def print_Tree():
        if BTree.size():
            for pair in BTree.bt.iteritems():
                print(pair)

    @staticmethod
    def size():
        if len(BTree.bt) == 0:
            return False
        else:
            return True

    @staticmethod
    def key_value(key):
        if BTree.size():
                if key in BTree.bt:
                    print(BTree.bt[key])
                else:
                    print("Ключ не найден")

    @staticmethod
    def remove_key(key):
        if BTree.size():
            del BTree.bt[key]

    @staticmethod
    def remove_all():
        if BTree.size():
            for i in list(BTree.bt.keys()):
                del BTree.bt[i]
        print("Дерево удалено")