import copy

from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self.squadre = DAO.getSquadre()
        self.anni = []
        self.codiciSquadre = []
        self.nomiMap = {}

        self.grafo = nx.Graph()
    def creaGrafo(self):
        for s in self.squadre:
            if s.year not in self.anni and s.teamCode in self.codiciSquadre:
                self.anni.append(s.year)
                self.grafo.add_node(s.year)
        for n1 in self.grafo.edges:
            for n2 in self.grafo.edges:
                pass
        print(self.grafo.number_of_nodes())
        print(self.grafo.number_of_edges())






