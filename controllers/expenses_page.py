import datetime
from kivy.metrics import dp
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog, MDDialogContentContainer
from kivymd.uix.divider import MDDivider
from kivymd.uix.label import MDLabel
from kivymd.uix.pickers import MDTimePickerDialHorizontal
from kivymd.uix.pickers import MDModalDatePicker
from models.gestionModel import GestionModel
from utilities.databases import to_database


class SelectYear(MDLabel):
    i = 2000
    current_year = datetime.datetime.now().year
    range_number = current_year - 2000
    text = current_year


class ExpensesPage(MDBoxLayout):
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
    def open_time_picker_horizontal(self,hour, minute):
        self.show_time_picker_horizontal(hour, minute)
    def open_time_picker_vertical(self,hour, minute):
        self.show_time_picker_vertical( hour, minute)
    def show_date_picker(self):
        self.date_picker()
    def show_modal_date_picker(self, *args):
        self.modal_date_picker()


    def on_ok_date(self, instance_date_picker):
        date = instance_date_picker.get_date()[0]
        self.ids.listedepense.show_expenses(date)
        instance_date_picker.dismiss()



    def on_ok_periode(self, instance_date_picker):
        date_debut = instance_date_picker.get_date()[0]
        date_fin = instance_date_picker.get_date()[-1]
        self.ids.listedepense.show_expenses(date_debut, date_fin)
        instance_date_picker.dismiss()

    def show_year(self):
        select_month_card = self.ids.select_month_year
        year_dialog = MDDialog(
            MDDialogContentContainer(
                MDDivider(),
                select_month_card
            ),

        )
        year_dialog.open()

    def add_expense(self):
        nom = self.ids.nom_depense.text
        somme = self.ids.somme_depense.text

        def get_id_depense_and_increment():
            gestionmodel = GestionModel()
            try:
                lastrow = gestionmodel.get_last_row_depense
            except:
                lastrow = 'DEP000'
            number = int(lastrow[3:])
            number += 1
            new_id = 'DEP' + f'{number:03d}'
            print(new_id)
            return new_id

        id = get_id_depense_and_increment()
        to_database("INSERT INTO depense(id_dep,nom_dep,somme_dep) VALUES(%s,%s,%s)",
                    (id, nom, somme))
        self.ids.listedepense.show_expenses()
        self.ids.labelsommeportefeuille.update_somme_portefeuille()


class LabelSommePortefeuille(Label):
    somme_portefeuille = StringProperty('')

    def __init__(self, **kwargs):
        super(LabelSommePortefeuille, self).__init__(**kwargs)
        #self.text = 'je ne sais pas'
        self.update_somme_portefeuille()

    def update_somme_portefeuille(self):
        gestionmodel = GestionModel()
        self.somme_portefeuille = str(gestionmodel.get_somme_portefeuille)


class ListeDepense(ScrollView):
    grid_showed = False
    grid = None
    instance = GestionModel()
    desc = False
    sort_by = 'date_dep'

    def __init__(self, **kwargs):
        super(ListeDepense, self).__init__(**kwargs)

    def show_expenses(self, date=None, date_fin=None, order=None):
        if self.grid_showed: self.remove_widget(self.grid)
        if not order:
            order ={'date_dep': False}
            self.desc=False
        if self.sort_by != list(order.keys())[0]:
            self.sort_by = list(order.keys())[0]
            self.desc = False
        else: self.desc = not self.desc

        self.grid = GridLayout(cols=3, spacing=2, size_hint_y=None)
        self.grid.bind(minimum_height=self.grid.setter('height'))

        # TITRES CLIQUABLES
        titles = [('DATE', 'date_dep'), ('NOM', 'nom_dep'), ('SOMME', 'somme_dep')]
        for text, column in titles:
            btn = Button(
                text=text,
                size_hint=(1, None),
                height=30,
                bold=True
            )
            btn.bind(on_press=lambda instance, col=column: self.show_expenses(date, date_fin, order={col: self.desc}))
            self.grid.add_widget(btn)

        # DONNÉES
        depenses = self.instance.get_expenses(order, date, date_fin)
        for row in depenses:
            for item in row:
                cell = Label(text=f'{item}', color=(.2, .2, .2, 1), size_hint=(1, None), height=40)
                self.grid.add_widget(cell)

        self.add_widget(self.grid)
        self.grid_showed = True

    def update_expenses(self):
        row = self.instance.get_last_depense
        for item in row:
            cell = Label(text=f'{item}', color=(.2, .2, .2, 1), size_hint=(1, None), height=40)
            self.grid.add_widget(cell)


import os

from kivy.lang import Builder

kv_path = os.path.join(os.path.dirname(__file__), '..', 'view', 'expenses_page.kv')
Builder.load_file(kv_path)
