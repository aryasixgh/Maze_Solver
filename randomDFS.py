import random
from treeMaker import treeMaker

path = []

def dfs(graph, start_node, visited=None):
    """
    Performs a Depth-First Search (DFS) on a graph.

    Args:
        graph (dict): An adjacency list representation of the graph,
                      where keys are nodes and values are lists of their neighbors.
        start_node: The node from which to start the DFS traversal.
        visited (set, optional): A set to keep track of visited nodes.
                                 If None, an empty set is initialized.
    """
    if visited is None:
        visited = set()

    # Mark the current node as visited and process it (e.g., print it)
    visited.add(start_node)
    print(start_node, end=" ")

    # Recursively visit all unvisited neighbors
    # choiceList = []
    # for neighbor in graph[start_node]:
    #     if neighbor not in visited:
    #         choiceList.append(neighbor)
    
    # if len(choiceList) != 0:          
    #     randomNeighbour = random.choice(choiceList)
    #     dfs(graph, randomNeighbour, visited)

    random.shuffle(graph[start_node])
    for neighbor in graph[start_node]:  # Iterate through neighbors
       if neighbor not in visited:
            dfs(graph, neighbor, visited) 

# Example Usage:
if __name__ == "__main__":
    # Represent the graph using an adjacency list
    graph = treeMaker()

    print("DFS Traversal starting from 'A':")
    dfs(graph, 1)
    print("\n")

    # Another example with a different starting node
    print("DFS Traversal starting from 'D':")
    #dfs(graph, 2)
    print("\n")