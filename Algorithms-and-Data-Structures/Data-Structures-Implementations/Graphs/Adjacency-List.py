class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_neighbor(self, neighbor, weight=0):
        self.connected_to[neighbor] = weight

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connected_to])

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.connected_to[neighbor]


class Graph:
    def __init__(self):
        self.vertices_list = {}
        self.num_of_vertices = 0

    def addVertex(self, key):
        self.num_of_vertices = self.num_of_vertices + 1
        new_vertex = Vertex(key)
        self.vertices_list[key] = new_vertex
        return new_vertex

    def getVertex(self, key):
        if key in self.vertices_list:
            return self.vertices_list[key]
        else:
            return None

    def __contains__(self, key):
        return key in self.vertices_list

    def addEdge(self, f, t, weight=0):
        if f not in self.vertices_list:
            nv = self.addVertex(f)
        if t not in self.vertices_list:
            nv = self.addVertex(t)
        self.vertices_list[f].addNeighbor(self.vertices_list[t], weight)

    def getVertices(self):
        return self.vertices_list.keys()

    def __iter__(self):
        return iter(self.vertices_list.values())
