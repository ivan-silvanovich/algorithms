from collections import deque


class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}

    @staticmethod
    def __node_object_validation(node):
        if type(node) != Node:
            raise TypeError('only \'Node\' object is allowed')

    def check_connection(self, target_node) -> bool:
        self.__node_object_validation(target_node)

        checked_nodes = deque()
        nodes_queue = deque(self.neighbors.keys())

        while nodes_queue:
            node = nodes_queue.popleft()

            if node not in checked_nodes:
                if node == target_node:
                    return True
                else:
                    nodes_queue.extend(node.neighbors.keys())
                    checked_nodes.append(node)

        return False

    @staticmethod
    def __get_min_weight_unchecked_node(table: dict):
        min_weight = float('inf')
        min_weight_node = None

        for node in table:
            if table[node]['weight'] < min_weight and not table[node]['is_checked']:
                min_weight = table[node]['weight']
                min_weight_node = node

        return min_weight_node

    @staticmethod
    def __retrieve_route(table: dict, target_node):
        route = []
        parent_node = target_node

        while parent_node is not None:
            route.append(parent_node)
            parent_node = table[parent_node]['parent']

        return route[::-1]

    def search_route(self, target_node) -> tuple:
        self.__node_object_validation(target_node)

        if not self.check_connection(target_node):
            raise ValueError(f'{self} has no connections with {target_node}')

        table = {
            self: {
                'parent': None,
                'weight': 0,
                'is_checked': False
            }
        }

        while True:
            current_node = self.__get_min_weight_unchecked_node(table)

            if current_node == target_node:
                break

            for node, weight in current_node.neighbors.items():
                current_weight = table[current_node]['weight'] + weight
                if node not in table or current_weight < table[node]['weight']:
                    table[node] = {
                        'parent': current_node,
                        'weight': current_weight,
                        'is_checked': False
                    }

            table[current_node]['is_checked'] = True

        return table[target_node]['weight'], self.__retrieve_route(table, target_node)

    def __str__(self):
        return f'<Node:{self.name}>'

    def __repr__(self):
        return f'<Node:{self.name}>'

    def __setitem__(self, node, weight):
        self.__node_object_validation(node)
        self.neighbors[node] = weight

    def __getitem__(self, node):
        return self.neighbors[node]


if __name__ == '__main__':
    A, B, C, D, E, F, G = Node('A'), Node('B'), Node('C'), Node('D'), Node('E'), Node('F'), Node('G')

    A[B], A[C] = 5, 0
    B[D], B[E] = 15, 20
    C[D], C[E] = 30, 35
    D[F] = 20
    E[F] = 10

    # A[B], A[C] = 5, 2
    # B[D], B[E] = 4, 2
    # C[B], C[E] = 8, 7
    # D[E], D[F] = 6, 3
    # E[F] = 1

    # A[B] = 10
    # B[D] = 20
    # C[B] = 1
    # D[C], D[E] = 1, 30

    # A[B], A[C] = 2, 2
    # B[C] = 2
    # C[D], C[E] = 2, 2
    # D[B], D[E] = -1, 2

    # print(A)
    # print(A.search_route(E))
    print(A.search_route(F))
    # print(A.search_route(G))
