from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy_garden.matplotlib import FigureCanvasKivyAgg
from matplotlib import pyplot as plt

from models.gestionModel import GestionModel

def pourcentage(self,nom_pourcentage,date=None,date_fin=None,):
    if self.widget_showed: self.clear_widgets()
    labels = []
    sizes = []
    instance = GestionModel()
    if nom_pourcentage=='pv':
        produits = instance.get_pourcentage_produits_vendus(date, date_fin)
    if nom_pourcentage=='dep':
        produits = instance.get_pourcentage_depense(date,date_fin)
    if not produits: return None

    for row in produits:
        labels.append(row[0])
        sizes.append(row[1])

    fig, ax = plt.subplots()

    if len(labels) <= 10:
        # Camembert
        explode = [0.1] + [0] * (len(labels) - 1)  # Explose seulement la première part
        ax.pie(sizes, labels=labels, textprops={'fontsize': 9},
               autopct='%1.1f%%', shadow=True, startangle=140, explode=explode)
        self.add_widget(FigureCanvasKivyAgg(fig))
    else:
        scroll = ScrollView(size_hint=(1, 1))
        grid = GridLayout(cols=2, spacing=4, size_hint_y=None, padding=4)
        grid.bind(minimum_height=grid.setter('height'))
        titles = ("PODUITS", "%")
        for i in titles:
            lbl = Label(text=f'{i}', size_hint_y=20, bold=True, color=[0, 0, 0, 1])
            grid.add_widget(lbl)
        for row in produits:
            for i in row:
                lbl = Label(text=f'{i}', size_hint_y=None, height=20, color=[0, 0, 0, 1])
                grid.add_widget(lbl)
        scroll.add_widget(grid)
        self.add_widget(scroll)

    self.widget_showed = True