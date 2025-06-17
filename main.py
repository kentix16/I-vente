import gc

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from utilities.platform_view import mobileview
from font.fonts import register_fonts
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from navigation_screen_manager import NavigationScreenManager
import controllers.sales_page  # ou sales_pages si c’est le bon nom


adresse_recherchee = '0x000002158F8E9BE0'


class MyScreenManager(NavigationScreenManager):
    def __init__(self,**kwargs):
        super(MyScreenManager,self).__init__(**kwargs)

    def update_all(self):
        self.ids.mainscreen.ids.salespage.ids.listevente.show_products_sale()
        self.ids.mainscreen.ids.salespage.update_total_de_ventes()
        self.ids.mainscreen.ids.salespage.update_somme_total_gagnee()
        self.ids.mainscreen.ids.salespage.ids.statedevente.show_stat_du_jour()
        self.ids.mainscreen.ids.salespage.update_produits_en_rupture()
        self.ids.mainscreen.ids.salespage.ids.pourcentagepv.show_pourcentage_pv()
        self.ids.mainscreen.ids.salespage.ids.statedevente.show_stat_du_jour()
        self.ids.expensesscreen.ids.expensespage.ids.labelsommeportefeuille.update_somme_portefeuille()
        self.ids.expensesscreen.ids.expensespage.ids.listedepense.update_expenses()
        self.ids.walletscreen.ids.walletpage.ids.historique.update_historique()
        self.ids.walletscreen.ids.walletpage.ids.labelsommeportefeuille2.update_somme_portefeuille()


def on_window_resize(window, width, height):
    for i in range(50):print("window resize")
    manager = App.get_running_app().manager
    if width <= 700 and height <= 833:

        if manager.ids.mainscreen.ids.salespage.orientation=='vertical':return
        orientation = "vertical"

    else:
        if manager.ids.mainscreen.ids.salespage.orientation=='horizontal':return
        orientation="horizontal"
    manager = App.get_running_app().manager
    layouts = [manager.ids.mainscreen.ids.salespage,
               manager.ids.productsscreen.ids.productspage,
               manager.ids.walletscreen.ids.walletpage,
               manager.ids.expensesscreen.ids.expensespage,
               manager.ids.statsscreen.ids.statsspage]

    for layout in layouts:
        layout.orientation = orientation
        """manager.ids.statsscreen.ids.statsspage.ids.sales_card_un.size_hint_x = 1
        manager.ids.statsscreen.ids.statsspage.ids.sales_card_deux.size_hint_x = 1
        manager.ids.statsscreen.ids.statsspage.ids.sales_card_un.do_layout()
        manager.ids.statsscreen.ids.statsspage.ids.sales_card_deux.do_layout()"""




class CompanyManager(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.theme_style = "Light"
        register_fonts(self.theme_cls)  # ⬅️ enregistrement ici
        Window.bind(on_resize=on_window_resize)
        print("ken")


    manager = ObjectProperty(None)
    def build(self):
        self.manager = MyScreenManager()
        return self.manager


if __name__ == "__main__":
    CompanyManager().run()