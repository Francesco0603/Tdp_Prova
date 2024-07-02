import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
    def fillDD(self):
        for g in self._model.grafo.nodes:
            self._view.ddGene.options.append(ft.dropdown.Option(g))
        self._view.update_page()

    def handle_graph(self,e):
        self._model.creaGrafo()
        self._view.txt_result.controls.append(ft.Text(f"Numero vertici #{self._model.grafo.number_of_nodes()}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero nodi #{self._model.grafo.number_of_edges()}"))
        self.fillDD()
    def handle_adiacenti(self,e):
        g = self._view.ddGene.value
        self._view.txt_result.controls.append(ft.Text(f"geni adiacenti a {g}:"))
        for n in self._model.grafo.neighbors(g):
            self._view.txt_result.controls.append(ft.Text(f"{n}, peso: {self._model.grafo[g][n] ["weight"]}"))
        self._view.update_page()

    def handle_simulazione(self,e):
        numero = self._view.txt_name.value
        g = self._view.ddGene.value
        try:
            n = int(numero)
        except:
            print("non è intero!!")
        self._model.creaSimulazione(n,g)

        self._view.update_page()
