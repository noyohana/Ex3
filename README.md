**Directed weighted graph**

- This project contains:
    1. [General information about the project's structure](#1)
    2. [Main algorithms in the project](#2)
       
    
**Part 1: Directed weighted graph python implementation**
___

<div id = '1'/>

**General information about the project's structure**
___

Our graph is built from dictionary of node's keys and node's data. 
Each node is built from key (the node id), dictionary Edges that represents the edges in the graph (the keys in the 
dictionary are the destination nodes id, and the values are the weight of the edge), info and tag (are used for algorithms 
in the project)
  
The main classes are: 
  * **DiGraph**: this class represent the structure of the graph. This class implements the following basic methods:

      * `v_size`: this method returns the number of vertices in the graph.
      * `e_size`: this method returns the number of edges in the graph.
      * `get_all_v`: this method returns dictionary of all the nodes in the graph (the nodes represented using a tuple of node id and node data)
      * `all_in_edges_of_node(id1)`: this method returns dictionary of all the node connected in to the node with the given id (the node
        represented by tuple of id and weight)
      * `all_out_edges_of_node`: this method returns a dictionary of all the nodes connected from the node with the given id 
        (the nodes are represented by tuple of destination node and weight of the edge between them)
      * `get_mc`: this method returns the number of changes that made on the graph
      * `add_edge(src,dest,weight)`: this method adds an edge to the graph return true if the edge was added false otherwise .
        If the edge already exists or one of the nodes dose not exists the functions will do nothing
      * `add_node(id,pos)`: this method adds node to the graph with the given id (key), and the given position (tuple)  
        return true if the node was added false otherwise if the node doesn't exist the method will do nothing
      * `remove_node(node_id)`: this method removes the node with the given id from the graph and return true if the node removed, false otherwise. if the node id does not 
        exist the function will do nothing
      * `remove_edge(node_id1, node_id2)`: this method remove the edge between the two given nodes keys from the graph and return true if the edge removed, false otherwise. If such an edge does not 
        exist the function will do nothing


  * **GraphAlgo**: this class represent the algorithms we can preform on the graph. This class implements the following basic methods:

      * `get_graph`:this method return the graph we work on.
      * `load_from_json(file_name)`: this method loads the graph from a json file return true if the loading was successful, false otherwise 
      * `save_to_json(file_name)`: this method  Saves the graph in JSON format to a file return true if the saving was successful, false otherwise
      * `shortest_path(int id1, int id2)`: this method returns the length of the shortest path from the source node and list of the node's id that the path
        are built from. If there is no path it will return (('inf', [])). This method using Dijkstra Algorithm implementation (Detailed below)
      * `connected_component(id)`: this method returns a list of the strongly connected component that the node with the given id is part of
      * `connected_components`: this method returns a list of all the strongly connected components in the graph
      * `plot_graph`: this method plots the graph
    
    
  * **node_data**: this class represents the structure of node in the graph. This class implements the following basic methods:
     
      * `get_key`: this method returns the key of the node
      * `get_info`: this method returns the info value of the node
      * `set_info(i)`: this method set the info value of the node to the given string info 
      * `get_tag`: this method returns the tag value of the node
      * `set_tag(i)`: this method set the tag value of the node to the given float tag
      * `get_edges()`: this method returns the dictionary of the node edges
      * `get_position()`: this method returns a tuple of the position of the node
      * `set_position(x,y,z)`: this method set the position of the node to the given position
      * `addNeighbor(node,weight)`: this method adding to the node's edges list another node with the given id (for key) and weight (for value)
   
<div id = '2'/>

**Main algorithms in the project**
___

  1. **Dijkstra algorithm**: This algorithm found the shortest distances from one node (vertex) to each other.
        This algorithm sums the weight of the edges in the graph and save the distances from the node to each other node. 
        How it works:
        This algorithm gets the key of the source node.
        The algorithm goes through all the neighbors of the key value and check the distance (by the weights of the edges) between 
        the source node to each other.
        The algorithm uses three main values:
           * boolean value - use the info value of the node. The default info is "false". The algorithm marks the info value with "true" if we went over all its neighbors.
           * float value - use the tag value of the node. The default value for each vertex is infinity. The algorithm store in the tag value the 
              distance between the nodes and compare different paths distances to save the lowest distance. After all nodes marked we can retrieve the information and use it in other methods in the project.
           * dictionary predecessor - to follow the predecessor of the node during the traverse.
          
  2. **BFS**:This algorithm traverse the graph and mark each node with color:
     This algorithm traverse the graph and mark the nodes to avoid repeating them
     We used the BFS principal to traverse the graph and find connected components from each node to its neighbors 
     and then traverse again from nodes that our current node is there neighbor.
     
     
     
      
       




