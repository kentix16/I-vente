from utilities.databases import to_database


class GestionModel:

    @property
    def get_pourcentage_produits_vendus(self):
        res = to_database("""SELECT s.nom,ROUND((SUM(pv.qte)/(select sum(qte) 
        from produits_vendu WHERE DATE(date_de_vente)=CURRENT_DATE()))*100,2) as pourcentage
         from stock s inner join produits_vendu pv on pv.id_produit=s.id_produit WHERE 
         DATE(pv.date_de_vente)= CURRENT_DATE() group by s.nom;
                           
                          """)
        return res
    @property
    def get_heures_stat(self):
        res = to_database("SELECT date_de_vente, qte FROM produits_vendu WHERE date(date_de_vente)=CURRENT_DATE()")
        return res


    @property
    def get_heures_stat(self):
        res = to_database("SELECT pv.date_de_vente, (pv.qte*s.pu) as somme from produits_vendu pv JOIN stock s ON "
                          "s.id_produit=pv.id_produit where DATE(pv.date_de_vente)=CURRENT_DATE()")
        return res
    @property
    def get_somme_total_gagnee(self):
        res = to_database("SELECT SUM(pv.qte*s.pu) FROM produits_vendu pv JOIN stock s ON s.id_produit=pv.id_produit WHERE DATE(date_de_vente)=CURRENT_DATE()")
        return res[0][0]
    @property
    def get_total_de_ventes(self):
        res = to_database("SELECT SUM(qte) as total FROM produits_vendu WHERE DATE(date_de_vente)=CURRENT_DATE()")
        return res[0][0]
    @property
    def get_produits_en_rupture(self):
        res = to_database('SELECT COUNT(nom) from stock WHERE qt=0 group by nom')
        if res:
            return res[0][0]
        else:
            return 0
    def get_produits(self, like):
        if like=="":
            res = to_database('SELECT s.nom, s.pu, s.qt, t.nom_type FROM stock s JOIN type_produit t ON t.id_type = s.id_type ORDER BY s.nom')
            return res
        else:
            query = """
                SELECT s.nom, s.pu, s.qt, t.nom_type
                FROM stock s
                JOIN type_produit t ON t.id_type = s.id_type
                WHERE s.nom LIKE %s OR s.pu LIKE %s OR s.qt LIKE %s OR t.nom_type LIKE %s
                ORDER BY s.nom
            """
            wildcard = f"%{like}%"
            params = (wildcard, wildcard, wildcard, wildcard)
            return to_database(query, params)
    @property
    def get_produits_vendus(self):
        res = to_database("SELECT pv.id_pv,s.nom,pv.date_de_vente,pv.qte from produits_vendu pv JOIN stock s "
                          "ON s.id_produit=pv.id_produit WHERE DATE(pv.date_de_vente)=CURRENT_DATE()")
        return res

    def get_produit_par_type(self,type):
        res = to_database('SELECT s.nom,s.pu,s.qt,t.nom_type from stock s'
                          ' join type_produit t on t.id_type=s.id_type '
                          'where t.nom_type=%s;',(type,))
        return res
    @property
    def get_last_row_produit(self):
        res = to_database('SELECT id_produit FROM stock ORDER BY id_produit DESC LIMIT 1')
        return res[0][0]
    @property
    def get_last_row_produit_vendu(self):
        res = to_database('SELECT id_pv FROM produits_vendu ORDER BY id_pv DESC LIMIT 1')
        return res[0][0]
    @property
    def get_last_row_type_produit(self):
        res = to_database('SELECT id_type FROM type_produit ORDER BY id_type DESC LIMIT 1')
        return res[0][0]

    @property
    def get_last_row_depense(self):
        res = to_database('SELECT id_dep FROM depense ORDER BY id_dep DESC LIMIT 1')
        return res[0][0]
    @property
    def get_last_depense(self):
        res = to_database(('SELECT id_dep FROM depense ORDER BY id_dep DESC LIMIT 1'))
        return res
    @property
    def get_last_historique(self):
        res = to_database('SELECT * from historique ORDER BY date DESC LIMIT 1')
        return res

    @property
    def get_type(self):
        res = to_database('SELECT nom_type FROM type_produit ORDER BY id_type')
        for i in range(len(res)):
            res[i]=res[i][0]
        return res
    def get_id_type(self,type):
        res = to_database('SELECT id_type from type_produit where nom_type=%s',(type,))
        return res[0][0]

    def get_expenses(self,order, date=None, date_fin=None):
        desc = list(order.values())[0]
        order_by = list(order.keys())[0]
        order_clause = f"ORDER BY {order_by}"
        if desc: order_clause+=' DESC'
        query_base = "SELECT date_dep, nom_dep, somme_dep FROM depense"

        if date:
            if not date_fin:
                res = to_database(f'{query_base} WHERE DATE(date_dep)=%s {order_clause}', (date,))
            else:
                res = to_database(f'{query_base} WHERE DATE(date_dep) BETWEEN %s AND %s {order_clause}',
                                  (date, date_fin))
        else:
            res = to_database(f'{query_base} {order_clause}')
        return res

    def get_historique(self,order, date=None, date_fin=None):
        desc = list(order.values())[0]
        order_by = list(order.keys())[0]
        order_clause = f"ORDER BY {order_by}"
        if desc:order_clause+=' DESC'

        if date:
            if not date_fin:
                res = to_database(f'SELECT * FROM historique WHERE DATE(date)=%s {order_clause}', (date,))
            else:
                res = to_database(f'SELECT * FROM historique WHERE DATE(date) BETWEEN %s AND %s {order_clause}',
                                  (date, date_fin))
        else:
            res = to_database(f'SELECT * FROM historique {order_clause}')
        return res

    @property
    def get_somme_portefeuille(self):
        res = to_database('SELECT sum(CASE WHEN mouvement=\'dépense\' THEN -somme ELSE somme END) from historique')
        return res[0][0]