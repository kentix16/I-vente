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
    for i in range(50):print("window size",window.height,window.width)
    manager = App.get_running_app().manager
    if width < 750:
        if width < 500:
            state = "open"
        else:
            state = "open"
        cols = 1
        orientation = "vertical"
        size_hint = 1
        font_style = "Title"
        scroll = True
        size_hint_1=1
        screen_size=550
        opacity=0

        color=0,0,0,0
        poshint={"center_x":.5}
    elif 750 <= width <= 850:
        orientation = "vertical"
        size_hint = 1
        font_style = "Headline"
        scroll = True
        cols = 1
        size_hint_1 = 1
        screen_size=550
        opacity = 1
        state = "close"
        color = 1, 1, 1, 1
        poshint = {"center_x": .5}

        if manager.ids.mainscreen.ids.salespage.orientation=='vertical':return

    else:
        poshint = {"center_x": .5}
        color = 1, 1, 1, 1
        state = "close"
        opacity = 1
        size_hint_1 = .6
        if manager.ids.mainscreen.ids.salespage.orientation=='horizontal':return
        screen_size=1100
        orientation="horizontal"
        size_hint = .4
        font_style = "Headline"
        scroll = False
        cols = 3
    manager = App.get_running_app().manager
    layouts = [manager.ids.mainscreen.ids.salespage,
               manager.ids.productsscreen.ids.productspage.ids.defaultscreen.ids.product_page_1,
               manager.ids.productsscreen.ids.productspage.ids.productlist.ids.product_page_2,
               manager.ids.walletscreen.ids.walletpage,
               manager.ids.expensesscreen.ids.expensespage,
               manager.ids.statsscreen.ids.statsspage]
    sections=[manager.ids.mainscreen.ids.salespage.ids.sale_section_2,
               manager.ids.productsscreen.ids.productspage.ids.defaultscreen.ids.product_page_1_section_2,
               manager.ids.productsscreen.ids.productspage.ids.productlist.ids.product_page_2_section_2,
               manager.ids.walletscreen.ids.walletpage.ids.wallet_section_2,
               manager.ids.expensesscreen.ids.expensespage.ids.expense_section_2,
               manager.ids.statsscreen.ids.statsspage.ids.stat_section_2]
    scroll_views=[manager.ids.mainscreen.ids.scroll_1,manager.ids.productsscreen.ids.scroll_2,manager.ids.productsscreen.ids.scroll_2,
                  manager.ids.walletscreen.ids.scroll_3,
                  manager.ids.expensesscreen.ids.scroll_4,manager.ids.statsscreen.ids.scroll_5]
    for i in range(len(layouts)):
        layouts[i].orientation = orientation
        sections[i].size_hint_x = size_hint
        if scroll:
            scroll_views[i].do_scroll_y = True
            layouts[i].size_hint_y = None
            layouts[i].height = layouts[i].minimum_height
    manager.ids.user_creation_screen.ids.bg_mobile.set_state(state)
    manager.ids.user_creation_screen.ids.image_desk.opacity=opacity
    manager.ids.user_creation_screen.ids.acc.opacity=opacity
    manager.ids.user_creation_screen.ids.text.opacity=1-opacity


    manager.ids.productsscreen.ids.productspage.ids.defaultscreen.ids.sliver_box.size_hint_x=size_hint_1
    manager.ids.mainscreen.ids.salespage.ids.sale_number.cols = cols
    manager.ids.productsscreen.ids.productspage.ids.productlist.ids.stock_card.size_hint_x = size_hint
    manager.ids.mainscreen.ids.salespage.ids.sale_label1.font_style = font_style
    manager.ids.mainscreen.ids.salespage.ids.sale_label2.font_style = font_style





class CompanyManager(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.theme_style = "Light"
        register_fonts(self.theme_cls)  # ⬅️ enregistrement ici
        Window.bind(on_resize=on_window_resize)


    manager = ObjectProperty(None)
    def build(self):
        self.manager = MyScreenManager()
        return self.manager

    def on_start(self):
        on_window_resize(Window, Window.width, Window.height)

if __name__ == "__main__":
    CompanyManager().run()