class Vertex():
    
    def __init__(self, vertex_value, vertex):
        self.vertex_value = vertex_value
        self.vertex = vertex
        self.adjacent = {}

    def add_neighbor(self, adj_vertex):
        self.adjacent[adj_vertex.vertex_value] = adj_vertex


class Graph():

    def __init__(self):
        self.verticies = {}
        self.verticies_len = 0

    def add_vertex(self, vertex_value):
        self.verticies_len += 1
        new_vertex = Vertex(vertex_value)
        self.verticies[vertex_value] = new_vertex
    
    def get_verticies(self):
        return self.verticies.keys()

    def add_edge(self, vertex_value, adj_vertex_value):

        current_vertex = self.verticies[vertex_value]
        if 
        



if __name__ == '__main__':

    test_graph = Graph()
    test_graph.add_vertex('A')
    print(test_graph.get_verticies())