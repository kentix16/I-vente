from collections import defaultdict
from datetime import datetime
from itertools import cycle
from typing import Literal

import matplotlib.dates as mdates

from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.graphics import Mesh, Color, Rectangle
from kivy.metrics import dp
from kivy.properties import ListProperty, StringProperty, NumericProperty, ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scrollview import ScrollView
from kivymd.theming import ThemeManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy_garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivymd.uix.label import MDLabel
from kivymd.uix.pickers import MDTimePickerDialHorizontal, MDModalDatePicker, MDTimePickerDialVertical, \
    MDDockedDatePicker
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.screen import MDScreen
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from models.gestionModel import GestionModel

# Pour les variantes spécifiques comme SemiBold et Black
LabelBase.register(name="OutfitSemiBold", fn_regular="font/Outfit-SemiBold.ttf")
LabelBase.register(name="OutfitBlack", fn_regular="font/Outfit-Black.ttf")

KV = '''
<CommonComponentLabel>
    halign: "center"


<MobileView>
    CommonComponentLabel:
        text: "Mobile"


<TabletView>
    CommonComponentLabel:
        text: "Table"


<DesktopView>
    CommonComponentLabel:
        text: "Desktop"


ResponsiveView:
'''

import os

kv_path = os.path.join(os.path.dirname(__file__), '..', 'view', 'statistics_page.kv')
Builder.load_file(kv_path)

class StatDeVenteGlobal(MDCard):
    widget_showed = False
    def __init__(self, **kwargs):
        super(StatDeVenteGlobal, self).__init__(**kwargs)

    def show_stat_global(self,date=None):
        if self.widget_showed:
            self.clear_widgets()

        salemodel = GestionModel()
        if date:rows = salemodel.get_heures_stat_global(date)
        else:rows = salemodel.get_heures_stat

        heures = [datetime.strptime(str(row[0]), '%Y-%m-%d %H:%M:%S') for row in rows]
        montants = [row[1] for row in rows]

        # Grouper par tranche de 10 minutes
        donnees_par_10min = defaultdict(float)
        for heure, montant in zip(heures, montants):
            minute = (heure.minute // 10) * 10
            heure_arrondie = heure.replace(minute=minute, second=0, microsecond=0)
            donnees_par_10min[heure_arrondie] += montant

        heures_groupees = sorted(donnees_par_10min.keys())
        montant_groupes = [donnees_par_10min[h] for h in heures_groupees]

        couleurs_palette = ['#1abc9c', '#16a085']
        couleurs_alternees = [couleurs_palette[i % len(couleurs_palette)] for i in range(len(heures_groupees))]

        fig, ax = plt.subplots(figsize=(10, 5))
        bars = ax.bar(heures_groupees, montant_groupes, width=0.006, color=couleurs_alternees, edgecolor='black',
                      linewidth=0.5)

        for bar, montant in zip(bars, montant_groupes):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2.0, height + 0.5, f"{montant:.0f}", ha='center', va='bottom',
                    fontsize=9, color="#333")

        # Format des dates : ticks majeurs toutes les heures
        ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

        # Optionnel : repères mineurs toutes les 10 minutes
        # ax.xaxis.set_minor_locator(mdates.MinuteLocator(interval=10))

        fig.autofmt_xdate()
        ax.grid(True, linestyle='--', alpha=0.4)
        fig.patch.set_facecolor("#f7f7f7")
        ax.set_facecolor('#f0f0f0')
        ax.set_ylabel("Prix ($)", fontsize=12)
        ax.set_xlabel("Heure", fontsize=12)
        plt.xticks(rotation=45)
        fig.tight_layout()

        self.add_widget(FigureCanvasKivyAgg(fig))
        self.widget_showed = True



class PourcentagePV(RelativeLayout):
    widget_showed = False

    def __init__(self, **kwargs):
        super(PourcentagePV, self).__init__(**kwargs)

    def show_pourcentage_pv(self,date=None):
        if self.widget_showed: self.clear_widgets()
        labels = []
        sizes = []
        instance = GestionModel()
        produits = instance.get_pourcentage_produits_vendus(date)
        for row in produits:
            labels.append(row[0])
            sizes.append(row[1])

        explode = (0.1, 0, 0, 0)  # mettre en avant la première part

        # Création de la figure
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, textprops={'fontsize': 9},
               autopct='%1.1f%%', shadow=True, startangle=140)
        # Ajout du canvas dans l'interface Kivy
        self.add_widget(FigureCanvasKivyAgg(fig))
        self.widget_showed = True


class StatsPage(MDBoxLayout):
    total_de_ventes = StringProperty('0')
    somme_total_gagnee = StringProperty('0 ar')
    produits_en_rupture = StringProperty('0')
    gestionmodel = GestionModel()

    def __init__(self, **kwargs):
        super(StatsPage, self).__init__(**kwargs)
        self.update_total_de_ventes()
        self.update_somme_total_gagnee()
        self.update_produits_en_rupture()

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
        date_dialog.bind(on_select_day=self.on_ok_date)
        date_dialog.open()
    def on_ok_date(self,instance_date_picker,number_day):
        date  =instance_date_picker.get_date()[0]
        self.ids.statedeventeglobal.show_stat_global(date)
        self.update_somme_total_gagnee(date)
        self.update_total_de_ventes(date)
        self.ids.pourcentagedepense.show_pourcentage_depense(date)
        instance_date_picker.dismiss()

    def show_modal_date_picker(self, *args):

        date_dialog = MDModalDatePicker(mode="range")
        # You have to control the position of the date picker dialog yourself.
        date_dialog.pos = [
            self.ids.date_button.center_x - date_dialog.width / 2,
            self.ids.date_button.y - (date_dialog.height + dp(32)),
        ]
        date_dialog.bind(on_ok=self.on_ok_periode)
        date_dialog.open()
    def on_ok_periode(self,instance_date_picker):
        date = instance_date_picker.get_date()[0]
        date_fin = instance_date_picker.get_date()[-1]
        self.ids.statedeventeglobal.show_stat_global(date)
        self.update_somme_total_gagnee(date)
        self.update_total_de_ventes(date)
        self.ids.pourcentagedepense.show_pourcentage_depense(date,date_fin)
        instance_date_picker.dismiss()




    def update_total_de_ventes(self,date=None):
        total_de_ventes = self.gestionmodel.get_total_de_ventes(date)
        self.total_de_ventes = str(total_de_ventes)

    def update_somme_total_gagnee(self,date=None):
        somme_total_gagnee = self.gestionmodel.get_somme_total_gagnee(date)
        self.somme_total_gagnee = str(somme_total_gagnee) + ' ar'

    def update_produits_en_rupture(self):
        produits_en_rupture = self.gestionmodel.get_produits_en_rupture
        self.produits_en_rupture = str(produits_en_rupture)


class DefaultLabel(MDLabel):
    def __init__(self, **kwargs):
        kwargs.setdefault("font_style", "OutfitMedium")
        kwargs.setdefault("role", "medium")
        super().__init__(**kwargs)


class CommonComponentLabel(MDLabel):
    pass


class MobileView(MDScreen):
    pass


class TabletView(MDScreen):
    pass


class DesktopView(MDScreen):
    pass


class ResponsiveView(MDResponsiveLayout, MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.mobile_view = MobileView()
        self.tablet_view = TabletView()
        self.desktop_view = DesktopView()


class GradientNavigationDrawer(MDNavigationDrawer):
    pass


class PourcentageDepense(ScrollView):
    grid_showed = False
    grid = None
    widget_showed = False

    def __init__(self, **kwargs):
        super(PourcentageDepense, self).__init__(**kwargs)

    def show_pourcentage_depense(self,date=None,date_fin=None):
        if self.widget_showed: self.clear_widgets()
        labels = []
        sizes = []
        instance = GestionModel()
        produits = instance.get_pourcentage_depense(date,date_fin)
        for row in produits:
            labels.append(row[0])
            sizes.append(row[1])

        explode = (0.1, 0, 0, 0)  # mettre en avant la première part

        # Création de la figure
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, textprops={'fontsize': 9},
               autopct='%1.1f%%', shadow=True, startangle=140)
        # Ajout du canvas dans l'interface Kivy
        self.add_widget(FigureCanvasKivyAgg(fig))
        self.widget_showed = True


