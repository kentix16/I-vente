from kivy.lang import Builder
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.card import MDCard

KV = '''
<StyledForm>:
    orientation: "vertical"
    spacing: "20dp"
    padding: "20dp"

    MDCard:
        orientation: "vertical"
        padding: "25dp"
        size_hint: None, None
        size: "500dp", "440dp"
        elevation: 4
        md_bg_color: [1, 1, 1, 1]

        MDLabel:
            text: "Formulaire Produit"
            font_style: "Headline"
            halign: "center"
            theme_text_color: "Primary"
            size_hint_y: None
            height: self.texture_size[1] + dp(10)

        MDTextField:
            id: name_field
            hint_text: "Nom du produit"
            mode: "outlined"

        BoxLayout:
            id: spinner_box
            orientation: "vertical"
            size_hint_y: None
            height: dp(80)
            spacing: "5dp"

            MDLabel:
                text: "Type de produit"
                theme_text_color: "Secondary"
                font_style: "Headline"
                size_hint_y: None
                height: self.texture_size[1]

        MDTextField:
            id: quantity_field
            hint_text: "Quantité"
            mode: "outlined"
            input_filter: "int"

        Widget:
            size_hint_y: None
            height: dp(200)

StyledForm:
'''


class StyledForm(BoxLayout):
    pass


class SpinnerApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.theme_style = "Light"

        # 🛠️ FIX : on stocke manuellement l’instance dans self.root
        self.root = Builder.load_string(KV)
        return self.root

    def on_start(self):
        product_types = ["Électronique", "Vêtements", "Alimentation", "Livres", "Meubles"]

        spinner = Spinner(
            text="Sélectionner...",
            values=product_types,
            size_hint=(1, None),
            height=dp(40),
            background_normal="",
            background_color=self.theme_cls.primaryColor,
            color=(1, 1, 1, 1),
            font_size="16sp"
        )

        self.root.ids.spinner_box.add_widget(spinner)


SpinnerApp().run()
