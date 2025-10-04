import datetime

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog, MDDialogContentContainer
from kivymd.uix.divider import MDDivider
from kivymd.uix.label import MDLabel
from kivymd.uix.pickers import MDTimePickerDialHorizontal
from kivymd.uix.pickers import MDModalDatePicker

from models.gestionModel import GestionModel
from utilities.myfunctions import show_month, show_year


class SelectMonth(MDCard):
    pass

class SelectYear(MDLabel):
    i = 2000
    current_year = datetime.datetime.now().year
    range_number = current_year - 2000
    text = current_year



class WalletPage(MDBoxLayout):
    time_picker_vertical: MDTimePickerDialHorizontal = ObjectProperty(allownone=True)
    date_picker_horizontal: MDModalDatePicker = ObjectProperty(allownone=True)
    date_picker_vertical: MDModalDatePicker = ObjectProperty(allownone=True)
    #from utilities.myfunctions import orientation
    from utilities.myfunctions import show_time_picker_horizontal
    from utilities.myfunctions import show_time_picker_vertical
    from utilities.myfunctions import date_picker
    from utilities.myfunctions import modal_date_picker
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #device_orientation = self.check_orientation

    """def check_orientation(self):
        self.orientation()"""

    def open_time_picker_horizontal(self, hour, minute):
        self.show_time_picker_horizontal(hour, minute)

    def open_time_picker_vertical(self, hour, minute):
        self.show_time_picker_vertical(hour, minute)

    def show_date_picker(self):
        self.date_picker()

    def show_modal_date_picker(self, *args):
        self.modal_date_picker()

    def show_month_picker(self):
        def on_month_selected(date_debut, date_fin):
            order = {"date_dep": False}
            self.ids.historique.show_historique(date=date_debut.strftime("%Y-%m-%d"),
                                                date_fin=date_fin.strftime("%Y-%m-%d"),
                                                order=order)

        show_month(on_month_selected)

    def show_year_picker(self):
        def on_year_selected(selected_year):
            # Utilise l'année sélectionnée pour construire la plage de dates
            date_debut = f"{selected_year}-01-01"
            date_fin = f"{selected_year}-12-31"
            order = {"date_dep": False}

            self.ids.historique.show_historique(date=date_debut, date_fin=date_fin, order=order)

        show_year(on_year_selected)
    def on_ok_date(self,instance_date_picker):
        date  =instance_date_picker.get_date()[0]
        self.ids.historique.show_historique(date)
        instance_date_picker.dismiss()

    def on_ok_periode(self,instance_date_picker):
        date_debut=instance_date_picker.get_date()[0]
        date_fin = instance_date_picker.get_date()[-1]
        self.ids.historique.show_historique(date_debut,date_fin)
        instance_date_picker.dismiss()
    def show_year(self):
        select_month_card=self.ids.select_month_year
        year_dialog = MDDialog(
            MDDialogContentContainer(
                MDDivider(),
                select_month_card
                ),
        )
        year_dialog.open()

class Historique(ScrollView):
    grid_showed = False
    grid = None
    instance = GestionModel()
    desc = True
    sort_by = 'date'
    def __init__(self,**kwargs):
        super(Historique,self).__init__(**kwargs)

    def show_historique(self, date=None, date_fin=None, order=None):
        if self.grid_showed:
            self.remove_widget(self.grid)

        # Initialiser une liste pour stocker les labels
        self.historique_labels = []  # Liste pour les cellules de données
        self.historique_headers = []  # Liste pour les en-têtes

        if not order:
            order = {'date': True}

        if self.sort_by == list(order.keys())[0]:
            self.desc = not self.desc
        else:
            self.sort_by = list(order.keys())[0]
            self.desc = True

        self.grid = GridLayout(cols=3, spacing=2, size_hint_y=None)
        self.grid.bind(minimum_height=self.grid.setter('height'))

        # TITRES CLIQUABLES
        titles = [('DATE', 'date'), ('SOMME', 'somme'), ('NOM', 'mouvement')]
        for text, column in titles:
            arrow = ""
            if self.sort_by == column:
                arrow = " ▲" if self.desc else " ▼"

            btn = Button(
                text=f"{text}{arrow}",
                size_hint=(1, None),
                height=30,
                bold=True,
                color=(1,1,1,1)
            )
            btn.bind(on_press=lambda instance, col=column: self.show_historique(date, date_fin, order={col: self.desc}))
            self.historique_headers.append(btn)  # Stocker la référence
            self.grid.add_widget(btn)

        # DONNÉES
        depenses = self.instance.get_historique(order, date, date_fin)
        for row in depenses:
            for item in row:
                cell = Label(
                    text=f'{item}',
                    color=App.get_running_app().text_color,
                    size_hint=(1, None),
                    height=40
                )
                self.historique_labels.append(cell)  # Stocker la référence
                self.grid.add_widget(cell)

        self.add_widget(self.grid)
        self.grid_showed = True

    def update_historique(self):
        row = self.instance.get_last_historique
        for item in row:
            cell = Label(text=f'{item}', color=(.2, .2, .2, 1), size_hint=(1, None), height=40)
            self.grid.add_widget(cell)


import os

kv_path = os.path.join(os.path.dirname(__file__), '..', 'view', 'wallet_page.kv')
Builder.load_file(kv_path)