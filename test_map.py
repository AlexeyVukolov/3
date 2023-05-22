from btree_map import BTree

while True:
    num = input('1: Создать\n'
              '2: Удалить\n'
              '3: Найти\n'
              '4: Все деревья\n'
              '5: Выход\n')
    if num:
        if num == '1':
            key = int(input('Введите ключ\n'))
            value = input('Введите данные\n')
            BTree.add_Node(key, value)
        elif num == '2':
            selection = input('1: Удалить по ключу\n'
                               '2: Удалить все\n')
            if selection:
                if selection == '1':
                    key = int(input('Введите ключ\n'))
                    BTree.remove_key(int(key))
                elif selection == '2':
                    BTree.remove_all()
        elif num == '3':
            key = int(input('Введите ключ\n'))
            BTree.key_value(int(key))
        elif num == '4':
            BTree.print_Tree()
        elif num == '5':
            break