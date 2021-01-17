from src.GraphInterface import GraphInterface
from src.node_data import Node


class DiGraph(GraphInterface):

    def __init__(self, graph: dict = None, countOfGraphChanges: int = 0, countOfEdgeChanges: int = 0):
        if graph is None:
            graph = {}
        self.graph = graph
        self.countOfGraphChanges = countOfGraphChanges
        self.countOfEdgeChanges = countOfEdgeChanges

    def v_size(self) -> int:
        return len(self.graph.keys())

    def e_size(self) -> int:
        return self.countOfEdgeChanges

    def get_all_v(self) -> dict:
        new_graph = dict({})
        ll = self.graph.keys()
        for x in ll:
            node = self.graph.get(x)
            ls = [x, node]
            tup = tuple(ls)
            new_graph[x] = tup
        return new_graph

    def all_in_edges_of_node(self, id1: int) -> dict:
        to_return = {}
        for x in self.graph.keys():
            if x is id1:
                pass
            node = self.graph.get(x)
            if id1 in node.get_edges().keys():
                ll = [id1, node.get_edges()[id1]]
                tup = tuple(ll)
                to_return[x] = tup
        return to_return

    def all_out_edges_of_node(self, id1: int) -> dict:
        to_return = {}
        node = self.graph.get(id1)
        if len(node.get_edges()) == 0:
            pass
        for x in node.get_edges().keys():
            ll = [id1, node.get_edges()[x]]
            tup = tuple(ll)
            to_return[x] = tup
        return to_return

    def get_mc(self) -> int:
        return self.countOfGraphChanges

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 not in self.graph.keys():
            return False
        if id2 not in self.graph.keys():
            return False
        node = self.graph.get(id1)
        if id2 in node.get_edges():
            return False
        if id1 in self.graph.keys() and id2 in self.graph.keys():
            self.graph[id1].addNeighbor(id2, weight)
            self.countOfEdgeChanges += 1
            self.countOfGraphChanges += 1
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        node: Node = Node(node_id)
        if pos is not None:
            print(pos[0])
            node.set_position(pos[0], pos[1], pos[2])
        li = self.graph.keys()
        if node_id in li:
            pass
        else:
            self.graph[node_id] = node
            self.countOfGraphChanges += 1
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.graph.keys():
            pass
        else:
            self.graph.pop(node_id)
            self.countOfGraphChanges += 1
            for i in self.graph:
                node = self.graph.get(i)
                if node_id in node.get_edges():
                    self.graph.get(i).get_edges().pop(node_id)
                    # self.countOfEdgeChanges -= 1
                    # self.countOfGraphChanges += 1
                return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        keys = self.graph.get(node_id1).get_edges().keys()
        if node_id2 not in keys:
            pass
        else:
            self.graph.get(node_id1).get_edges().pop(node_id2)
            self.countOfEdgeChanges -= 1
            self.countOfGraphChanges += 1
            return True
        return False

    def __str__(self):
        return f"Graph -> graph: {self.graph} , count_Edge_changes: {self.countOfEdgeChanges} , count_graph_changes :{self.countOfGraphChanges}"
