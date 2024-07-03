import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
    def handle_graph(self,e):
        anno = self._view.txt_anno.value
        giorni = self._view.txt_giorni.value
        self._model.creaGrafo(anno,giorni)
        for n in self._model.grafo.edges():
            self._view.txt_result.controls.append(ft.Text(f"{self._model.grafo[n[0]][n[1]["weight"]]}"))
        self._view.update_page()