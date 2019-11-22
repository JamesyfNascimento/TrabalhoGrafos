class Grafo(object):
    def __init__(self, grafo=None):
        if grafo == None:
            grafo = {}
        self.__grafo = grafo

    def vertices(self):
        return list(self.__grafo())

    def arestas(self):
        return self.__arestas_grafo()

    def add_vertice(self, vertice):
        if vertice not in self.__grafo:
            self.__grafo[vertice] = []
    
    def add_aresta(self, aresta):
        aresta = set(aresta)
        verticeA = aresta.pop()
        if aresta:
            verticeB = aresta.pop()
        else:
            # loop AQUI
            verticeB = verticeA
        if verticeA in self.__grafo:
            self.__grafo[verticeA].append(verticeB)
        else:
            self.__grafo[verticeA] = [verticeB]



    def __arestas_grafo(self):
        arestas = []
        for vertice in self.__grafo:
            for vizinho in self.__grafo[vertice]:
                if {vizinho, vertice} not in arestas:
                    arestas.append({vertice, vizinho})
        return arestas

    

    def __str__(self):
        res = "Vertices: "
        for k in self.__grafo:
            res += str(k) + " "
        res += "\Arestas: "
        for edge in self.__arestas_grafo():
            res += str(edge) + " "
        return res

    def vertice_isolado(self):
        grafo = self.__grafo
        isolados = []
        for vertice in grafo:
            print(isolados, vertice)
            if not grafo[vertice]:
                isolados += [vertice]
        return isolados
    
    def eh_conexo(self, vertices_encontrados = None, vertice_inicio=None):
        if vertices_encontrados is None:
            vertices_encontrados = set()
        gdict = self.__grafo        
        vertices = list(gdict.keys()) 
        if not vertice_inicio:
            vertice_inicio = vertices[0]
        vertices_encontrados.add(vertice_inicio)

    def grau_vetice(self, vertice):
        adj_vertices =  self.__grafo[vertice]
        grau = len(adj_vertices) + adj_vertices.count(vertice)
        return grau

    def grau_maior_vertices(self):
        maior_grau = -1
        for vertice in self.__grafo:
            grau_vertice = self.grau_vetice(vertice)
            if grau_vertice > maior_grau:
                maior_grau = grau_vertice
        return maior_grau


g = { "va" : ["d"],
      "vb" : ["c"],
      "vc" : ["b", "c", "d", "e"],
      "vd" : ["a", "c"],
      "ve" : ["c"],
      "vf" : []
    }

grafo = Grafo(g)
print(grafo)
print(grafo.grau_maior_vertices())
