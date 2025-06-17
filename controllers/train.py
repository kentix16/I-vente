import tkinter as tk
from tkinter import filedialog

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class MonLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.label = Label(text="Aucun fichier sélectionné")
        self.add_widget(self.label)

        bouton = Button(text="Ouvrir le gestionnaire de fichiers")
        bouton.bind(on_press=self.ouvrir_fichier)
        self.add_widget(bouton)

    def ouvrir_fichier(self, instance):
        # Lancer tkinter de manière cachée juste pour le file dialog
        root = tk.Tk()
        root.withdraw()  # Cacher la fenêtre principale de Tkinter

        fichier = filedialog.askopenfilename(title="Choisissez un fichier")
        if fichier:
            self.label.text = f"Fichier sélectionné :\n{fichier}"
        root.destroy()  # Fermer le root tkinter après sélection


class MonApp(App):
    def build(self):
        return MonLayout()


if __name__ == '__main__':
    MonApp().run()
