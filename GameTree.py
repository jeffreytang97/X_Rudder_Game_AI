class Node(object):
    def __init__(self, potential_board, potential_coordinate):
        # Attributes are the state of the board during in any given node, as well as the coordinates played to get there
        self.potential_board = potential_board
        self.potential_coordinate = potential_coordinate
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

# references: https://stackoverflow.com/questions/2482602/a-general-tree-implementation