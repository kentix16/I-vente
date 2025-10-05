from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, FadeTransition, SlideTransition
from openpyxl.styles.colors import WHITE


class NavigationScreenManager(ScreenManager):
    screen_stack = []

    def set_active_item(self, i):
        app = App.get_running_app()

        # Screens à parcourir
        screens = [
            app.manager.ids.mainscreen,
            app.manager.ids.productsscreen,
            app.manager.ids.walletscreen,
            app.manager.ids.expensesscreen,
            app.manager.ids.statsscreen,
        ]

        for screen in screens:
            drawer = screen.ids.nav_drawer

            for j in range(6):  # tes items item1..item9
                item = drawer.ids.get(f"item{j + 1}")
                icon = drawer.ids.get(f"icon{j + 1}")
                text = drawer.ids.get(f"text{j + 1}")
                icon.theme_icon_color = "Custom"
                text.theme_text_color = "Custom"
                text.text_color = (1, 1, 1, 1)
                icon.icon_color = (1, 1, 1, 1)
                #icon.text_color = WHITE
                #text.text_color = WHITE
                icon.text_color_disabled = WHITE
                text.text_color_disabled = WHITE
                #text.selected_color = WHITE
                #icon.selected_color = WHITE
                if not item:
                    continue

                if j == i:
                    # ✅ Item actif
                    item.md_bg_color = app.drawer_color
                    item.selected_color = app.drawer_color
                    item.theme_bg_color = "Custom"
                    item.selected = True
                    item.icon_color=(1,1,1,1)
                    item.text_color=(1,1,1,1)

                else:
                    # ✅ Items inactifs
                    item.md_bg_color = (0, 0, 0, 0)
                    item.selected = False

                    # garder textes/icônes en blanc aussi
                    for child in item.children:
                        if hasattr(child, "theme_text_color"):
                            child.theme_text_color = "Custom"
                            child.text_color = (1, 1, 1, 1)

    def go(self,screen_name,i=0):
        self.set_active_item(i)
        App.get_running_app().manager.ids.mainscreen.ids.nav_drawer.ids.get(f"item{i + 1}").disabled = True
        App.get_running_app().manager.ids.productsscreen.ids.nav_drawer.ids.get(f"item{i + 1}").disabled = True
        App.get_running_app().manager.ids.walletscreen.ids.nav_drawer.ids.get(f"item{i + 1}").disabled = True
        App.get_running_app().manager.ids.expensesscreen.ids.nav_drawer.ids.get(f"item{i + 1}").disabled = True
        App.get_running_app().manager.ids.statsscreen.ids.nav_drawer.ids.get(f"item{i + 1}").disabled = True
        for j in range(6):
            if j != i:
                App.get_running_app().manager.ids.mainscreen.ids.nav_drawer.ids.get(f"item{j + 1}").disabled = False
                App.get_running_app().manager.ids.productsscreen.ids.nav_drawer.ids.get(f"item{j + 1}").disabled = False
                App.get_running_app().manager.ids.walletscreen.ids.nav_drawer.ids.get(f"item{j + 1}").disabled = False
                App.get_running_app().manager.ids.expensesscreen.ids.nav_drawer.ids.get(f"item{j + 1}").disabled = False
                App.get_running_app().manager.ids.statsscreen.ids.nav_drawer.ids.get(f"item{j + 1}").disabled = False

        self.current = screen_name
    def push(self,screen_name,i=0):
        if screen_name not in self.screen_stack:
            self.screen_stack.append(self.current)
            self.transition = FadeTransition() if not self.screen_stack else SlideTransition(direction="left")
            self.current=screen_name

    def pop(self):
        if len(self.screen_stack):
            screen_name=self.screen_stack[-1]
            self.transition.direction="right"
            del self.screen_stack[-1]
            self.current=screen_name
    def toggle(self):
        App.get_running_app().manager.ids.mainscreen.ids.nav_drawer.set_state("toggle")
        App.get_running_app().manager.ids.productsscreen.ids.nav_drawer.set_state("toggle")
        App.get_running_app().manager.ids.walletscreen.ids.nav_drawer.set_state("toggle")
        App.get_running_app().manager.ids.expensesscreen.ids.nav_drawer.set_state("toggle")
        App.get_running_app().manager.ids.statsscreen.ids.nav_drawer.set_state("toggle")
    def close(self):
        App.get_running_app().manager.ids.mainscreen.ids.nav_drawer.set_state('close')
        App.get_running_app().manager.ids.productsscreen.ids.nav_drawer.set_state('close')
        App.get_running_app().manager.ids.walletscreen.ids.nav_drawer.set_state('close')
        App.get_running_app().manager.ids.expensesscreen.ids.nav_drawer.set_state('close')
        App.get_running_app().manager.ids.statsscreen.ids.nav_drawer.set_state('close')





