from Node import *
from queue import Queue

def Breadth_First_Search(initial_state, empty_cell_position, goal_state):
        node = Node(state = initial_state, parent = None,empty_cell_position = empty_cell_position)
        frontier = Queue()
        frontier.put(node)
        explored = set()
        while not frontier.empty():
             
             node = frontier.get() #pop 
             explored.add(tuple(map(tuple,node.state))) # [[,,],[,,],[,,]] => ((,,),(,,),(,,))

             if node.state == goal_state:
                   print("GOAL REACHED !!!\n")
                   print("Path to goal: " )
                   print_path(node)
                   print("Number of nodes :",node.no_of_nodes)
                   print("Number of explored nodes :",len(explored))
                   return node
             """
               Generate the possible children 
               we move left right down up 
               left right => change in column only
               ==>> when it moves left the column - 1
               ==>> when it moves right the column + 1 
               down up => change in row only 
               ==>> when it moves up the row - 1 
               ==>> when it moves down the row + 1  

               so we can generate like this row [-1,1,0,0] ----- col [0,0,-1,1] 
             """
             row = [-1,1,0,0]
             col = [0,0,-1,1]

             for i in range(4):
                  new_empty_cell_position = [
                              node.empty_cell_position[0] + row[i],
                              node.empty_cell_position[1] + col[i],]# [0,2]
                  
                  if(new_empty_cell_position[0] < 3 and new_empty_cell_position[1] < 3):
                       child = new_node(state = node.state, parent = node , 
                                        empty_cell_position= node.empty_cell_position, new_empty_cell_position=new_empty_cell_position)
                       
                       if tuple(map(tuple, child.state)) not in explored:
                        frontier.put(child)

if __name__ == "__main__":
    initial_state = [[1, 2, 5], [3, 4, 0], [6, 7, 8]]
    goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    Breadth_First_Search(initial_state=initial_state, empty_cell_position=find_zeros(initial_state), goal_state=goal_state)

