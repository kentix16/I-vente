from kivy.app import App
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivymd.uix.behaviors import RotateBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog, MDDialogButtonContainer, MDDialogHeadlineText
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
import os

from kivymd.uix.pickers import MDTimePickerDialHorizontal, MDModalDatePicker
from kivymd.uix.screen import MDScreen
from kivymd.uix.sliverappbar import MDSliverAppbarContent

from controllers.sales_page import PourcentagePV
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
from kivymd.uix.list import MDListItem, MDListItemHeadlineText, MDListItemTrailingIcon


class MDExpansionPanelThreeLine:
    pass

class TrailingPressedIconButton(
    ButtonBehavior, RotateBehavior, MDListItemTrailingIcon
):
    ...

class InsertProduct(MDCard):
    from utilities.myfunctions import show_popup,show_popup_confirmation
    product_types = ListProperty()
    selected_product_type = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Ne rien faire ici avec self.ids
        self.extension(showed=False)

    def tap_expansion_chevron(
            self, panel: MDExpansionPanel, chevron: TrailingPressedIconButton
    ):
        panel.open() if not panel.is_open else panel.close()
        panel.set_chevron_down(
            chevron
        ) if not panel.is_open else panel.set_chevron_up(chevron)

    def extension(self,showed=False):
        if showed=="False":
            panel=self.ids.panel
            instance = GestionModel()
            product_types = instance.get_type
            for produit in product_types:
                label=MDLabel(text=f'{produit}', color=(.2, .2, .2, 1), size_hint=(1, None), height=40)
                panel.MDExpansionPanelContent.add_widget(label)
            showed=True
            for i in range(20):
                print("ao le type")
        else:
            return
    """def on_kv_post(self, base_widget):
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
        print("Type sélectionné :", text)"""
    def show_produit(self):
        instance = GestionModel()
        product_types = instance.get_type
        data=[]

        for produit in product_types:
            data.append({"type_produit": produit})
        self.ids.Pd.data=data
        for i in range(30):
            print(self.ids.Pd.data)

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
            plus=''
            if not gestionmodel.same_pu_stock(nom,int(pu)):plus=f' \net mettre à jour son pu'
            message = (f'duplicata du nom de produit.\n'
                       f'voulez-vous ajouter {qt} à ce produit{plus}?')
            self.show_popup_confirmation(title='erreur',message=message,nom=nom,pu=pu,qt=qt)
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

    def change_page_screen(self):
        screen_manager = self.ids.product_sreen_manager
        screen_manager.current = "screenTwo"
        screen_manager.transition.direction = "left"
    def change_page_screen_pop(self):
        screen_manager = self.ids.product_sreen_manager
        screen_manager.current = "screenOne"
        screen_manager.transition.direction = "left"
    def change_screen(self):
        screen_manager = self.ids.defaultscreen.ids.screen_manager
        screen_manager.current = "screen2"
        screen_manager.transition.direction = "left"

    def change_screen_pop(self):
        screen_manager = self.ids.defaultscreen.ids.screen_manager
        screen_manager.current = "screen1"
        screen_manager.transition.direction = "right"
        insert_product = screen_manager.get_screen("screen1").children[0]
        insert_product.load_product_types()
    def change_screen_type(self):
        screen_manager = self.ids.defaultscreen.ids.screen_manager
        screen_manager.current = "screen3"
        screen_manager.transition.direction = "left"
class ProductList(MDScreen):
    time_picker_vertical: MDTimePickerDialHorizontal = ObjectProperty(allownone=True)
    date_picker_horizontal: MDModalDatePicker = ObjectProperty(allownone=True)
    date_picker_vertical: MDModalDatePicker = ObjectProperty(allownone=True)
    # from utilities.myfunctions import orientation
    from utilities.myfunctions import show_time_picker_horizontal
    from utilities.myfunctions import show_time_picker_vertical
    from utilities.myfunctions import date_picker
    from utilities.myfunctions import modal_date_picker

    def __init__(self, **kwargs):
        super(ProductList, self).__init__(**kwargs)

    def open_time_picker_horizontal(self, hour, minute):
        self.show_time_picker_horizontal(hour, minute)

    def open_time_picker_vertical(self, hour, minute):
        self.show_time_picker_vertical(hour, minute)

    def show_date_picker(self):
        self.date_picker()

    def show_modal_date_picker(self, *args):
        self.modal_date_picker()

    def on_ok_date(self, instance_date_picker,):
        date = instance_date_picker.get_date()[0]

        self.ids.salescontainer.date = date
        self.ids.salescontainer.date_fin = None
        self.ids.salescontainer.ids.pourcentagepvg.show_pourcentage_pv(date=date)
        instance_date_picker.dismiss()

    def on_ok_periode(self, instance_date_picker):
        date = instance_date_picker.get_date()[0]
        date_fin = instance_date_picker.get_date()[-1]

        self.ids.salescontainer.date = date
        self.ids.salescontainer.date_fin = date_fin

        self.ids.salescontainer.ids.pourcentagepvg.show_pourcentage_pv(date,date_fin)
        self.ids.pourcentagedepense.show_pourcentage_depense(date, date_fin)
        instance_date_picker.dismiss()


class Resume(BoxLayout):
    initiale=StringProperty()
    vendu=StringProperty()
    perime=StringProperty()
    reste=StringProperty()

class SalesStatContent(MDBoxLayout):

    def __init__(self, **kwargs):
        super(SalesStatContent, self).__init__(**kwargs)
        self.date = None
        self.date_fin = None
        self._search_trigger= Clock.create_trigger(self.search_order_delayed,0.3)

    def on_kv_post(self, base_widget):
        Clock.schedule_once(self.load_initial_data)

    def load_initial_data(self, dt):
        order = self.ids.textfieldproductsold.text
        pv_widget = self.ids.pourcentagepvg.ids.get("pv")
        if pv_widget:
            self.ids.pourcentagepvg.show_pourcentage_pv(
            date=self.date, date_fin=self.date_fin, order=order
        )
        else:
            print("pv introuvable (init)")

    def search_order(self):
        self._search_trigger()

    def search_order_delayed(self, *args):
        order = self.ids.textfieldproductsold.text
        pv_widget = self.ids.pourcentagepvg.ids.get("pv")
        if pv_widget:
            self.ids.pourcentagepvg.show_pourcentage_pv(
            date=self.date, date_fin=self.date_fin, order=order
        )
        else:
            print("pv introuvable (search)")

class ProductRowPV(BoxLayout):
    product_name=StringProperty()
    sale_percent=StringProperty()
class PourcentagePVG(PourcentagePV):
    widget_showed = False

    def __init__(self, **kwargs):
        super(PourcentagePVG, self).__init__(**kwargs)
        Clock.schedule_once(self.delayed_init)

    def delayed_init(self, dt):
        # Assure-toi que l'ID 'pv' est bien présent
        if "pv" in self.ids:
            self.show_pourcentage_pv()
        else:
            print("ERREUR: id 'pv' introuvable dans PourcentagePVG")

class ProductResume(ScrollView):
    def __init__(self,**kwargs):
        super(ProductResume,self).__init__(**kwargs)

    def show_list(self):
        stock_init=GestionModel().get_initial_product()
        sold_product=GestionModel().get_sold_product()
        current_stock=GestionModel().get_current_stock()
        minimum=min(len(stock_init),len(sold_product),len(current_stock))
        data=[]
        for i in range(minimum):
            data.append({"initiale":str(stock_init[i]),"vendu":str(sold_product[i]),"perime":str(0),"reste":str(current_stock[i])})

        self.ids.pr.data=data
        for i in range(2):
            print(self.ids.pr.data)



class ListProducts(ScrollView):
    grid_showed = False
    grid = None
    def __init__(self,**kwargs):
        super(ListProducts,self).__init__(**kwargs)

    def sell_product(self, nom_produit):
        App.get_running_app().manager.ids.productsscreen.ids.productspage.ids.delectproduct.ids.nom_produit_vente.text = nom_produit
    def remove_product(self,nom_produit):
        to_database("update stock set is_showed=0 WHERE nom=%s",(nom_produit,))
        self.show_products()
    def show_products(self, order=""):
        produits= GestionModel().get_produits(order)
        data=[]

        for row in produits:
            data.append({
                'nom_produit': str(row[0]),
                'prix_unitaire': str(row[1]),
                'qt': str(row[2]),
                'type': str(row[3]),

            })
        self.ids.rv.data = data

class Produit(BoxLayout):
    type_produit=StringProperty()


class ProductRow(BoxLayout):
    nom_produit=StringProperty()
    type=StringProperty()
    qt=StringProperty()
    prix_unitaire=StringProperty()

class SaleProduct(MDCard):
    from utilities.myfunctions import show_popup
    def __init__(self,**kwargs):
        super(SaleProduct,self).__init__(**kwargs)

    def sale_product(self):
        gestionmodel = GestionModel()
        nom = self.ids.nom_produit_vente.text
        try:qt=int(self.ids.qt_produit_vente.text)
        except:
            self.show_popup('erreur','qt invalide')
            return None

        if gestionmodel.qt_stock(nom)>=qt: to_database('UPDATE stock SET qt=qt-%s WHERE nom=%s',(qt,nom))
        else:
            self.show_popup('erreur','quantité insuffisante')
            return
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
        App.get_running_app().manager.ids.productsscreen.ids.productspage.ids.sliver_box.ids.content.ids.listproducts.show_products()








