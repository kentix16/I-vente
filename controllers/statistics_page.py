import numpy as np
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy_garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivymd.uix.label import MDLabel
from kivymd.uix.pickers import MDTimePickerDialHorizontal, MDModalDatePicker
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.screen import MDScreen
from matplotlib import pyplot as plt
from controllers.sales_page import PourcentagePV
from models.gestionModel import GestionModel
from utilities.myfunctions import show_year, show_month
from datetime import datetime, timedelta

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
    from utilities.myfunctions import exist_data
    widget_showed = False
    def __init__(self, **kwargs):
        super(StatDeVenteGlobal, self).__init__(**kwargs)

    def show_stat_global(self, date=None, date_fin=None):
        self.clear_widgets()

        salemodel = GestionModel()

        if not date_fin:
            # Single day, hourly data
            heure_min_vente = salemodel.get_min_max_heures_vente(order="MIN", date=date)
            heure_max_vente = salemodel.get_min_max_heures_vente(order="MAX", date=date) + 1
            heure_min_dep = salemodel.get_min_max_heures_dep(order="MIN", date=date)
            heure_max_dep = salemodel.get_min_max_heures_dep(order="MAX", date=date) + 1
            heure_min = f"{min(heure_min_vente, heure_min_dep)}"
            heure_max = f"{max(heure_max_vente, heure_max_dep)}"

            ventes = salemodel.get_heures_somme_stat(date=date, heure_min=heure_min, heure_max=heure_max)
            depense = salemodel.get_heures_depense_stat(date=date, heure_min=heure_min, heure_max=heure_max)


            dates_ventes = [row[0] for row in ventes]
            montants = [row[1] for row in ventes]
            depense_vals = [row[1] for row in depense]

            min_len = min(len(dates_ventes), len(montants), len(depense_vals))
            for i in range(100):print(montants)
            if not self.exist_data(montants, depense_vals):
                self.add_widget(Label(text="Pas de données suffisantes pour générer le graphique.",color=(0,0,0,1)))
                return

            dates = dates_ventes[:min_len]
            montants = montants[:min_len]
            depense_vals = depense_vals[:min_len]

            x_label = "Heure"
            x_labels = [d.strftime('%H:%M') if hasattr(d, 'strftime') else str(d) for d in dates]
        else:
            # Date range, daily data
            if isinstance(date, str):
                date = datetime.strptime(date, '%Y-%m-%d')
            if isinstance(date_fin, str):
                date_fin = datetime.strptime(date_fin, '%Y-%m-%d')

            # Generate list of dates in the range
            delta = (date_fin - date).days + 1
            dates = [date + timedelta(days=i) for i in range(delta)]

            # Aggregate data for each day

            ventes = salemodel.get_somme_statistique_periode(date,date_fin)
            depense = salemodel.get_depense_statistique_periode(date,date_fin)
            for i in range(100):
                for vente in ventes:
                    print(f"fente:{vente[1]}")

            # Sum values for the day
            montant = sum(row[1] for row in ventes) if ventes else 0
            depense_val = sum(row[1] for row in depense) if depense else 0
            montants = [vente[1] for vente in ventes ]
            depense_vals = [dep[1] for dep in depense]

            min_len = min(len(dates), len(montants), len(depense_vals))
            if not self.exist_data(montants, depense_vals):
                self.add_widget(Label(text="Pas de données suffisantes pour générer le graphique.",color=(0,0,0,1)))
                return

            """dates = dates[:min_len]
            montants = montants[:min_len]
            depense_vals = depense_vals[:min_len]"""

            x_label = "Jour"
            x_labels = [d.strftime('%Y-%m-%d') for d in dates]

        # Create the plot
        fig, ax = plt.subplots(figsize=(10, 6))
        x = np.arange(min_len)
        bar_width = 0.35

        ax.bar(x+bar_width/2, montants, width=bar_width, label='Vente', color='turquoise')
        ax.bar(x +3* bar_width / 2, depense_vals, width=bar_width, label='Dépense', color='mediumpurple')

        ax.set_title("Ventes & Dépenses")
        ax.set_xlabel(x_label)
        ax.set_ylabel("Montant ($)")
        ax.set_xticks(x)
        ax.set_xticklabels(x_labels, rotation=45)
        ax.legend()
        ax.grid(axis='y', linestyle="--", alpha=0.7)
        fig.tight_layout()

        self.add_widget(FigureCanvasKivyAgg(fig))

        widget_showed = True


class StatsPage(MDBoxLayout):
    total_de_ventes = StringProperty('0')
    somme_nette_total_gagnee = StringProperty('0 ar')
    produits_en_rupture = StringProperty('0')
    gestionmodel = GestionModel()
    avg_gain = StringProperty('')
    avg_dep=StringProperty('')
    time_picker_vertical: MDTimePickerDialHorizontal = ObjectProperty(allownone=True)
    date_picker_horizontal: MDModalDatePicker = ObjectProperty(allownone=True)
    date_picker_vertical: MDModalDatePicker = ObjectProperty(allownone=True)
    #from utilities.myfunctions import orientation
    from utilities.myfunctions import show_time_picker_horizontal
    from utilities.myfunctions import show_time_picker_vertical
    from utilities.myfunctions import date_picker
    from utilities.myfunctions import modal_date_picker

    def __init__(self, **kwargs):
        super(StatsPage, self).__init__(**kwargs)
        gestionmodel=GestionModel()
        self.update_total_de_ventes()
        self.update_somme_total_gagnee()
        self.update_produits_en_rupture()
        self.avg_gain=f'moyenne gain:{gestionmodel.get_average_gains()[0]}'
        self.avg_dep= f'moyenne depense:{gestionmodel.get_average_depense()[0]}'


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
            self.ids.statedeventeglobal.show_stat_global(date=date_debut.strftime("%Y-%m-%d"),
                                                date_fin=date_fin.strftime("%Y-%m-%d"))

        show_month(on_month_selected)

    def show_year_picker(self):
        def on_year_selected(selected_year):
            # Utilise l'année sélectionnée pour construire la plage de dates
            date_debut = f"{selected_year}-01-01"
            date_fin = f"{selected_year}-12-31"
            order = {"date_dep": False}

            self.ids.statedeventeglobal.show_stat_global(date=date_debut, date_fin=date_fin)

        show_year(on_year_selected)
    def on_ok_date(self,instance_date_picker,):
        date  =instance_date_picker.get_date()[0]

        #self.ids.salescontainer.date = date
        #self.ids.salescontainer.date_fin = None
        self.ids.statedeventeglobal.show_stat_global(date)
        self.update_somme_total_gagnee(date)
        self.update_total_de_ventes(date)
        #self.ids.pourcentagedepense.show_pourcentage_depense(date)
        #self.ids.salescontainer.ids.pourcentagepvg.show_pourcentage_pv(date=date)
        instance_date_picker.dismiss()

    def on_ok_periode(self,instance_date_picker):
        date = instance_date_picker.get_date()[0]
        date_fin = instance_date_picker.get_date()[-1]

        #self.ids.salescontainer.date = date
        #self.ids.salescontainer.date_fin = date_fin

        self.ids.statedeventeglobal.show_stat_global(date,date_fin)
        self.update_somme_total_gagnee(date)
        self.update_total_de_ventes(date)
        #self.ids.salescontainer.ids.pourcentagepvg.show_pourcentage_pv(date,date_fin)
        #self.ids.pourcentagedepense.show_pourcentage_depense(date,date_fin)
        instance_date_picker.dismiss()




    def update_total_de_ventes(self,date=None):
        total_de_ventes = self.gestionmodel.get_total_de_ventes(date)
        self.total_de_ventes = str(total_de_ventes)

    def update_somme_total_gagnee(self,date=None):
        somme_total_gagnee = self.gestionmodel.get_somme_nette_totale_gagnee(date)
        self.somme_nette_total_gagnee = str(somme_total_gagnee) + ' ar'

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





