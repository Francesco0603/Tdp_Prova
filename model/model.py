import copy

from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self.classificazioni = DAO.getClassif()
        self.localizzazioni = DAO.getLocaliz()
        self.locMap = {}
        self.interazioni = DAO.getInteraz()
        self.archi = {}
        self.ptot = 0
    def creaGrafo(self):
        self.grafo.add_nodes_from(self.localizzazioni)
        for c in self.classificazioni:
            if c.Localization in self.locMap.keys():
                self.locMap[c.Localization].append(c.GeneID)
            else:
                self.locMap[c.Localization] = [c.GeneID]
        for a in self.interazioni:
            self.grafo.add_edge(a[0],a[1],weight=a[2])
            self.ptot += a[2]
            self.archi[(a[0],a[1])] = a[2]
        print(self.grafo.number_of_nodes())
        print(self.grafo.number_of_edges())
        print(self.ptot)
    def cercaPercorso(self,l):
        self.lmax = 0
        self.bestPercorso = []
        print("dddddd")
        self.ricorsione([str(l)],1,[])
        return self.lmax,self.bestPercorso
    def ricorsione(self,parziale,lunghezza,archi):
        vicini = list(self.grafo.neighbors(parziale[-1]))
        if self.lmax <= lunghezza:
            self.lmax = lunghezza
            self.bestPercorso = copy.deepcopy(parziale)
            print(self.lmax)
            print(self.bestPercorso)
            print(len(archi))
        if len(archi) == self.ptot:
            return True
        for n in vicini:
            if (parziale[-1],n) in archi or (n,parziale[-1]) in archi:
                continue
            archi.append((parziale[-1], n))
            lunghezza += self.grafo[parziale[-1]][n]["weight"]
            parziale.append(n)
            if self.ricorsione(parziale,lunghezza,archi):
                return True
            parziale.pop()
            archi.pop()
            lunghezza -= self.grafo[parziale[-1]][n]["weight"]




