from functools import partial

import xlsxwriter
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy_garden.matplotlib import FigureCanvasKivyAgg
from matplotlib import pyplot as plt

from models.gestionModel import GestionModel
from kivy.clock import Clock
from kivy.metrics import dp
from kivymd.theming import ThemeManager
from kivymd.uix.pickers import MDDockedDatePicker, MDTimePickerDialVertical, MDTimePickerDialHorizontal, \
    MDModalDatePicker
from typing import Literal

from utilities.databases import to_database


def pourcentage(self,nom_pourcentage="pv",date=None,date_fin=None,order=""):
    if self.widget_showed: self.clear_widgets()
    labels = []
    sizes = []
    instance = GestionModel()
    if nom_pourcentage=='pv':
        produits = instance.get_pourcentage_produits_vendus(date, date_fin,order)

    if nom_pourcentage=='dep':
        produits = instance.get_pourcentage_depense(date,date_fin)
    if not produits: return None

    for row in produits:
        labels.append(row[0])
        sizes.append(row[1])

    fig, ax = plt.subplots()

    if len(labels) <= 10 and order=="":

        # Camembert
        explode = [0.1] + [0] * (len(labels) - 1)  # Explose seulement la première part
        ax.pie(sizes, labels=labels, textprops={'fontsize': 9},
               autopct='%1.1f%%', shadow=True, startangle=140, explode=explode)
        self.add_widget(FigureCanvasKivyAgg(fig))

    else:
        if nom_pourcentage == 'pv':
            data = []

            for row in produits:
                data.append({
                    'product_name': str(row[0]),
                    'sale_percent': str(row[1])
                })
            pourcentagepvg=App.get_running_app().manager.ids.statsscreen.ids.statsspage.ids.salescontainer.ids.pourcentagepvg
            pourcentagepvg.ids.pv.data = data
            pourcentagepvg.clear_widgets()
            pourcentagepvg.add_widget(pourcentagepvg.ids.pv)


    self.widget_showed = True

def show_popup(self,title, message):
    popup = Popup(size_hint=(.4,.4))
    popup.title = title
    content = BoxLayout(orientation='vertical')
    label=Label(text=message)
    button = Button(text='ok',size_hint=(.3,.3),pos_hint={'right':.94,'y':.012})
    button.bind(on_press=popup.dismiss)
    for w in (label,button):content.add_widget(w)
    popup.content=content
    popup.open()
def show_popup_confirmation(self,title,message,nom,qt,pu=None):
    self.popup = Popup(size_hint=(.4, .4))
    self.popup.title = title
    content = BoxLayout(orientation='vertical')
    label = Label(text=message)
    boxbutton = BoxLayout(orientation='horizontal')
    button1 = Button(text='Confirmer', size_hint=(.3, .3), pos_hint={'right': .94, 'y': .012})
    button1.bind(on_press=partial(self.popup.dismiss,qt,pu))
    button2 = Button(text='Annuler', size_hint=(.3, .3), pos_hint={'right': .94, 'y': .012})
    button2.bind(on_press=self.popup_confirmed)
    for w in (button1,button2):boxbutton.add_widget(w)
    for w in (label, boxbutton): content.add_widget(w)
    self.popup.content = content
    self.popup.open()
def popup_confirmed(self,nom,qt,pu=None):
    self.popup.dismiss()
    if pu:to_database("update stock set qt=qt+%s pu=%s where nom=%s",(qt,pu,nom))
    else:to_database("update stock set qt=qt+%s where nom=%s",(qt,nom))



"""ORIENTATION = Literal["landscape","portrait"]

def orientation(self, instance: ThemeManager, orientation: ORIENTATION):
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
"""
def show_time_picker_horizontal(self, hour, minute):
    self.time_picker_vertical = None
    self.time_picker_horizontal = MDTimePickerDialHorizontal(
        hour=hour, minute=minute
    )
    self.time_picker_horizontal.open()

def show_time_picker_vertical(self, hour, minute):
    self.time_picker_horizontal = None
    self.time_picker_vertical = MDTimePickerDialVertical(
        hour=hour, minute=minute
    )
    self.time_picker_vertical.open()

def date_picker(self):

    date_dialog = MDDockedDatePicker()
    # You have to control the position of the date picker dialog yourself.
    date_dialog.pos = [
        self.ids.date_button.center_x - date_dialog.width / 2,
        self.ids.date_button.y - (date_dialog.height + dp(32)),
    ]
    date_dialog.bind(on_ok=self.on_ok_date)
    date_dialog.open()

def modal_date_picker(self, *args):

    date_dialog = MDModalDatePicker(mode="range")
    # You have to control the position of the date picker dialog yourself.
    date_dialog.pos = [
        self.ids.date_button.center_x - date_dialog.width / 2,
        self.ids.date_button.y - (date_dialog.height + dp(32)),
    ]
    date_dialog.bind(on_ok=self.on_ok_periode)
    date_dialog.open()

def generate_fic_excel(title,column_title, datas,):
    # Créer un nouveau fichier Excel
    workbook = xlsxwriter.Workbook(f'{title}.xlsx')
    worksheet = workbook.add_worksheet()
    for i in range(len(column_title)):
        worksheet.write(0,i,str(column_title[i]))

    for data in enumerate(datas):
        for item in enumerate(data[1]):
            worksheet.write(data[0]+1,item[0], str(item[1]))

    # Fermer le fichier
    workbook.close()

data = [('banane',2),('citron',5),('orange',6),('pommes','8')]
generate_fic_excel('fruit5',('modeles','quantité'),data)

