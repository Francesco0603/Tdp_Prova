import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
    def fillDD(self):

        for s in self._model.squadre:
            if s.teamCode not in self._model.codiciSquadre:
                self._model.codiciSquadre.append(s.name)
                self._model.nomiMap[s.teamCode] = s.name
                self._view.ddteam.options.append(ft.dropdown.Option(key=s.teamCode,text=s.name))
    def handle_graph(self,e):
        self._model.creaGrafo()
    def handle_details(self,e):
        pass
    def handle_simulation(self,e):
        pass