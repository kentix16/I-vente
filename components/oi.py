from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
MDScreen:

    MDTopAppBar:
        title: "Palette CSS test"
        pos_hint: {"top": 1}
        elevation: 4

    MDLabel:
        text: "Bonjour !"
        halign: "center"
        pos_hint: {"center_y": 0.6}
        theme_text_color: "Primary"

    MDButton:
        text: "Clic"
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        md_bg_color: "#f48935"  # ton orange
        text_color: "white"
'''

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"  # ou "Dark"
        self.theme_cls.primary_palette = "Darkslateblue"  # compatible CSS name
        return Builder.load_string(KV)

MyApp().run()
