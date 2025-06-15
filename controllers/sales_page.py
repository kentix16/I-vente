from collections import defaultdict
from datetime import datetime

import numpy as np
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.properties import ListProperty, StringProperty, NumericProperty
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy_garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivymd.uix.label import MDLabel
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
class StatToday(MDCard):
    stat_showed = False
    def __init__(self,**kwargs):
        super(StatToday,self).__init__(**kwargs)

    def show_stat(self):
        if self.stat_showed:self.clear_widgets()
        salemodel = GestionModel()
        rows = salemodel.get_heures_stat
        heures = [row[0] for row in rows]
        somme = [valeur[1] for valeur in rows]

        fig,ax = plt.subplots(figsize=(10, 6))
class StatDeVente(MDCard):
    widget_showed = False

    def __init__(self, **kwargs):
        super(StatDeVente, self).__init__(**kwargs)

    def show_stat_du_jour(self):
        self.clear_widgets()
        salemodel = GestionModel()
        heure_min_vente = salemodel.get_min_max_heures_vente(order="MIN")
        heure_max_vente = salemodel.get_min_max_heures_vente(order="MAX")
        heure_min_dep = salemodel.get_min_max_heures_dep(order="MIN")
        heure_max_dep = salemodel.get_min_max_heures_dep(order="MAX")

        # Vérifie que les valeurs sont valides
        if not all([heure_min_vente, heure_max_vente, heure_min_dep, heure_max_dep]):
            self.add_widget(Label(text="Aucune donnée disponible pour cette période."))
            return

        heure_min = f"{min(heure_min_vente, heure_min_dep):02d}:00:00"
        heure_max = f"{max(heure_max_vente, heure_max_dep):02d}:00:00"

        ventes = salemodel.get_heures_somme_stat(heure_min=heure_min, heure_max=heure_max)
        depense = salemodel.get_heures_depense_stat(heure_min=heure_min, heure_max=heure_max)

        if not ventes or not depense:
            self.add_widget(Label(text="Aucune donnée à afficher."))
            return

        dates_ventes = [row[0] for row in ventes]
        montants = [row[1] for row in ventes]
        depense_vals = [row[1] for row in depense]
        for i in range(20):
            for i in dates_ventes:
                print(i)

        min_len = min(len(dates_ventes), len(montants), len(depense_vals))
        if min_len == 0:
            self.add_widget(Label(text="Pas de données suffisantes pour générer le graphique."))
            return

        dates = dates_ventes[:min_len]
        montants = montants[:min_len]
        depense_vals = depense_vals[:min_len]

        fig, ax = plt.subplots(figsize=(10, 6))
        x = np.arange(min_len)
        bar_width = 0.35

        ax.bar(x - bar_width / 2, montants, width=bar_width, label='Vente', color='turquoise')
        ax.bar(x + bar_width / 2, depense_vals, width=bar_width, label='Dépense', color='mediumpurple')

        ax.set_title("Ventes vs Dépenses")
        ax.set_xlabel("Heure")
        ax.set_ylabel("Montant (Ar)")
        ax.set_xticks(x)
        ax.set_xticklabels([str(d) for d in dates], rotation=45)
        ax.legend()
        ax.grid(axis='y', linestyle="--", alpha=0.7)
        fig.tight_layout()

        self.add_widget(FigureCanvasKivyAgg(fig))
        """salemodel = GestionModel()
        rows = salemodel.get_heures_somme_stat()

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

        # Forcer l'affichage de 00:00 à 23:00
        if heures_groupees:
            jour = heures_groupees[0].date()
        else:
            jour = datetime.today().date()

        debut_journee = datetime.combine(jour, datetime.min.time())
        fin_journee = datetime.combine(jour, datetime.max.time()).replace(hour=23, minute=59, second=59)

        ax.set_xlim(debut_journee, fin_journee)

        # Ticks majeurs toutes les heures
        ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

        # Formatage et esthétique
        fig.autofmt_xdate()
        ax.grid(True, linestyle='--', alpha=0.4)
        fig.patch.set_facecolor("#f7f7f7")
        ax.set_facecolor('#f0f0f0')
        ax.set_ylabel("Prix ($)", fontsize=12)
        ax.set_xlabel("Heure", fontsize=12)
        plt.xticks(rotation=45)
        fig.tight_layout()

        self.add_widget(FigureCanvasKivyAgg(fig))
"""
    """def show_stat_du_jour(self):
        self.clear_widgets()

        salemodel = GestionModel()
        rows = salemodel.get_heures_stat

        heures = [datetime.strptime(str(row[0]),'%Y-%m-%d %H:%M:%S') for row in rows]
        montants = [row[1] for row in rows]
        donnees_par_heure = defaultdict(float)
        for heure,montant in zip(heures,montants):
                heure_arrondie=heure.replace(minute=0,second=0,microsecond=0)
                donnees_par_heure[heure_arrondie] +=montant
        heures_groupees = sorted(donnees_par_heure.keys())
        montant_groupes = [donnees_par_heure[h] for h in heures_groupees]

        couleurs_palette = ['#1abc9c','#16a085']
        couleurs_alternees = [couleurs_palette[i %len(couleurs_palette)] for i in range(len(heures_groupees))]


        fig, ax = plt.subplots(figsize=(10,5))
        bars = ax.bar(heures_groupees, montant_groupes, width=0.035, color=couleurs_alternees,edgecolor='black',linewidth=0.5)

        for bar,montant in zip(bars,montant_groupes):
            height=bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2.0, height +0.5 , f"{montant:.0f}", ha='center',va='bottom',fontsize=9,color="#333")



        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
        fig.autofmt_xdate()
        ax.grid(True,linestyle='--',alpha=0.4)
        fig.patch.set_facecolor("#f7f7f7")
        ax.set_facecolor('#f0f0f0')
        #ax.set_title("Shopify Inc", fontsize=16)
        ax.set_ylabel("Prix ($)", fontsize=12)
        ax.set_xlabel("Date", fontsize=12)
        plt.xticks(rotation=45)
        fig.tight_layout()


        self.add_widget(FigureCanvasKivyAgg(fig))"""


class PourcentagePV(RelativeLayout):
    from utilities.myfunctions import pourcentage
    widget_showed = False

    def __init__(self, **kwargs):
        super(PourcentagePV, self).__init__(**kwargs)

    def show_pourcentage_pv(self,date=None,date_fin=None,order=""):
        print("ids disponibles dans PourcentagePVG:", self.ids.keys())
        self.pourcentage('pv', date, date_fin, order=order)

class SalesPage(MDBoxLayout):
    total_de_ventes = StringProperty('0')
    somme_total_gagnee = StringProperty('0 ar')
    produits_en_rupture = StringProperty('0')
    gestionmodel = GestionModel()

    def __init__(self,**kwargs):
        super(SalesPage,self).__init__(**kwargs)
        self.update_total_de_ventes()
        self.update_somme_total_gagnee()
        self.update_produits_en_rupture()

    def update_total_de_ventes(self):
        total_de_ventes = self.gestionmodel.get_total_de_ventes()
        self.total_de_ventes = str(total_de_ventes)
    def update_somme_total_gagnee(self):
        somme_total_gagnee = self.gestionmodel.get_somme_total_gagnee()
        self.somme_total_gagnee = str(somme_total_gagnee)+' ar'
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

class ListeVente(ScrollView):
    grid_showed = False
    grid = None
    def __init__(self, **kwargs):
        super(ListeVente, self).__init__(**kwargs)

    def show_products_sale(self):
        if self.grid_showed:
            self.remove_widget(self.grid)
            self.grid = None
        self.grid = MDGridLayout(cols=4, spacing=2, size_hint_y=None,)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        instance = GestionModel()
        produits = instance.get_produits_vendus
        # print(produits)
        titles = ('ID', 'PRODUIT', 'DATE', 'QT')
        for i in enumerate(titles):
            cell = Label(text=i[1], color=(0, 0, 0, 1), bold=True, size_hint=(1, None), height=25)
            if i[0]==0 or i[0]==1 :
                cell.size_hint_x=0.5
            elif i[0]==3:
                cell.size_hint_x = 0.2
            self.grid.add_widget(cell)
        for row in produits:
            for item in range(len(row)):
                cell = Label(text=f'{row[item]}', color=(.2, .2, .2, 1), size_hint=(1, None), height=25)
                if item==0 or item==1:
                    cell.size_hint_x=0.5
                elif item==3:
                    cell.size_hint_x = 0.2
                self.grid.add_widget(cell)
        self.add_widget(self.grid)
        self.grid_showed = True

import os

kv_path = os.path.join(os.path.dirname(__file__), '..', 'view', 'sales_page.kv')
Builder.load_file(kv_path)
