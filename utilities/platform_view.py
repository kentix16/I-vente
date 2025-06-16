from kivy.app import App
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout


def mobileview(window,width,height):
    orientate="vertical" if width <= 600 and height <= 948 else "horizontal"
    manager=App.get_running_app().manager
    layouts=[manager.ids.mainscreen.ids.salespage,
    manager.ids.productsscreen.ids.productspage,
    manager.ids.walletscreen.ids.walletpage,
    manager.ids.expensesscreen.ids.expensespage,
    manager.ids.statsscreen.ids.statsspage]
    for layout in layouts:
        layout.orientation=orientate
        manager.ids.statsscreen.ids.statsspage.id.sales_card_un.size_hint_x=1
        manager.ids.statsscreen.ids.statsspage.id.sales_card_deux.size_hint_x=1
        manager.ids.statsscreen.ids.statsspage.id.sales_card_un.do_layout()
        manager.ids.statsscreen.ids.statsspage.id.sales_card_deux.do_layout()



        layout.do_layout()
        print(orientate)
    Window.bind(on_resize=mobileview)



