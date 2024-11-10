import copy

class Node():
    """
    A node in the tree is represented by a data structure with many components:

    node.STATE => the state to which the node corresponds. 
    node.PARENT => the node in the tree that generated this node.
    node.ACTION => the action that was applied to the parent's state to generate this node. 
    node.EMPTY_CELL_POSITION => the position of the empty cell (0) we will know by function find_zeros()
    """
    # how many instance of the Node class
    no_of_nodes = 0 

    def __init__(self, state, parent,empty_cell_position):
        self.state = state 
        self.parent = parent
        self.empty_cell_position = empty_cell_position
        Node.no_of_nodes += 1


def print_path(root):
    """
    the first passing in this argument is goal_state and it has 
    """
    if root == None:
        return
     
    print_path(root.parent)
    for i in root.state:
        print(i)
    print()

def new_node(state,parent,empty_cell_position,new_empty_cell_position):
     """
     
     """
     new_state = copy.deepcopy(state)
     x1 = empty_cell_position[0]
     y1 = empty_cell_position[1]
     x2 = new_empty_cell_position[0]
     y2 = new_empty_cell_position[1]

     new_state[x1][y1], new_state[x2][y2] = new_state[x2][y2], new_state[x1][y1]

     newNode = Node(state = new_state, parent = parent, empty_cell_position = new_empty_cell_position)

     return newNode

def find_zeros(state):
     """
     
     """
     for i in range(0,3):
          for j in range(0,3):
               if state[i][j] == 0:
                    empty_cell_position = [i,j]
                    return empty_cell_position
               
def manhattan(node):
    """
    Using manhattan method f(x) = g(x) + h 
    cost is always equal one so we didn't add it
    h(x) 
    """
    goal_keys = {
        "1": [0, 1],
        "2": [0, 2],
        "3": [1, 0],
        "4": [1, 1],
        "5": [1, 2],
        "6": [2, 0],
        "7": [2, 1],
        "8": [2, 2]
    }
    mat = node.state
    cost = 0
    for i in range(3):
        for j in range(3):
            x = mat[i][j]
            if x == 0:
                continue
            key = goal_keys[str(x)]
            cost += abs(i - key[0]) + abs(j - key[1])
    return cost



