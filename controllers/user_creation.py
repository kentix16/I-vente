from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.image import Image
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen


class UserCreationScreen(MDScreen):
    pass


class Background(MDFloatLayout):
    pass

class DefaultLabel(MDLabel):
    def __init__(self, **kwargs):
        kwargs.setdefault("font_style", "OutfitMedium")
        kwargs.setdefault("role", "medium")
        super().__init__(**kwargs)
class Meme(MDBoxLayout):
    pass



import os

kv_path = os.path.join(os.path.dirname(__file__), '..', 'view', 'user_creation.kv')
Builder.load_file(kv_path)

Bg=Background()
