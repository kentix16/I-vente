import gc

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window

from kivy.utils import get_color_from_hex

from font.fonts import register_fonts
from kivy.properties import ObjectProperty, ColorProperty
from kivymd.app import MDApp
from navigation_screen_manager import NavigationScreenManager
import controllers.sales_page  # ou sales_pages si c’est le bon nom


adresse_recherchee = '0x000002158F8E9BE0'
class Damn(NavigationScreenManager):
    pass

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
    manager = App.get_running_app().manager

    for i in range(50):
        print("window size",window.height,window.width)
        try:
            print("🎯 test accès :", manager.ids.mainscreen.ids.salespage.orientation)
        except Exception as e:
            print("❌ erreur d’accès à salespage:", e)



    if width < 750:
        if width < 350:
            state = "open"
            opacity = 0
        else:
            state = "open"
            opacity = 0
        cols = 1
        orientation = "vertical"
        size_hint = 1
        font_style = "Title"
        scroll = True
        size_hint_1=1
        screen_size=550


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
    primary_color = ColorProperty()
    accent_color = ColorProperty()
    bg_normal = ColorProperty()
    bg_dark = ColorProperty()
    text_color = ColorProperty()
    opposite_bg_normal = ColorProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.theme_style = "Light"
        register_fonts(self.theme_cls)
        self.theme_cls.primary_palette = "Darkslateblue"
        Window.bind(on_resize=on_window_resize)

        # Définir les couleurs initiales en mode clair
        self.set_light_theme_colors()

    def set_light_theme_colors(self):
        self.primary_color = get_color_from_hex("#245478")
        self.accent_color = get_color_from_hex("#f48935")
        self.bg_normal = get_color_from_hex("#ffffff")
        self.bg_dark = get_color_from_hex("#132e49")
        self.text_color = get_color_from_hex("#000000")
        self.opposite_bg_normal = get_color_from_hex("#fcbe8d")

    def wait_for_layout(self, dt):
        try:
            # test si le layout cible est disponible
            _ = self.manager.ids.mainscreen.ids.salespage
            print("✅ Layout disponible !")
            on_window_resize(Window, Window.width, Window.height)
        except Exception as e:
            print("🕒 Layout non prêt, on attend…")
            Clock.schedule_once(self.wait_for_layout, 0.2)

    def set_dark_theme_colors(self):
        self.primary_color = get_color_from_hex("#132e49")
        self.accent_color = get_color_from_hex("#f48935")
        self.bg_normal = get_color_from_hex("#132e49")
        self.bg_dark = get_color_from_hex("#1a1a1a")
        self.text_color = get_color_from_hex("#fcbe8d")
        self.opposite_bg_normal = get_color_from_hex("#245478")

    def damn(self, value=False):
        if value:
            self.theme_cls.theme_style = "Dark"
            self.set_dark_theme_colors()
        else:
            self.theme_cls.theme_style = "Light"
            self.set_light_theme_colors()

    def on_switch_active(self, instance_switch, value):
        self.damn(value)

    """def on_start(self):
        on_window_resize(Window, Window.width, Window.height)"""

    def on_start(self):
        # ⏳ attendre que l'UI soit prête
        Clock.schedule_once(self.assign_manager_and_resize, 0.1)
        Clock.schedule_once(self.wait_for_layout, 0.2)
    def assign_manager_and_resize(self, dt):
        try:
            self.manager = self.first.ids.nav_screen_manager_2  # ✅ maintenant accessible
            on_window_resize(Window, Window.width, Window.height)


        except Exception as e:
            print("[ERROR] assign_manager_and_resize:", e)
        for i in range(20):
            print("self.first:", self.first)
            print("self.first.ids:", self.first.ids)
            print("self.first.ids.mainscreen:", self.first.ids.get('mainscreen'))

    manager = ObjectProperty(None)
    def build(self):
        self.first = Damn()  # Root contenant appbar, nav, etc.
        return self.first


if __name__ == "__main__":
    CompanyManager().run()