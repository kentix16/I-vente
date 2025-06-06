from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, ListProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from functools import partial
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
        gestionmodel = GestionModel()
        id_type = gestionmodel.get_id_type(type)
        print(id_product,nom,pu,qt,type)
        to_database('INSERT INTO stock VALUES (%s,%s,%s,%s,%s)',
                    (id_product, nom, pu, id_type, qt))
        self.ids.nom.text = ''
        self.ids.pu.text = ''
        self.ids.qt.text = ''
        self.parent.parent.parent.parent.ids.sliver_box.ids.listproducts.show_products()


class InsertProductType(MDCard):
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
        to_database('INSERT INTO type_produit VALUES(%s,%s,"CLI001")',
                    (id_type, nom_type))

        App.get_running_app().manager.ids.productsscreen.ids.productspage.ids.insertproduct.load_product_types()
        self.ids.typetoinsert.text=''



class GuitarItem(MDListItem):
    pass

class Content(MDSliverAppbarContent):
    """Composant Sliver qui affiche la liste des guitares."""

    def __init__(self, **kwargs):
        super(Content, self).__init__(**kwargs)
        #Méthode pour initialiser et peupler le contenu du sliver en toute sécurité.
        """try:
            # Ajouter des éléments de guitare
                guitar_models = [
                    {"brand": "Ibanez", "model": "GRG121DX-BKF", "price": "$445.99"},
                    {"brand": "Fender", "model": "Stratocaster AM", "price": "$849.99"},
                    {"brand": "Gibson", "model": "Les Paul Studio", "price": "$1,299.99"},
                    {"brand": "ESP", "model": "LTD EC-1000", "price": "$999.99"},
                    {"brand": "PRS", "model": "SE Custom 24", "price": "$789.99"}
                ]

                for guitar in guitar_models:
                    item = MDListItem(
                MDListItemLeadingIcon(icon="guitar-electric"),
                MDListItemHeadlineText(text=guitar["brand"]),
                MDListItemSupportingText(text=guitar["model"]),
                MDListItemTertiaryText(text=guitar["price"]),
                MDListItemTrailingIcon(icon="cart"),
            )


                    # Ajouter l'élément à la liste
                    self.add_widget(item)
                    print(f"Guitare ajoutée: {guitar['brand']} {guitar['model']}")


        except Exception as e:
            print(f"Erreur lors de l'initialisation du contenu: {e}")"""

class ProductsPage(MDBoxLayout):
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

    def show_products(self):
        if self.grid_showed:
            self.remove_widget(self.grid)
            self.grid = None
        self.grid = GridLayout(cols=5,spacing=2,size_hint_y=None)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        instance = GestionModel()
        produits = instance.get_produits
        #print(produits)
        titles = ('PRODUITS','PU','QT','TYPE','')
        for i in enumerate(titles):
            cell = Label(text=i[1], color=(0, 0, 0, 1), bold=True, size_hint=(1, None), height=20)
            if i[0]==4:
                cell.size_hint=(.45,None)
            self.grid.add_widget(cell)
        for row in produits:
            for item in range(len(row)):
                cell = Label(text = f'{row[item]}',color=(.2,.2,.2,1),size_hint=(1,None),height=20)
                self.grid.add_widget(cell)
            else:
                btn = Button(text='-',bold=True,color=(1,0,0,1),size_hint=(.45,None),
                              height=20,background_color=(0,0,0,.1))
                btn.bind(on_press=partial(self.remove_product,nom_produit=row[0]))
                self.grid.add_widget(btn)
        self.add_widget(self.grid)
        self.grid_showed = True

    def remove_product(self,instance,nom_produit):
        try:
            to_database('DELETE FROM stock WHERE nom=%s',(nom_produit,))
            self.show_products()
        except:print('on ne peut pas effacer')

class DeleteProduct(MDCard):
    def __init__(self,**kwargs):
        super(DeleteProduct,self).__init__(**kwargs)

    def sale_product(self):
        nom = self.ids.nom_produit_vente.text
        qt=self.ids.qt_produit_vente.text
        print(nom,qt)
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
        id_produit_vendu = to_database('SELECT id_produit FROM stock WHERE nom=%s',(nom,))
        to_database('INSERT INTO produits_vendu VALUES(%s,CURRENT_TIMESTAMP,%s,%s)', (id_prov,qt,id_produit_vendu[0][0]))
        self.ids.nom_produit_vente.text = ''
        self.ids.qt_produit_vente.text = ''
        App.get_running_app().manager.update_all()





