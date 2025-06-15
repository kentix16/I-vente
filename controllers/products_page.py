from kivy.app import App
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.properties import StringProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog, MDDialogButtonContainer, MDDialogHeadlineText
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
import os

from kivymd.uix.sliverappbar import MDSliverAppbarContent

from models.gestionModel import GestionModel
from utilities.databases import to_database


# Chemin de votre fichier KV
kv_path = os.path.join(os.path.dirname(__file__), '..', 'view', 'products_page.kv')
# Charger le fichier KV seulement s'il n'est pas déjà chargé
if not os.path.basename(kv_path) in Builder.files:
    Builder.load_file(kv_path)

class ExpansionPanelItem(MDExpansionPanel):
    ...


class MDExpansionPanelOneLine:
    pass


class OneLineListItem:
    pass


from kivymd.uix.expansionpanel import MDExpansionPanel
from kivymd.uix.list import MDListItem, MDListItemHeadlineText


class MDExpansionPanelThreeLine:
    pass


class InsertProduct(MDCard):
    from utilities.myfunctions import show_popup
    product_types = ListProperty()
    selected_product_type = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Ne rien faire ici avec self.ids

    def on_kv_post(self, base_widget):
        # Cette méthode est appelée automatiquement une fois le KV chargé
        self.load_product_types()

    def load_product_types(self):
        instance = GestionModel()
        types = instance.get_type or []
        self.product_types = [str(t) for t in types]  # ⚠️ forcer la conversion en string
        if self.ids.get("product_type_spinner"):  # sécurité si spinner déjà instancié
            self.ids.product_type_spinner.values = self.product_types
        else:
            self.ids.product_type_spinner.values = ["Aucun type"]

    def on_product_type_select(self, spinner, text):
        self.selected_product_type = text
        print("Type sélectionné :", text)
    def show_product_type(self):
        expansion_panel = self.ids.product_type

        content = MDBoxLayout(size_hint=(None,None),size=("120dp","50"),orientation="vertical", spacing="10dp", padding="10dp")

        instance = GestionModel()
        product_types = instance.get_type

        if not product_types:
            content.add_widget(MDLabel(text="Aucun type disponible", halign="center"))
        else:
            for p_type in product_types:
                item = MDListItem(
                    MDListItemHeadlineText(text=str(p_type)),
                    on_release=lambda x, pt=p_type: self.select_product_type(str(pt)),
                    size_hint_y=None,
                    height=dp(48)
                )
                content.add_widget(item)

        panel = MDExpansionPanel(_content=content)
        expansion_panel.add_widget(panel)

    def select_product_type(self, product_type):
        # Stocker le type sélectionné
        self.selected_product_type = product_type
        print(f"Type sélectionné: {product_type}")
    def add(self):
        def get_id_produit_and_increment():
            gestionmodel = GestionModel()
            try:
                lastrow = gestionmodel.get_last_row_produit
            except:
                lastrow='PRO0'
            number = int(lastrow[3:])
            number+=1
            new_id='PRO'+str(number)
            print(new_id)
            return new_id
        for i in range(100):print('ajout')
        id_product=get_id_produit_and_increment()
        nom = self.ids.nom.text
        pu = self.ids.pu.text
        qt = self.ids.qt.text
        type = self.selected_product_type
        if not (nom and pu and qt):
            self.show_popup('champ manquant','veuillez compléter les champs manquants')
            return
        if not (qt.isnumeric() and pu.isnumeric()):
            self.show_popup('erreur', 'la quantité et le pu doivent \nêtre des entiers')
            return
        if not type:
            self.show_popup('erreur','aucun type séléctionné')
            return
        gestionmodel = GestionModel()
        id_type = gestionmodel.get_id_type(type)
        print(id_product,nom,pu,qt,type)
        try:to_database('INSERT INTO stock VALUES (%s,%s,%s,%s,%s)',
                    (id_product, nom, pu, id_type, qt))
        except:
            message = 'duplicata de nom de produit '+str(nom)
            self.show_popup(title='erreur',message=message)
            return
        self.ids.nom.text = ''
        self.ids.pu.text = ''
        self.ids.qt.text = ''
        manager = App.get_running_app().manager
        manager.ids.productsscreen.ids.productspage.ids.sliver_box.ids.content.ids.listproducts.show_products()


class InsertProductType(MDCard):
    from utilities.myfunctions import show_popup
    def add_type(self):
        def get_id_produit_vendu_and_increment():
            gestionmodel = GestionModel()
            try:
                lastrow = gestionmodel.get_last_row_type_produit
            except:
                lastrow = 'TYP001'
            number = int(lastrow[3:])
            number += 1
            new_id = 'TYP' + f'{number:03d}'
            return new_id
        id_type = get_id_produit_vendu_and_increment()
        nom_type = self.ids.typetoinsert.text
        if not nom_type.isalpha():
            App.get_running_app().manager.ids.productsscreen.ids.productspage.show_dialog()
        try:
            to_database('INSERT INTO type_produit VALUES(%s,%s,"CLI001")',
                    (id_type, nom_type))
        except:
            message = f'Duplicata du type {nom_type}'
            self.show_popup('erreur',message)
            return
        

        App.get_running_app().manager.ids.productsscreen.ids.productspage.ids.insertproduct.load_product_types()
        self.ids.typetoinsert.text=''



class GuitarItem(MDListItem):
    pass

class Content(MDSliverAppbarContent):

    def __init__(self, **kwargs):
        super(Content, self).__init__(**kwargs)
        #Méthode pour initialiser et peupler le contenu du sliver en toute sécurité.
        self._search_trigger= Clock.create_trigger(self.search_order_delayed,0.3)

    def on_kv_post(self, base_widget):
        productsearchbar = self.ids.search_textfield.text
        productslist = self.ids.listproducts
        productslist.show_products(productsearchbar)

    def search_order(self):
        self._search_trigger()

    def search_order_delayed(self,*args):
        productsearchbar = self.ids.search_textfield.text
        productslist=self.ids.listproducts
        productslist.show_products(productsearchbar)


class MDFlatButton:
    pass


class ProductsPage(MDBoxLayout):
    def show_dialog(self):
        MDDialog(
            MDDialogHeadlineText(
                text="Erreur",
                halign="left",
            ),
            MDDialogButtonContainer(
                Widget(),
                MDButton(
                    MDButtonText(text="Annuler"),
                    style="text",
                ),

                spacing="8dp",
            ),
        ).open()

    def change_screen(self):
        screen_manager = self.ids.screen_manager
        screen_manager.current = "screen2"
        screen_manager.transition.direction = "left"

    def change_screen_pop(self):
        screen_manager = self.ids.screen_manager
        screen_manager.current = "screen1"
        screen_manager.transition.direction = "right"
        insert_product = screen_manager.get_screen("screen1").children[0]
        insert_product.load_product_types()
    def change_screen_type(self):
        screen_manager = self.ids.screen_manager
        screen_manager.current = "screen3"
        screen_manager.transition.direction = "left"



class ListProducts(ScrollView):
    grid_showed = False
    grid = None
    def __init__(self,**kwargs):
        super(ListProducts,self).__init__(**kwargs)

    def remove_product(self, nom_produit):
        App.get_running_app().manager.ids.productsscreen.ids.productspage.ids.delectproduct.ids.nom_produit_vente.text = nom_produit
    def show_products(self, order=""):
        produits= GestionModel().get_produits(order)
        data=[]

        for row in produits:
            data.append({
                'nom_produit': str(row[0]),
                'pu': str(row[1]),
                'qt': str(row[2]),
                'type': str(row[3]),

            })
        self.ids.rv.data = data

class ProductRow(BoxLayout):
    nom_produit=StringProperty()
    type=StringProperty()
    qt=StringProperty()
    prix_unitaire=StringProperty()

class DeleteProduct(MDCard):
    from utilities.myfunctions import show_popup
    def __init__(self,**kwargs):
        super(DeleteProduct,self).__init__(**kwargs)

    def sale_product(self):
        nom = self.ids.nom_produit_vente.text
        try:qt=int(self.ids.qt_produit_vente.text)
        except:
            self.show_popup('erreur','qt invalide')
            return None
        to_database('UPDATE stock SET qt=qt-%s WHERE nom=%s',(qt,nom))
        self.add_to_produit_vendu(qt,nom)

    def add_to_produit_vendu(self,qt,nom):
        def get_id_produit_vendu_and_increment():
            gestionmodel = GestionModel()
            try:
                lastrow = gestionmodel.get_last_row_produit_vendu
            except:
                lastrow='PROV001'
            number = int(lastrow[4:])
            number+=1
            new_id='PROV'+f'{number:03d}'
            print(new_id)
            return new_id
        id_prov=get_id_produit_vendu_and_increment()
        try:
            id_produit_vendu = to_database('SELECT id_produit FROM stock WHERE nom=%s',(nom,))
            to_database('INSERT INTO produits_vendu VALUES(%s,CURRENT_TIMESTAMP,%s,%s)', (id_prov,qt,id_produit_vendu[0][0]))
            App.get_running_app().manager.update_all()
        except:
            print('ce produit n\'existe pas')
            self.show_popup('Erreur','Vente invalide')
        self.ids.nom_produit_vente.text = ''
        self.ids.qt_produit_vente.text = ''






