import queue
from typing import List

import networkx as nx
from matplotlib.patches import ConnectionPatch
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
import json
import matplotlib.pyplot as plt
from src.node_data import Node
import random


def adjusted_graph(graph: str) -> DiGraph():
    to_return = DiGraph()
    nodes_list = []
    json_obj = json.loads(graph)
    ll_temp1 = json_obj.get("Nodes")
    i = 0
    j = -1
    while i < len(ll_temp1):
        nodes_list.append(ll_temp1[i].get("id"))
        i = i + 1
    for n in nodes_list:
        j = j + 1
        node_id = n
        node = Node(node_id)
        pos = ll_temp1[j].get("pos")
        if pos is not None:
            p1 = pos.index(",")
            p2 = pos.rindex(",")
            x = pos[0: p1]
            y = pos[p1 + 1: p2]
            z = pos[p2 + 1:]
            node.set_position(x, y, z)
            to_return.add_node(node.get_key(), node.get_position())
        else:
            to_return.add_node(node.get_key())
    ll_temp2 = json_obj.get("Edges")
    for i in ll_temp2:
        src = i.get("src")
        weight = i.get("w")
        dest = i.get("dest")
        to_return.add_edge(src, dest, weight)
    return to_return.graph


def min_max_values(ll) -> tuple:
    min_value = min(ll)
    max_value = max(ll)
    ll_ans = [min_value, max_value]
    ans = tuple(ll_ans)
    return ans


def init_nodes_tag(graph: DiGraph):
    # initialize the nodes tags - to avoid problems in cases of activating the function several times in a row
    for n in graph.graph:
        node = graph.graph.get(n)
        node.set_tag(float('inf'))


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, Graph_Algo: DiGraph = DiGraph()):
        self.Graph_Algo = Graph_Algo
        self.predecessor = {}
        for node_key in self.Graph_Algo.graph.keys():
            self.predecessor[node_key] = None

    def get_graph(self) -> GraphInterface:
        return self.Graph_Algo

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "r") as file:
                st = file.read().replace("\n", " ")
                to_return = adjusted_graph(st)
                self.Graph_Algo.graph = to_return
                return True
        except IOError as e:
            print(e)
        return False

    def save_to_json(self, file_name: str) -> bool:
        list_of_nodes = []
        list_of_edges = []
        G = {}
        for n in self.Graph_Algo.graph.keys():
            node = self.Graph_Algo.graph.get(n)
            pos = node.get_position()
            temp_node = {}
            temp_node.update({"id": node.get_key()})
            if pos is not None:
                pos0 = str(pos[0])
                pos1 = str(pos[1])
                pos2 = str(pos[2])
                pos = pos0 + "," + pos1 + "," + pos2
                temp_node.update({"pos": pos})
            list_of_nodes.append(temp_node)
            for e in node.get_edges().keys():
                src = n
                dest = e
                weight = node.get_edges()[e]
                temp_edge = {}
                temp_edge.update({"src": src})
                temp_edge.update({"w": weight})
                temp_edge.update({"dest": dest})
                list_of_edges.append(temp_edge)
        G.update({"Edges:": list_of_edges})
        G.update({"Nodes:": list_of_nodes})
        try:
            with open(file_name, "w") as file:
                json.dump(G, indent=4, fp=file)
                return True
        except IOError as e:
            print(e)
        return False

    def DijkstraAlgorithm(self, source):
        GraphAlgo(self.Graph_Algo)
        key = self.Graph_Algo.graph.get(source)
        Pq = queue.PriorityQueue()
        key.set_tag(0)
        Pq.put((key.get_tag(), key))
        while not Pq.empty():
            temp = Pq.get()
            Ni: list = []
            for i in temp[1].get_edges().keys():
                t = self.Graph_Algo.graph.get(i)
                Ni.append(t)
            for i in Ni:
                if i.get_info() == "false":
                    distance = temp[0] + temp[1].get_edges()[i.get_key()]
                    if i.get_tag() > distance:
                        i.set_tag(distance)
                        self.predecessor[i.get_key()] = temp[1]
                        Pq.put((i.get_tag(), i))
            temp[1].set_info("true")

    def shortest_path_value(self, id1: int, id2: int) -> float:
        if id1 not in self.Graph_Algo.graph.keys() or id2 not in self.Graph_Algo.graph.keys():
            return float('inf')
        GraphAlgo(self.Graph_Algo)
        self.DijkstraAlgorithm(id1)
        temp = self.Graph_Algo.graph.get(id2)
        if temp.get_tag() is float('inf'):
            return float('inf')
        return temp.get_tag()

    def shortest_path_List(self, id1: int, id2: int) -> list:
        if id1 not in self.Graph_Algo.graph.keys() or id2 not in self.Graph_Algo.graph.keys():
            return []
        ans = []
        GraphAlgo(self.Graph_Algo)
        self.DijkstraAlgorithm(id1)
        temp = self.Graph_Algo.graph.get(id2)
        while temp is not None and temp is not self.Graph_Algo.graph.get(id1):
            ans.append(temp.get_key())
            temp = self.predecessor.get(temp.get_key())
        if temp is None:
            return []
        ans.append(temp.get_key())
        ans.reverse()
        return ans

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        init_nodes_tag(self.Graph_Algo)
        return self.shortest_path_value(id1, id2), self.shortest_path_List(id1, id2)

    def BFS_Algorithm_in_edges(self, source):
        init_nodes_tag(self.Graph_Algo)
        qu = []
        temp_ans = []
        component = []
        for i in self.Graph_Algo.graph:
            node_temp = self.Graph_Algo.graph.get(i)
            node_temp.set_mark("WHITE")
        node_source = self.Graph_Algo.graph.get(source)
        node_source.set_mark("GRAY")
        qu.append(source)
        while len(qu) != 0:
            i = qu.pop(0)
            for j in self.Graph_Algo.all_in_edges_of_node(i):
                node = self.Graph_Algo.graph.get(j)
                if node.get_mark() == "WHITE":
                    node.set_mark("GRAY")
                    qu.append(j)
                    temp_ans.append(j)
        for i in temp_ans:
            node = self.Graph_Algo.graph.get(i)
            if node.get_mark() == "GRAY":
                component.append(i)
        return component

    def BFS_Algorithm_out_edges(self, source):
        init_nodes_tag(self.Graph_Algo)
        qu = []
        temp_ans = []
        component = []
        for i in self.Graph_Algo.graph:
            node_temp = self.Graph_Algo.graph.get(i)
            node_temp.set_mark("WHITE")
        node_source = self.Graph_Algo.graph.get(source)
        node_source.set_mark("GRAY")
        qu.append(source)
        while len(qu) != 0:
            i = qu.pop()
            for j in self.Graph_Algo.all_out_edges_of_node(i):
                node = self.Graph_Algo.graph.get(j)
                if node.get_mark() == "WHITE":
                    node.set_mark("GRAY")
                    qu.append(j)
                    temp_ans.append(j)
        for i in temp_ans:
            node = self.Graph_Algo.graph.get(i)
            if node.get_mark() == "GRAY":
                component.append(i)
        return component

    def connected_components(self) -> List[list]:
        ans = []
        added = []
        for i in self.Graph_Algo.graph:
            if i not in added:
                component = self.connected_component(i)
                ans.append(component)
                added.extend(component)
        return ans

    def connected_component(self, id1: int) -> list:
        if id1 not in self.Graph_Algo.graph:
            return []
        ll_in_edges = self.BFS_Algorithm_in_edges(id1)
        ll_out_edges = self.BFS_Algorithm_out_edges(id1)
        ans = list((set(ll_out_edges) & set(ll_in_edges)))
        ans.insert(0,id1)
        return ans

    def random_position(self, node: int) -> tuple:
        node_ans = self.Graph_Algo.graph.get(node)
        random_x = random.uniform(0.0, 15.0)
        random_y = random.uniform(0.0, 30.0)
        random_z = random.uniform(0, 0)
        ll = [random_x, random_y, random_z]
        tup = tuple(ll)
        return tup

    def plot_graph(self) -> None:
        ll_x = []
        ll_y = []
        ll_id = []
        p = plt.subplot()
        pos_list = []
        # place and draw all the nodes in there position
        for n in self.Graph_Algo.graph:
            node = self.Graph_Algo.graph.get(n)
            temp_pos = node.get_position()
            if temp_pos is None:
                for i in range(len(self.Graph_Algo.graph)):
                    t_pos = self.random_position(n)
                    pos_list.append(t_pos)
                k = 0
                for m in self.Graph_Algo.graph:
                    to_pos = self.Graph_Algo.graph.get(m)
                    to_pos.set_position(pos_list[k][0], pos_list[k][1], pos_list[k][2])
                    k = k + 1
            temp_pos = node.get_position()
            ll_x.append(float(temp_pos[0]))
            ll_y.append(float(temp_pos[1]))
            ll_id.append(node.get_key())
        x_tup = min_max_values(ll_x)
        min_x = x_tup[0]
        max_x = x_tup[1]
        y_tup = min_max_values(ll_y)
        min_y = y_tup[0]
        max_y = y_tup[1]
        j = 0
        i = 0

        # adjust the graph positions to the graph drawing
        for x in ll_x:
            ll_x[j] = (ll_x[j] - min_x + max_x) * (max_x / (max_x - min_x + max_x))
            j = j + 1
        for y in ll_y:
            ll_y[i] = (ll_y[i] - min_y) * (0.009 / (max_y - min_y))
            i = i + 1
        for i, txt in enumerate(ll_id):
            p.annotate(ll_id[i], (ll_x[i], ll_y[i] + 0.00005))
        k = 0

        # connect each node to its neighbors
        for n in self.Graph_Algo.graph:
            node = self.Graph_Algo.graph.get(n)
            node.set_position(ll_x[k], ll_y[k], 0.0)
            k = k + 1
        for n in self.Graph_Algo.graph:
            node = self.Graph_Algo.graph.get(n)
            tup_point1 = node.get_position()
            x1 = tup_point1[0]
            y1 = tup_point1[1]
            z1 = tup_point1[2]
            for e in node.get_edges():
                node_e = self.Graph_Algo.graph.get(e)
                tup_point2 = node_e.get_position()
                x2 = tup_point2[0]
                y2 = tup_point2[1]
                z2 = tup_point2[2]
                A = (x1, y1)
                B = (x2, y2)
                # drawing the connection between the nodes (the edges of the graph)
                con = ConnectionPatch(A, B, "data", "data", arrowstyle="->", mutation_scale=15, color="black")
                p.plot([A[0], B[0]], [A[1], B[1]], "go")
                p.add_artist(con)
        plt.show()

    def nx_graph(self, file) -> nx.DiGraph:
        try:
            with open(file, "r") as file:
                st = file.read().replace("\n", " ")
                dicton = json.loads(st)

        except IOError as e:
            print(e)
        Graph = nx.DiGraph()
        ll_nodes = dicton["Nodes"]
        ll_edges = dicton["Edges"]
        for i in ll_nodes:
            node = i["id"]
            Graph.add_node(node)
        for i in ll_edges:
            src = i["src"]
            dest = i["dest"]
            weight = i["w"]
            Graph.add_edge(src, dest, weight=weight)
        return Graph

    def __str__(self):
        return f"GraphAlgo -> graph: {self.Graph_Algo.graph}"
