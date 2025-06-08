from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy_garden.matplotlib import FigureCanvasKivyAgg
from matplotlib import pyplot as plt

from models.gestionModel import GestionModel

def pourcentage(self,nom_pourcentage,date=None,date_fin=None,widgetcontainer=None,order=""):
    if self.widget_showed: self.clear_widgets()
    labels = []
    sizes = []
    instance = GestionModel()
    if nom_pourcentage=='pv':
        produits = instance.get_pourcentage_produits_vendus(date, date_fin,order)
        print("Résultat produits:", produits)
        if widgetcontainer:
            print("l'ordre est!",order)
            print("Résultat date:", date)
            print("Résultat date_fin:", date_fin)

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
        if widgetcontainer:

            data = []

            for row in produits:
                data.append({
                    'product_name': str(row[0]),
                    'sale_percent': str(row[1])
                })
            # App.manager.statsscreen.statsspage.percentstat
            widgetcontainer.data = data
            self.add_widget(widgetcontainer)
        else:
            print("widget introuvable")

    self.widget_showed=True


