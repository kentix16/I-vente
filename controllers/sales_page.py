from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.graphics import Mesh, Color, Rectangle
from kivy.properties import ListProperty, StringProperty, NumericProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
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
        ax.plot(heures, somme, color='green', linewidth=2)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
        fig.autofmt_xdate()
        self.stat_showed = True

        ax.set_title("Shopify Inc", fontsize=16)
        ax.set_ylabel("Prix ($)", fontsize=12)
        ax.set_xlabel("Date", fontsize=12)
        ax.grid(True)

        # Rotation des dates
        plt.xticks(rotation=45)

        # Afficher le graphique
        fig.tight_layout()
        self.add_widget(FigureCanvasKivyAgg(fig))


class PourcentagePV(RelativeLayout):
    widget_showed = False

    def __init__(self, **kwargs):
        super(PourcentagePV, self).__init__(**kwargs)

    def show_pourcentage_pv(self):
        if self.widget_showed:self.clear_widgets()
        labels= []
        sizes=[]
        instance = GestionModel()
        produits = instance.get_pourcentage_produits_vendus
        for row in produits:
            labels.append(row[0])
            sizes.append(row[1])

        explode = (0.1, 0, 0, 0)  # mettre en avant la première part

        # Création de la figure
        fig, ax = plt.subplots()
        ax.pie(sizes,labels=labels, textprops={'fontsize':9},
               autopct='%1.1f%%', shadow=True, startangle=140)
        # Ajout du canvas dans l'interface Kivy
        self.add_widget(FigureCanvasKivyAgg(fig))
        self.widget_showed = True
        

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
        total_de_ventes = self.gestionmodel.get_total_de_ventes
        self.total_de_ventes = str(total_de_ventes)
    def update_somme_total_gagnee(self):
        somme_total_gagnee = self.gestionmodel.get_somme_total_gagnee
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
        self.grid = GridLayout(cols=4, spacing=2, size_hint_y=None)
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
