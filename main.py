from font.fonts import register_fonts
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from navigation_screen_manager import NavigationScreenManager

class MyScreenManager(NavigationScreenManager):
    def __init__(self,**kwargs):
        super(MyScreenManager,self).__init__(**kwargs)
    def update_all(self):
        self.ids.mainscreen.ids.salespage.ids.listevente.show_products_sale()
        self.ids.mainscreen.ids.salespage.update_total_de_ventes()
        self.ids.mainscreen.ids.salespage.update_somme_total_gagnee()
        self.ids.mainscreen.ids.salespage.update_produits_en_rupture()
        self.ids.mainscreen.ids.salespage.ids.pourcentagepv.show_pourcentage_pv()
        self.ids.mainscreen.ids.salespage.ids.statedevente.show_stat_du_jour()
        self.ids.expensesscreen.ids.expensespage.ids.labelsommeportefeuille.update_somme_portefeuille()
        self.ids.expensesscreen.ids.expensespage.ids.listedepense.update_expenses()
        self.ids.walletscreen.ids.walletpage.ids.historique.update_historique()
        self.ids.walletscreen.ids.walletpage.ids.labelsommeportefeuille2.update_somme_portefeuille()

class CompanyManager(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.theme_style = "Light"
        register_fonts(self.theme_cls)  # ⬅️ enregistrement ici

    manager = ObjectProperty(None)
    def build(self):
        self.manager = MyScreenManager()
        return self.manager


if __name__ == "__main__":
    CompanyManager().run()