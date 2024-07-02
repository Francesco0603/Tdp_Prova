import copy
from random import random

from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self.geni = DAO.getGeniEssenziali()
        self.geniMap = {}
        self.interactions = DAO.getInteractions()

    def creaGrafo(self):
        for g in self.geni:
            self.geniMap[g.GeneID] = g
            self.grafo.add_node(g.GeneID)
        for a in self.interactions:
            if a[0] in self.grafo.nodes and a[1] in self.grafo.nodes:
                if self.geniMap[a[0]].Chromosome == self.geniMap[a[1]].Chromosome:
                    self.grafo.add_edge(a[0],a[1], weight=2*a[2])
                else:
                    self.grafo.add_edge(a[0],a[1], weight=a[2])
        print(self.grafo.number_of_nodes())
        print(self.grafo.number_of_edges())
    def creaSimulazione(self,n,g):
        self.ricorsione([g],n)
        return

    def ricorsione(self, n, months=36):
        # Start with each bioengineer studying a random gene
        bioengineers = [random.choice(list(self.grafo.nodes)) for _ in range(n)]

        for month in range(months):
            new_bioengineers = []
            for gene in bioengineers:
                if random < 0.3:
                    # 30% probability to continue with the same gene
                    new_bioengineers.append(gene)
                else:
                    # 70% probability to focus on an adjacent gene
                    neighbors = list(graph.neighbors(gene))
                    if neighbors:
                        weights = [graph[gene][neighbor]['weight'] for neighbor in neighbors]
                        total_weight = sum(weights)
                        probabilities = [weight / total_weight for weight in weights]
                        new_gene = random.choices(neighbors, probabilities)[0]
                        new_bioengineers.append(new_gene)
                    else:
                        new_bioengineers.append(gene)  # No neighbors, stay at the same gene
            bioengineers = new_bioengineers

        # Count the number of bioengineers at each gene
        gene_counts = {gene: bioengineers.count(gene) for gene in graph.nodes}
        return gene_counts
