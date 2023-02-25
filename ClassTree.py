class Node:
    # children - массив исходящих вершин (наследников)
    # parent - входящая вершина (родитель)
    # value - содержание ноды
    def __init__(self, children: list, parent, value):
        self.children = children
        self.parent = parent
        self.value = value

    # возвращает предка
    def get_parent(self):
        return self.parent

    # возвращает линию предков
    def get_parents_line(self) -> list:
        buff = self
        parents = []
        while buff:
            parents += buff
            buff = buff.parent
        return parents

    # добавляет наследника
    def add_child(self, node):
        self.children += node

    # возврает массив наследников
    def get_children(self) -> list:
        return self.children


class ClassTree:
    # root - корень дерева
    def __init__(self, root: Node):
        self.root = root

    # проверяет содержит ли дерево циклы
    def is_valid(self, node: Node = None, visited: set = None) -> bool:
        if not node:
            node = self.root
        if not visited:
            visited = set()
        visited.add(node)
        for child in node.children:
            if child in visited:
                return False
            if not self.is_valid(child, visited):
                return False
        return True

    # возращает первого общего предка
    def get_common_parent(self, node1: Node, node2: Node) -> Node:
        parents1 = node1.get_parents_line()
        parents2 = node2.get_parents_line()
        for node in parents1:
            if node in parents2:
                return node
        raise Exception("function get_common_parent can not find the common parent")




