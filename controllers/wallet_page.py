from datetime import datetime
import datetime
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivymd.theming import ThemeManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog, MDDialogContentContainer
from kivymd.uix.divider import MDDivider
from kivymd.uix.label import MDLabel
from kivymd.uix.pickers import MDTimePickerDialHorizontal, MDTimePickerDialVertical, MDDockedDatePicker
from typing import Literal
from kivymd.uix.pickers import MDModalDatePicker

from models.gestionModel import GestionModel


class SelectMonth(MDCard):
    pass

class SelectYear(MDLabel):
    i = 2000
    current_year = datetime.datetime.now().year
    range_number = current_year - 2000
    text = current_year



class WalletPage(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        device_orientation = self.check_orientation
    ORIENTATION = Literal["portrait", "landscape"]
    time_picker_horizontal: MDTimePickerDialHorizontal = ObjectProperty(
        allownone=True
    )
    time_picker_vertical: MDTimePickerDialHorizontal = ObjectProperty(
        allownone=True
    )

    date_picker_horizontal: MDModalDatePicker = ObjectProperty(
        allownone=True
    )
    date_picker_vertical: MDModalDatePicker = ObjectProperty(
        allownone=True
    )


    def check_orientation(
        self, instance: ThemeManager, orientation: ORIENTATION
    ):
        if orientation == "portrait" and self.time_picker_horizontal:
            self.time_picker_horizontal.dismiss()
            hour = str(self.time_picker_horizontal.time.hour)
            minute = str(self.time_picker_horizontal.time.minute)
            Clock.schedule_once(
                lambda x: self.open_time_picker_vertical(hour, minute),
                0.1,
            )
        elif orientation == "landscape" and self.time_picker_vertical:
            self.time_picker_vertical.dismiss()
            hour = str(self.time_picker_vertical.time.hour)
            minute = str(self.time_picker_vertical.time.minute)
            Clock.schedule_once(
                lambda x: self.open_time_picker_horizontal(hour, minute),
                0.1,
            )
        if orientation == "portrait" and self.date_picker_horizontal:
            self.date_picker_horizontal.dismiss()
            day = str(self.date_picker_horizontal.date.minute)
            minute = str(self.date_picker_horizontal.date.minute)
            Clock.schedule_once(
                lambda x: self.open_date_picker_vertical(hour, minute),
                0.1,
            )
        elif orientation == "landscape" and self.date_picker_vertical:
            self.date_picker_vertical.dismiss()
            hour = str(self.date_picker_vertical.date.hour)
            minute = str(self.date_picker_vertical.date.minute)
            Clock.schedule_once(
                lambda x: self.open_date_picker_horizontal(hour, minute),
                0.1,
            )

    def open_time_picker_horizontal(self, hour, minute):
        self.time_picker_vertical = None
        self.time_picker_horizontal = MDTimePickerDialHorizontal(
            hour=hour, minute=minute
        )
        self.time_picker_horizontal.open()

    def open_time_picker_vertical(self, hour, minute):
        self.time_picker_horizontal = None
        self.time_picker_vertical = MDTimePickerDialVertical(
            hour=hour, minute=minute
        )
        self.time_picker_vertical.open()

    def show_date_picker(self):

        date_dialog = MDDockedDatePicker()
        # You have to control the position of the date picker dialog yourself.
        date_dialog.pos = [
            self.ids.date_button.center_x - date_dialog.width / 2,
            self.ids.date_button.y - (date_dialog.height + dp(32)),
        ]
        date_dialog.bind(on_ok=self.on_ok_date)
        date_dialog.open()
    def on_ok_date(self,instance_date_picker):
        date  =instance_date_picker.get_date()[0]
        self.ids.historique.show_historique(date)
        instance_date_picker.dismiss()

    def show_modal_date_picker(self, *args):

        date_dialog =  MDModalDatePicker(mode="range")
        # You have to control the position of the date picker dialog yourself.
        date_dialog.pos = [
            self.ids.date_button.center_x - date_dialog.width / 2,
            self.ids.date_button.y - (date_dialog.height + dp(32)),
        ]
        date_dialog.bind(on_ok=self.on_ok_periode)
        date_dialog.open()


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
    def __init__(self,**kwargs):
        super(Historique,self).__init__(**kwargs)


    def show_historique(self,date=None,date_fin=None):
        if self.grid_showed:
            self.remove_widget(self.grid)
            self.grid = None
        self.grid = GridLayout(cols=3,spacing=2,size_hint_y=None)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        depenses = self.instance.get_historique(date,date_fin)
        titles = ('DATE','NOM','SOMME')
        for i in enumerate(titles):
            cell = Label(text=i[1], color=(0, 0, 0, 1), bold=True, size_hint=(1, None), height=20)
            if i[0]==4:
                cell.size_hint=(.45,None)
            self.grid.add_widget(cell)
        for row in depenses:
            for item in range(len(row)):
                cell = Label(text = f'{row[item]}',color=(.2,.2,.2,1),size_hint=(1,None),height=20)
                self.grid.add_widget(cell)
        self.add_widget(self.grid)
        self.grid_showed = True
    def update_historique(self):
        row = self.instance.get_last_historique
        for item in row:
            cell = Label(text=f'{item}', color=(.2, .2, .2, 1), size_hint=(1, None), height=20)
            self.grid.add_widget(cell)




import os

kv_path = os.path.join(os.path.dirname(__file__), '..', 'view', 'wallet_page.kv')
Builder.load_file(kv_path)