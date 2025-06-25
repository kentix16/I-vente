from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.image import Image
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen


class UserCreationScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def on_kv_post(self, base_widget):
        self.add_widget(MDLabel(text="Maîtrisez votre business.",font_style="RobotoBold",pos_hint= {"center_x": 0.7, "center_y": 0.85},theme_text_color="Custom",text_color=(1,1,1,1)))


class Background(MDFloatLayout):
    pass

class DefaultLabel(MDLabel):
    def __init__(self, **kwargs):
        kwargs.setdefault("font_style", "OutfitMedium")
        kwargs.setdefault("role", "medium")
        super().__init__(**kwargs)
class Meme(MDCard):
    pass



import os

kv_path = os.path.join(os.path.dirname(__file__), '..', 'view', 'user_creation.kv')
Builder.load_file(kv_path)

Bg=Background()
