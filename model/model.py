import copy

from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self.squadre = DAO.getSquadre()
        self.anni = []
        self.nomiSquadre = []
        self.codiciSquadre = []
        self.nomiMap = {}
        self.anniMap = {}

        self.grafo = nx.Graph()
    def creaGrafo(self,squadra):
        for s in self.squadre:
            if s.name == squadra:
                self.anni.append(s.year)
                if s.year in self.anni:
                    self.anniMap[s.year].append(s.teamCode)
                else:
                    self.anniMap[s.year] = [s.teamCode]
                    self.grafo.add_node(s.year)
        for y1 in self.grafo.edges:
            for y2 in self.grafo.edges:
                peso = 0
                self.grafo.add_edge(y1,y2,weight=peso)
        print(self.grafo.number_of_nodes())
        print(self.grafo.number_of_edges())






