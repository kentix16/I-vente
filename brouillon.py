"""from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

import matplotlib.pyplot as plt

from kivy_garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg


class PieChart(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Données pour le camembert
        labels = ['Pommes', 'Bananes', 'Cerises', 'Raisins']
        sizes = [30, 25, 20, 25]
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
        explode = (0.1, 0, 0, 0)  # mettre en avant la première part

        # Création de la figure
        fig, ax = plt.subplots()
        ax.pie(sizes, explode=explode, labels=labels, colors=colors,
               autopct='%1.1f%%', shadow=True, startangle=140)
        ax.set_title("Répartition des Fruits")

        # Ajout du canvas dans l'interface Kivy
        self.add_widget(FigureCanvasKivyAgg(fig))


class PieChartApp(App):
    def build(self):
        return PieChart()


if __name__ == '__main__':
    PieChartApp().run()
"""
booleen = False
print(not not not not not booleen)