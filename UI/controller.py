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
                self._model.codiciSquadre.append(s.teamCode)
            if s.teamCode not in self._model.nomiMap.keys():
                self._model.nomiMap[s.teamCode] = [s.name]
            else:
                self._model.nomiMap[s.teamCode].append(s.name)
            if s.name not in self._model.nomiSquadre:
                self._model.nomiSquadre.append(s.name)
                self._view.ddteam.options.append(ft.dropdown.Option(s.name))

    def handle_graph(self,e):
        squadra = self._view.ddteam.value
        self._model.creaGrafo(squadra)
    def handle_details(self,e):
        pass
    def handle_simulation(self,e):
        pass