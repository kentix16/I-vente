from datetime import datetime
from functools import partial
from tkinter import filedialog
from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogContentContainer, MDDialogButtonContainer
from kivymd.uix.textfield import MDTextField, MDTextFieldHelperText, MDTextFieldHintText, MDTextFieldLeadingIcon, \
    MDTextFieldTrailingIcon, MDTextFieldMaxLengthText
from kivymd.uix.button import MDButton, MDButtonText

import xlsxwriter
import tkinter as tk
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy_garden.matplotlib import FigureCanvasKivyAgg
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButtonText, MDButton, MDIconButton
from kivymd.uix.dialog import MDDialogButtonContainer, MDDialogContentContainer, MDDialogSupportingText, \
    MDDialogHeadlineText, MDDialog
from kivymd.uix.divider import MDDivider
from kivymd.uix.label import MDLabel
from matplotlib import pyplot as plt

from models.gestionModel import GestionModel
from kivy.metrics import dp
from kivymd.uix.pickers import MDDockedDatePicker, MDTimePickerDialVertical, MDTimePickerDialHorizontal, \
    MDModalDatePicker

from utilities.databases import to_database


def pourcentage(self,nom_pourcentage="pv",date=None,date_fin=None,order=""):
    if self.widget_showed: self.clear_widgets()
    labels = []
    sizes = []
    instance = GestionModel()
    if nom_pourcentage=='pv':
        produits = instance.get_pourcentage_produits_vendus(date, date_fin,order)

    if nom_pourcentage=='dep':
        produits = instance.get_pourcentage_depense(date,date_fin)
    if not produits: return None

    for row in produits:
        labels.append(row[0])
        sizes.append(row[1])

    fig, ax = plt.subplots()

    if len(labels) <= 10 and order=="":

        # Camembert
        explode = [0.1] + [0] * (len(labels) - 1)  # Explose seulement la première part
        ax.pie(sizes, labels=labels, textprops={'fontsize': 9},
               autopct='%1.1f%%', shadow=True, startangle=140, explode=explode)
        self.add_widget(FigureCanvasKivyAgg(fig))

    else:
        if nom_pourcentage == 'pv':
            data = []

            for row in produits:
                data.append({
                    'product_name': str(row[0]),
                    'sale_percent': str(row[1])
                })
            pourcentagepvg=App.get_running_app().manager.ids.productsscreen.ids.productspage.ids.productlist.ids.salescontainer.ids.pourcentagepvg
            pourcentagepvg.ids.pv.data = data
            pourcentagepvg.clear_widgets()
            pourcentagepvg.add_widget(pourcentagepvg.ids.pv)
            """pourcentagepvg=App.get_running_app().manager.ids.statsscreen.ids.statsspage.ids.salescontainer.ids.pourcentagepvg
            pourcentagepvg.ids.pv.data = data
            pourcentagepvg.clear_widgets()
            pourcentagepvg.add_widget(pourcentagepvg.ids.pv)"""


    self.widget_showed = True
def show_profile_popup():
    profile_dialog = MDDialog(
        MDDialogHeadlineText(
            text="Modifier le profil",
        ),
        MDDialogContentContainer(
            MDTextField(
                MDTextFieldLeadingIcon(
                    icon="Eail",
                ),
                MDTextFieldHintText(
                    text="Email",
                ),
                MDTextFieldHelperText(
                    text="Entrer le nouveau mail",
                    mode="persistent",
                ),

                mode="outlined",
            ),
            MDTextField(
                MDTextFieldLeadingIcon(
                    icon="account",
                ),
                MDTextFieldHintText(
                    text="Pseudo",
                ),
                MDTextFieldHelperText(
                    text="Entres le nouveau pseudo",
                    mode="persistent",
                ),
                mode="outlined",
            ),
            MDTextField(
                MDTextFieldLeadingIcon(
                    icon="lock",
                ),
                MDTextFieldHintText(
                    text="Enrtrez le nouveau mot de passe",
                ),
                MDTextFieldHelperText(
                    text="ex: Meva004",
                    mode="persistent",
                ),
                mode="outlined",
            ),
            MDTextField(
                MDTextFieldLeadingIcon(
                    icon="lock",
                ),
                MDTextFieldHintText(
                    text="confirmer le mot de passe",
                ),
                mode="outlined",
            ),
            orientation="vertical",
            spacing="12dp",
            adaptive_height=True,
        ),
        MDDialogButtonContainer(
            MDButton(
                MDButtonText(text="Annuler"),
                style="text",
                on_release=lambda x: (profile_dialog.dismiss(), App.get_running_app().enable_button())            ),
            MDButton(
                MDButtonText(text="Modifier"),
                style="filled",
                on_release=update_profile,
            ),
            spacing="8dp",
        ),
    )
    profile_dialog.open()

def update_profile(dialog):
    # Récupérer les valeurs des champs
    content = dialog.ids.container.children[0]

    email = content.ids.email_field.text
    username = content.ids.username_field.text
    password = content.ids.password_field.text
    confirm_password = content.ids.confirm_password_field.text

    # Validation
    if password != confirm_password:
        print("Les mots de passe ne correspondent pas!")
        return

    # Votre logique de mise à jour ici
    print(f"Email: {email}")
    print(f"Username: {username}")
    print(f"Password: {password}")

    dialog.dismiss()
def show_popup(self,title, message):
    popup = Popup(size_hint=(.4,.4))
    popup.title = title
    content = BoxLayout(orientation='vertical')
    label=Label(text=message)
    button = Button(text='ok',size_hint=(.3,.3),pos_hint={'right':.94,'y':.012})
    button.bind(on_press=popup.dismiss)
    for w in (label,button):content.add_widget(w)
    popup.content=content
    popup.open()
def show_popup_confirmation(self,title,message,nom,qt,pu=None):
    self.popup = Popup(size_hint=(.4, .4))
    self.popup.title = title
    content = BoxLayout(orientation='vertical')
    label = Label(text=message)
    boxbutton = BoxLayout(orientation='horizontal')
    button1 = Button(text='Confirmer', size_hint=(.3, .3), pos_hint={'right': .94, 'y': .012})
    button1.bind(on_press=partial(self.popup.dismiss,qt,pu))
    button2 = Button(text='Annuler', size_hint=(.3, .3), pos_hint={'right': .94, 'y': .012})
    button2.bind(on_press=self.popup_confirmed)
    for w in (button1,button2):boxbutton.add_widget(w)
    for w in (label, boxbutton): content.add_widget(w)
    self.popup.content = content
    self.popup.open()
def popup_confirmed(self,nom,qt,pu=None):
    self.popup.dismiss()
    if pu:to_database("update stock set qt=qt+%s pu=%s where nom=%s",(qt,pu,nom))
    else:to_database("update stock set qt=qt+%s where nom=%s",(qt,nom))
def ouvrir_fichier(self, instance):
    # Lancer tkinter de manière cachée juste pour le file dialog
    root = tk.Tk()
    root.withdraw()  # Cacher la fenêtre principale de Tkinter

    fichier = filedialog.askopenfilename(title="Choisissez un fichier")
    if fichier:
        self.label.text = f"Fichier sélectionné :\n{fichier}"
    root.destroy()  # Fermer le root tkinter après sélection


"""ORIENTATION = Literal["landscape","portrait"]

def orientation(self, instance: ThemeManager, orientation: ORIENTATION):
    if orientation == "portrait" and self.time_picker_horizontal:
        self.time_picker_horizontal.dismiss()
        hour = str(self.time_picker_horizontal.time.hour)
        minute = str(self.time_picker_horizontal.time.minute)
        Clock.schedule_once(
            lambda x: self.open_time_picker_vertical(hour, minute),
            0.1,
        )
    elif orientation == "landscape" and self.time_picker_vertical:
        self.time_picker_vertical.dismiss()
        hour = str(self.time_picker_vertical.time.hour)
        minute = str(self.time_picker_vertical.time.minute)
        Clock.schedule_once(
            lambda x: self.open_time_picker_horizontal(hour, minute),
            0.1,
        )
    if orientation == "portrait" and self.date_picker_horizontal:
        self.date_picker_horizontal.dismiss()
        day = str(self.date_picker_horizontal.date.minute)
        minute = str(self.date_picker_horizontal.date.minute)
        Clock.schedule_once(
            lambda x: self.open_date_picker_vertical(hour, minute),
            0.1,
        )
    elif orientation == "landscape" and self.date_picker_vertical:
        self.date_picker_vertical.dismiss()
        hour = str(self.date_picker_vertical.date.hour)
        minute = str(self.date_picker_vertical.date.minute)
        Clock.schedule_once(
            lambda x: self.open_date_picker_horizontal(hour, minute),
            0.1,
        )
"""
def show_time_picker_horizontal(self, hour, minute):
    self.time_picker_vertical = None
    self.time_picker_horizontal = MDTimePickerDialHorizontal(
        hour=hour, minute=minute
    )
    self.time_picker_horizontal.open()

def show_time_picker_vertical(self, hour, minute):
    self.time_picker_horizontal = None
    self.time_picker_vertical = MDTimePickerDialVertical(
        hour=hour, minute=minute
    )
    self.time_picker_vertical.open()

def date_picker(self):

    date_dialog = MDDockedDatePicker()
    # You have to control the position of the date picker dialog yourself.
    date_dialog.pos = [
        self.ids.date_button.center_x - date_dialog.width / 2,
        self.ids.date_button.y - (date_dialog.height + dp(32)),
    ]
    date_dialog.bind(on_ok=self.on_ok_date)
    date_dialog.open()

def modal_date_picker(self, *args):

    date_dialog = MDModalDatePicker(mode="range")
    # You have to control the position of the date picker dialog yourself.
    date_dialog.pos = [
        self.ids.date_button.center_x - date_dialog.width / 2,
        self.ids.date_button.y - (date_dialog.height + dp(32)),
    ]
    date_dialog.bind(on_ok=self.on_ok_periode)
    date_dialog.open()

def generate_fic_excel(title,column_title, datas,):
    # Créer un nouveau fichier Excel
    workbook = xlsxwriter.Workbook(f'{title}.xlsx')
    worksheet = workbook.add_worksheet()
    for i in range(len(column_title)):
        worksheet.write(0,i,str(column_title[i]))

    for data in enumerate(datas):
        for item in enumerate(data[1]):
            worksheet.write(data[0]+1,item[0], str(item[1]))

    # Fermer le fichier
    workbook.close()

data = [('banane',2),('citron',5),('orange',6),('pommes','8')]
generate_fic_excel('fruit5',('modeles','quantité'),data)

def show_year(action):
    # 1. Crée une seule instance du label
    year_label = MDLabel(text=str(datetime.now().year), halign="center", theme_text_color="Primary", font_style="Title",
        size_hint_x=0.6)

    # 2. Fonctions modifiant CE label
    def increment_year(instance):
        current = int(year_label.text)
        if current < datetime.now().year:
            year_label.text = str(current + 1)

    def decrement_year(instance):
        current = int(year_label.text)
        if current > 2000:
            year_label.text = str(current - 1)

    # 3. Création du dialog avec le label centré
    dialog = MDDialog(
        MDDialogHeadlineText(text="Année"),
        MDDialogContentContainer(
            MDBoxLayout(MDDivider(),
            MDBoxLayout(
                MDIconButton(icon="chevron-left", on_release=decrement_year),
                year_label,
                MDIconButton(icon="chevron-right", on_release=increment_year),
                spacing="20dp",padding="20dp",size_hint_x=1
            ),
            MDDivider(),orientation="vertical"),

        ),
        MDDialogButtonContainer(
            Widget(),  # Espaceur
            MDButton(
                MDButtonText(text="Annuler"),
                style="text",
                on_release=lambda x: dialog.dismiss()
            ),
            MDButton(
                MDButtonText(text="OK"),
                style="text",
                on_release=lambda x:  (
        dialog.dismiss(),
        action(year_label.text)
    )

            ),
            spacing="8dp",
        ),
    )

    dialog.open()

from datetime import datetime
import calendar

def show_month(action):
    # 1. Créer une seule instance du label
    current_date = datetime.now()
    current_month = current_date.month
    current_year = current_date.year

    # Liste des mois
    mois_noms = [
        "janvier", "février", "mars", "avril", "mai", "juin",
        "juillet", "août", "septembre", "octobre", "novembre", "décembre"
    ]

    # Label initial
    month_label = MDLabel(
        text=mois_noms[current_month - 1] + f" {current_year}",
        halign="center",
        theme_text_color="Primary",
        size_hint_x=0.6
    )

    # Variable de suivi
    selection = {"mois": current_month, "année": current_year}

    # 2. Fonctions pour modifier le mois
    def increment_month(instance):
        if selection["mois"] == 12:
            selection["mois"] = 1
            selection["année"] += 1
        else:
            selection["mois"] += 1
        update_label()

    def decrement_month(instance):
        if selection["mois"] == 1:
            selection["mois"] = 12
            selection["année"] -= 1
        else:
            selection["mois"] -= 1
        update_label()

    def update_label():
        month_label.text = mois_noms[selection["mois"] - 1] + f" {selection['année']}"

    # Fonction pour déclencher action avec la date de début et de fin du mois sélectionné
    def validate_selection(x):
        dialog.dismiss()
        y = selection["année"]
        m = selection["mois"]
        start_date = datetime(y, m, 1)
        end_day = calendar.monthrange(y, m)[1]
        end_date = datetime(y, m, end_day)
        action(start_date, end_date)

    # 3. Dialog
    dialog = MDDialog(
        MDDialogHeadlineText(text="Mois"),
        MDDialogContentContainer(
            MDBoxLayout(MDDivider(),
            MDBoxLayout(
                MDIconButton(icon="chevron-left", on_release=decrement_month),
                month_label,
                MDIconButton(icon="chevron-right", on_release=increment_month),
                spacing="20dp", padding="20dp",size_hint_x=1
            ),
            MDDivider(), orientation="vertical",size_hint_y=1)
        ),
        MDDialogButtonContainer(
            Widget(),  # Espaceur
            MDButton(
                MDButtonText(text="Annuler"),
                style="text",
                on_release=lambda x: dialog.dismiss()
            ),
            MDButton(
                MDButtonText(text="OK"),
                style="text",
                on_release=validate_selection
            ),
            spacing="8dp",
        ),
    )

    dialog.open()
