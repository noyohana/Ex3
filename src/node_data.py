class Node:

    def __init__(self, key: int = None, Tag: float = float('inf'), mark: str = "", Info: str = "false",
                 Position: tuple = None):
        self.key = key
        self.Info = Info
        self.Tag = Tag
        self.Edges = {}
        self.mark = mark
        self.Position = Position

    def get_key(self) -> int:
        return self.key

    def get_info(self) -> str:
        return self.Info

    def set_info(self, i):
        self.Info = i

    def get_tag(self) -> int:
        return self.Tag

    def set_tag(self, t):
        self.Tag = t

    def get_mark(self):
        return self.mark

    def set_mark(self,m):
        self.mark=m

    def get_edges(self) -> dict:
        return self.Edges

    def get_position(self) -> tuple:
        return self.Position

    def set_position(self, x, y, z):
        position = [x, y, z]
        self.Position = tuple(position)

    def addNeighbor(self, node, weight):
        self.Edges[node] = weight

    def __str__(self):
        return f"key: {self.key}, Tag: {self.Tag}, Info:{self.Info}, Edges:{self.Edges},Position:{self.Position}"

    def __repr__(self):
        return f"[Node -> key:{self.key},Tag: {self.Tag}, Info:{self.Info}, Edges:{self.Edges}, Position:{self.Position}]"
