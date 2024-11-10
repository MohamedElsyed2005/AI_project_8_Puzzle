from Node import * 
from queue import PriorityQueue

def aStar(initial_state, empty_cell_position, goal_state):
    node = Node(state=initial_state, parent=None, empty_cell_position=empty_cell_position)
    frontier = PriorityQueue()
    count = 0  
    frontier.put((manhattan(node), count, node))
    explored = set()

    while not frontier.empty():
        _, _, node = frontier.get() 
        explored.add(tuple(map(tuple, node.state)))

        if node.state == goal_state:
            print("GOAL REACHED !!!\n")
            print("Path to goal:")
            print_path(node)
            print("Number of nodes :",node.no_of_nodes)
            print("Number of explored nodes :",len(explored))
            return node

        # Possible moves: up, down, left, right
        row = [-1, 1, 0, 0]
        col = [0, 0, -1, 1]

        for i in range(4):
            new_row = node.empty_cell_position[0] + row[i]
            new_col = node.empty_cell_position[1] + col[i]

            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_empty_cell_position = [new_row, new_col]
                child = new_node(
                    state=node.state,
                    parent=node,
                    empty_cell_position=node.empty_cell_position,#old
                    new_empty_cell_position=new_empty_cell_position
                )

                if tuple(map(tuple, child.state)) not in explored:
                    count += 1
                    frontier.put((manhattan(child), count, child))  

if __name__ == "__main__":
    initial_state = [[1, 2, 5], [3, 4, 0], [6, 7, 8]]
    goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    aStar(initial_state=initial_state, empty_cell_position=find_zeros(initial_state), goal_state=goal_state)