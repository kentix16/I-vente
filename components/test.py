from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.boxlayout import MDBoxLayout

KV = '''
<Houi@MDScreen>:
    name: "screen1"
    MDBoxLayout:
        orientation: "vertical"
        adaptive_height: True
    
        MDSliverAppbar:
            background_color: 0.176, 0.290, 0.313, 1
            hide_appbar: True
            size_hint_y: None
            height: dp(50)
    
            MDTopAppBar:
                type: "medium"
                size_hint_y: None
                height: dp(50)
    
                MDTopAppBarLeadingButtonContainer:
                    MDActionTopAppBarButton:
                        icon: "package"
    
                MDTopAppBarTitle:
                    text: "Écran 1"
    
                MDTopAppBarTrailingButtonContainer:
                    MDActionTopAppBarButton:
                        icon: "attachment"
                    MDActionTopAppBarButton:
                        icon: "calendar"
                    MDActionTopAppBarButton:
                        icon: "dots-vertical"
    
            MDSliverAppbarHeader:
                FitImage:
                    source: "images/playabg.jpg"
                    size_hint_y: None
                    height: dp(180)
    
            Content:
<CustomItem>:
    text: ""
    orientation: "vertical"
    padding: "8dp"
    spacing: "4dp"
    adaptive_height:True
    MDLabel:
        size_hint_y: None
        height: dp(18)
        text: root.text
        theme_text_color: "Primary"
    MDLabel:
        size_hint_y: None
        height: dp(18)
        text: "Ligne A"
    MDLabel:
        size_hint_y: None
        height: dp(18)
        text: "Ligne B"

<Heyhey@MDScrollView>:
    MDRecycleView:
        id: recycle
        viewclass: "CustomItem"
        RecycleBoxLayout:
            default_size: None, dp(220)
            default_size_hint: 1, None
            size_hint_y: None
            height: self.minimum_height
            orientation: 'vertical'

<Content@MDBoxLayout>:
    orientation: "vertical"
    adaptive_height: True
    spacing: "12dp"
    padding: "12dp"
    MDTextField:
        hint_text: "Champ 1"
    MDTextField:
        hint_text: "Champ 2"

MDScreen:
    MDScrollView:
        MDBoxLayout:
            orientation: 'vertical'
            adaptive_height: True
            spacing: "24dp"
            padding: "12dp"

            # 1. Boutons
            MDBoxLayout:
                adaptive_height: True
                spacing: "12dp"
                MDButton:
                    text: "Écran 1"
                    on_release: screen_manager.current = "screen1"
                MDButton:
                    text: "Écran 2"
                    on_release: screen_manager.current = "screen2"

            # 2. ScreenManager avec Sliver
            MDScreenManager:
                id: screen_manager
                size_hint_y: None
                height: dp(550)

                
                Houi:
                
                MDScreen:
                    name: "screen2"
                    MDBoxLayout:
                        orientation: "vertical"
                        adaptive_height: True

                        MDSliverAppbar:
                            background_color: 0.176, 0.290, 0.313, 1
                            hide_appbar: True
                            size_hint_y: None
                            height: dp(50)

                            MDTopAppBar:
                                type: "medium"
                                size_hint_y: None
                                height: dp(50)

                                MDTopAppBarLeadingButtonContainer:
                                    MDActionTopAppBarButton:
                                        icon: "shopping"

                                MDTopAppBarTitle:
                                    text: "Écran 2"

                                MDTopAppBarTrailingButtonContainer:
                                    MDActionTopAppBarButton:
                                        icon: "cloud"
                                    MDActionTopAppBarButton:
                                        icon: "calendar"
                                    MDActionTopAppBarButton:
                                        icon: "dots-vertical"

                            MDSliverAppbarHeader:
                                FitImage:
                                    source: "images/playabg.jpg"
                                    size_hint_y: None
                                    height: dp(180)

                            Content:

            # 3. RecycleView avec scroll dans chaque CustomItem
            MDLabel:
                text: "Liste des éléments (chaque élément a un scroll)"
                halign: "center"
                size_hint_y: None
                height: self.texture_size[1]
            MDCard:
                size_hint_x:1
                size_hint_y:None
                height:dp(500)
                style: "elevated"
                elevation:10
                radius:[20]
                Heyhey:
                    size_hint_y: None
                    height: dp(450)
                    id: heyhey
'''

class CustomItem(MDBoxLayout):
    nom_produit=StringProperty()
    Ordinateur=StringProperty()
    portable=StringProperty()
    prix_unitaire=StringProperty()
    type_produit=StringProperty()

class TestApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        self.root.ids.heyhey.ids.recycle.data = [
            {"text": f"Produit {i} (scrollable)"} for i in range(1, 6)
        ]

TestApp().run()
