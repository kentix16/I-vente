from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy_garden.matplotlib import FigureCanvasKivyAgg
from matplotlib import pyplot as plt

from models.gestionModel import GestionModel

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
            App.get_running_app().manager.ids.statsscreen.ids.statsspage.ids.salescontainer.ids.pourcentagepvg.ids.pv.data = data
            App.get_running_app().manager.ids.statsscreen.ids.statsspage.ids.salescontainer.ids.pourcentagepvg.clear_widgets()
            App.get_running_app().manager.ids.statsscreen.ids.statsspage.ids.salescontainer.ids.pourcentagepvg.add_widget(App.get_running_app().manager.ids.statsscreen.ids.statsspage.ids.salescontainer.ids.pourcentagepvg.ids.pv)


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



