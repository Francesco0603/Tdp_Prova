import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
    def handle_grafo(self):
        self._model.creaGrafo()
        self._view.txt_result.controls.append(ft.Text(f"Nodi #{self._model.grafo.number_of_nodes()}"))
        self._view.txt_result.controls.append(ft.Text(f"Archi #{self._model.grafo.number_of_edges()}"))
        for l in self._model.localizzazioni:
            self._view.ddlocalizzazione.options.append(ft.dropdown.Option(l))
    def handle_stat(self,e):
        l = self._view.ddlocalizzazione.value
        self._view.txt_result.controls.append(ft.Text(f"Adiacenti a {l}:"))
        for loc in self._model.grafo.neighbors(l):
            self._view.txt_result.controls.append(ft.Text(f"{loc} --> {self._model.grafo[l][loc]["weight"]}"))
        self._view.update_page()
    def handle_search(self,e):
        l = self._view.ddlocalizzazione.value
        lmax,percorso = self._model.cercaPercorso(l)
        self._view.txt_result.controls.append(ft.Text(f"{lmax}"))
        self._view.txt_result.controls.append(ft.Text(f"{percorso}"))
        self._view.update_page()


