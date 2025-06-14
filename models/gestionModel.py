from utilities.databases import to_database


class GestionModel:


    def get_pourcentage_produits_vendus(self,date=None,date_fin=None,order=""):
        if order=="":
            if date:
                if date_fin:
                    res = to_database("""SELECT s.nom,ROUND((SUM(pv.qte)/(select sum(qte) 
                            from produits_vendu WHERE DATE(date_de_vente) BETWEEN %s AND %s))*100,2) as pourcentage
                             from stock s inner join produits_vendu pv on pv.id_produit=s.id_produit WHERE 
                             DATE(pv.date_de_vente) BETWEEN %s AND %s group by s.nom ORDER BY pourcentage DESC;        
                                              """, (date,date_fin,date,date_fin))
                else:
                    res = to_database("""SELECT s.nom,ROUND((SUM(pv.qte)/(select sum(qte) 
            from produits_vendu WHERE DATE(date_de_vente)=%s))*100,2) as pourcentage
             from stock s inner join produits_vendu pv on pv.id_produit=s.id_produit WHERE 
             DATE(pv.date_de_vente)=%s  group by s.nom ORDER BY pourcentage DESC;        
                              """,(date,date))
            else:res = to_database("""SELECT s.nom,ROUND((SUM(pv.qte)/(select sum(qte) 
            from produits_vendu WHERE DATE(date_de_vente)=CURRENT_DATE()))*100,2) as pourcentage
             from stock s inner join produits_vendu pv on pv.id_produit=s.id_produit WHERE 
             DATE(pv.date_de_vente)= CURRENT_DATE() group by s.nom ORDER BY pourcentage DESC;         
                              """)
            return res
        else:
            like_order = f"%{order}%"

            if date:
                if date_fin:
                    query = """
                        SELECT s.nom,
                               ROUND((SUM(pv.qte) / (SELECT SUM(qte) FROM produits_vendu
                                                      WHERE DATE(date_de_vente) BETWEEN %s AND %s)) * 100, 2) AS pourcentage
                        FROM stock s
                        INNER JOIN produits_vendu pv ON pv.id_produit = s.id_produit
                        WHERE DATE(pv.date_de_vente) BETWEEN %s AND %s
                        GROUP BY s.nom
                        HAVING s.nom LIKE %s OR CAST(pourcentage AS CHAR) LIKE %s
                        ORDER BY pourcentage DESC;
                    """
                    params = (date, date_fin, date, date_fin, like_order, like_order)

                else:
                    query = """
                        SELECT s.nom,
                               ROUND((SUM(pv.qte) / (SELECT SUM(qte) FROM produits_vendu
                                                      WHERE DATE(date_de_vente) = %s)) * 100, 2) AS pourcentage
                        FROM stock s
                        INNER JOIN produits_vendu pv ON pv.id_produit = s.id_produit
                        WHERE DATE(pv.date_de_vente) = %s
                        GROUP BY s.nom
                        HAVING s.nom LIKE %s OR CAST(pourcentage AS CHAR) LIKE %s
                        ORDER BY pourcentage DESC;
                    """
                    params = (date, date, like_order, like_order)
            else:
                query = """
                    SELECT s.nom,
                           ROUND((SUM(pv.qte) / (SELECT SUM(qte) FROM produits_vendu
                                                  WHERE DATE(date_de_vente) = CURRENT_DATE())) * 100, 2) AS pourcentage
                    FROM stock s
                    INNER JOIN produits_vendu pv ON pv.id_produit = s.id_produit
                    WHERE DATE(pv.date_de_vente) = CURRENT_DATE()
                    GROUP BY s.nom
                    HAVING s.nom LIKE %s OR CAST(pourcentage AS CHAR) LIKE %s
                    ORDER BY pourcentage DESC;
                """
                params = (like_order, like_order)

            print("Requête exécutée avec order:", order)
            return to_database(query, params)


    @property
    def get_heures_stat(self):
        res = to_database("SELECT date_de_vente, qte FROM produits_vendu WHERE date(date_de_vente)=CURRENT_DATE()")
        return res
    def get_min_max_heures_vente(self,order="MIN",date=None):
        if date:
            query = f"""
            SELECT COALESCE({order}(HOUR(date_de_vente)), 0)
            FROM produits_vendu
            WHERE DATE(date_de_vente) = %s
        """
            res = to_database(query, (date,))
        else:
            query = f"""
                       SELECT COALESCE({order}(HOUR(date_de_vente)), 0)
                       FROM produits_vendu
                       WHERE DATE(date_de_vente) = CURDATE()
                   """
            res = to_database(query)
        return int(res[0][0]) if res and res[0] else 0

    def get_min_max_heures_dep(self, order="MIN", date=None):
        if order not in ("MIN", "MAX"):
            raise ValueError("order doit être 'MIN' ou 'MAX'")

        if date:
            query = f"""
                SELECT COALESCE({order}(HOUR(date_dep)), 0)
                FROM depense
                WHERE DATE(date_dep) = %s
            """
            res = to_database(query, (date,))
        else:
            query = f"""
                SELECT COALESCE({order}(HOUR(date_dep)), 0)
                FROM depense
                WHERE DATE(date_dep) = CURDATE()
            """
            res = to_database(query)

        return int(res[0][0]) if res and res[0] else 0

    def get_heures_depense_stat(self, date=None, date_fin=None, heure_min=None, heure_max=None):
        if date:
            if date_fin:
                res = to_database("""
                    WITH RECURSIVE date_range AS (
                        SELECT DATE(%s) AS date_jour
                        UNION ALL
                        SELECT DATE_ADD(date_jour, INTERVAL 1 DAY)
                        FROM date_range
                        WHERE date_jour < %s
                    )
                    SELECT 
                        d.date_jour,
                        COALESCE(SUM(dep.somme_dep), 0) AS depense_du_jour
                    FROM date_range d
                    LEFT JOIN depense dep ON DATE(dep.date_dep) = d.date_jour
                    GROUP BY d.date_jour
                    ORDER BY d.date_jour
                """, (date, date_fin))
            else:
                res = to_database("""
                    WITH RECURSIVE interval_time AS (
                        SELECT CAST(CONCAT(%s, ' ', %s) AS DATETIME) AS time_slot
                        UNION ALL
                        SELECT DATE_ADD(time_slot, INTERVAL 1 HOUR)
                        FROM interval_time
                        WHERE time_slot < CAST(CONCAT(%s, ' ', %s) AS DATETIME)
                    ),
                    dep_sum AS (
                        SELECT 
                            DATE_FORMAT(date_dep, '%Y-%m-%d %H:00:00') AS rounded_hour,
                            SUM(somme_dep) AS somme
                        FROM depense
                        WHERE date_dep >= CAST(CONCAT(%s, ' ', %s) AS DATETIME)
                          AND date_dep < CAST(CONCAT(%s, ' ', %s) AS DATETIME)
                        GROUP BY rounded_hour
                    )
                    SELECT 
                        it.time_slot,
                        COALESCE(ds.somme, 0) AS depense
                    FROM interval_time it
                    LEFT JOIN dep_sum ds 
                        ON ds.rounded_hour = DATE_FORMAT(it.time_slot, '%Y-%m-%d %H:00:00')
                    ORDER BY it.time_slot
                """, (date, heure_min, date, heure_max, date, heure_min, date, heure_max))
        else:
            res = to_database("""
                WITH RECURSIVE interval_time AS (
                    SELECT CAST(CONCAT(CURDATE(), ' ', %s) AS DATETIME) AS time_slot
                    UNION ALL
                    SELECT DATE_ADD(time_slot, INTERVAL 1 HOUR)
                    FROM interval_time
                    WHERE time_slot < CAST(CONCAT(CURDATE(), ' ', %s) AS DATETIME)
                ),
                dep_sum AS (
                    SELECT 
                        DATE_FORMAT(date_dep, '%Y-%m-%d %H:00:00') AS rounded_hour,
                        SUM(somme_dep) AS somme
                    FROM depense
                    WHERE date_dep >= CAST(CONCAT(CURDATE(), ' ', %s) AS DATETIME)
                      AND date_dep < CAST(CONCAT(CURDATE(), ' ', %s) AS DATETIME)
                    GROUP BY rounded_hour
                )
                SELECT 
                    it.time_slot,
                    COALESCE(ds.somme, 0) AS depense
                FROM interval_time it
                LEFT JOIN dep_sum ds 
                    ON ds.rounded_hour = DATE_FORMAT(it.time_slot, '%Y-%m-%d %H:00:00')
                ORDER BY it.time_slot
            """, (heure_min, heure_max, heure_min, heure_max))

        return res

    def get_heures_somme_stat(self, date=None, date_fin=None, heure_min=None, heure_max=None):
        if date:
            if date_fin:
                res = to_database("""
                    WITH RECURSIVE date_range AS (
                        SELECT DATE(%s) AS date_jour
                        UNION ALL
                        SELECT DATE_ADD(date_jour, INTERVAL 1 DAY)
                        FROM date_range
                        WHERE date_jour < %s
                    )
                    SELECT 
                        d.date_jour,
                        COALESCE(SUM(pv.qte * s.pu), 0) AS vente_du_jour
                    FROM date_range d
                    LEFT JOIN produits_vendu pv ON DATE(pv.date_de_vente) = d.date_jour
                    LEFT JOIN stock s ON s.id_produit = pv.id_produit
                    GROUP BY d.date_jour
                    ORDER BY d.date_jour
                """, (date, date_fin))
            else:
                res = to_database("""
                    WITH RECURSIVE interval_time AS (
                        SELECT CAST(CONCAT(%s, ' ', %s) AS DATETIME) AS time_slot
                        UNION ALL
                        SELECT DATE_ADD(time_slot, INTERVAL 1 HOUR)
                        FROM interval_time
                        WHERE time_slot < CAST(CONCAT(%s, ' ', %s) AS DATETIME)
                    ),
                    vente_sum AS (
                        SELECT 
                            DATE_FORMAT(pv.date_de_vente, '%Y-%m-%d %H:00:00') AS rounded_hour,
                            SUM(pv.qte * s.pu) AS somme
                        FROM produits_vendu pv
                        LEFT JOIN stock s ON s.id_produit = pv.id_produit
                        WHERE pv.date_de_vente >= CAST(CONCAT(%s, ' ', %s) AS DATETIME)
                          AND pv.date_de_vente < CAST(CONCAT(%s, ' ', %s) AS DATETIME)
                        GROUP BY rounded_hour
                    )
                    SELECT 
                        it.time_slot,
                        COALESCE(vs.somme, 0) AS vente
                    FROM interval_time it
                    LEFT JOIN vente_sum vs 
                        ON vs.rounded_hour = DATE_FORMAT(it.time_slot, '%Y-%m-%d %H:00:00')
                    ORDER BY it.time_slot
                """, (date, heure_min, date, heure_max, date, heure_min, date, heure_max))
        else:
            res = to_database("""
                WITH RECURSIVE interval_time AS (
                    SELECT CAST(CONCAT(CURDATE(), ' ', %s) AS DATETIME) AS time_slot
                    UNION ALL
                    SELECT DATE_ADD(time_slot, INTERVAL 1 HOUR)
                    FROM interval_time
                    WHERE time_slot < CAST(CONCAT(CURDATE(), ' ', %s) AS DATETIME)
                ),
                vente_sum AS (
                    SELECT 
                        DATE_FORMAT(pv.date_de_vente, '%Y-%m-%d %H:00:00') AS rounded_hour,
                        SUM(pv.qte * s.pu) AS somme
                    FROM produits_vendu pv
                    LEFT JOIN stock s ON s.id_produit = pv.id_produit
                    WHERE pv.date_de_vente >= CAST(CONCAT(CURDATE(), ' ', %s) AS DATETIME)
                      AND pv.date_de_vente < CAST(CONCAT(CURDATE(), ' ', %s) AS DATETIME)
                    GROUP BY rounded_hour
                )
                SELECT 
                    it.time_slot,
                    COALESCE(vs.somme, 0) AS vente
                FROM interval_time it
                LEFT JOIN vente_sum vs 
                    ON vs.rounded_hour = DATE_FORMAT(it.time_slot, '%Y-%m-%d %H:00:00')
                ORDER BY it.time_slot
            """, (heure_min, heure_max, heure_min, heure_max))

        return res

    def get_somme_total_gagnee(self,date=None):
        if date:res = to_database("SELECT SUM(pv.qte*s.pu) FROM produits_vendu pv JOIN stock s ON s.id_produit=pv.id_produit WHERE DATE(date_de_vente)=%s",(date,))
        else:res = to_database("SELECT SUM(pv.qte*s.pu) FROM produits_vendu pv JOIN stock s ON s.id_produit=pv.id_produit WHERE DATE(date_de_vente)=CURRENT_DATE()")
        return res[0][0]
    def get_total_de_ventes(self,date=None):
        if date: res = to_database("SELECT SUM(qte) as total FROM produits_vendu WHERE DATE(date_de_vente)=%s",(date,))
        else: res = to_database("SELECT SUM(qte) as total FROM produits_vendu WHERE DATE(date_de_vente)=CURRENT_DATE()")
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

    def get_pourcentage_depense(self, date,date_fin):
        if  date:
            if date_fin:res = to_database('SELECT nom_dep,(SUM(somme_dep)*100/(SELECT SUM(somme_dep) FROM depense WHERE date(date_dep) BETWEEN %s AND %s)) as pourcentage from depense where date(date_dep) BETWEEN %s AND %s group by nom_dep ORDER BY pourcentage DESC',
                              (date,date_fin,date,date_fin))
            else:
                res = to_database('SELECT nom_dep,(SUM(somme_dep)*100/(SELECT SUM(somme_dep) FROM depense WHERE date(date_dep)=%s)) as pourcentage from depense where date(date_dep)=%s group by nom_dep order by pourcentage desc',
                              (date,date))
        else:
            res = to_database('SELECT nom_dep,(SELECT SUM(somme_dep) FROM depense WHERE date(date_dep)=CURRENT_DATE()) as pourcentage from depense where date(date_dep)=CURRENT_DATE() group by nom_dep')

        return res
