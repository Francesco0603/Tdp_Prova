import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None

        # graphical elements
        self._title = None
        self.txt_name = None

        self.btn_graph = None
        self.btn_countedges = None
        self.btn_search = None

        self.txt_result = None
        self.txt_result2 = None
        self.txt_result3 = None

        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("ESAME 01/06/2023", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        self.txt_name = ft.TextField(
            label="ingegneri(n)",
            width=200,
        )
        self.btn_grafo = ft.ElevatedButton(text="Crea Grafo",width=500, on_click=self._controller.handle_graph)
        self.btn_adiacenti = ft.ElevatedButton(text="Geni Adiacenti", on_click=self._controller.handle_adiacenti)
        self.btn_simulazione = ft.ElevatedButton(text="Simulazione", on_click=self._controller.handle_simulazione)

        self.ddGene = ft.Dropdown(label="gene",width=200)


        row1 = ft.Row([self.btn_grafo],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        row2 = ft.Row([self.ddGene, self.btn_adiacenti],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        row3 = ft.Row([self.txt_name, self.btn_simulazione],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()


        self._page.update()
    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
