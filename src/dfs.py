from Node import *
from queue import LifoQueue

def Depth_First_Search(initial_state, empty_cell_position, goal_state):
    node = Node(state=initial_state, parent=None, empty_cell_position=empty_cell_position)

    frontier = LifoQueue() 
    frontier.put(node)
    explored = set()

    while not frontier.empty():
        node = frontier.get()  # pop from stack
        explored.add(tuple(map(tuple, node.state)))

        if node.state == goal_state:
            print("GOAL REACHED!!!\n")
            print("Path to goal:")
            print_path(node)
            print("Number of nodes :",node.no_of_nodes)
            print("Number of explored nodes :",len(explored))
            return node
        
        row = [0,0,-1,1]
        col = [-1,1,0,0]
        for i in range(4):
            new_empty_cell_position = [
                node.empty_cell_position[0] + row[i],
                node.empty_cell_position[1] + col[i],
            ]
            # Check if new position is within bounds (assuming 3x3 grid)
            if 0 <= new_empty_cell_position[0] < 3 and 0 <= new_empty_cell_position[1] < 3:
                # Generate a child node
                child = new_node(
                    state=node.state,
                    parent=node,
                    empty_cell_position=node.empty_cell_position,
                    new_empty_cell_position=new_empty_cell_position
                )

                # Avoid re-exploring already visited states
                if tuple(map(tuple, child.state)) not in explored:
                    frontier.put(child)

if __name__ == "__main__":

    initial_state = [[1, 2, 5], [3, 4, 0], [6, 7, 8]]
    goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    Depth_First_Search(initial_state=initial_state, empty_cell_position=find_zeros(initial_state), goal_state=goal_state)
