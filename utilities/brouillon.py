###################pour les anciens show_state_du_jour########################
"""self.clear_widgets()
        salemodel = GestionModel()
        heure_min_vente = salemodel.get_min_max_heures_vente(order="MIN")
        heure_max_vente = salemodel.get_min_max_heures_vente(order="MAX")
        heure_min_dep = salemodel.get_min_max_heures_dep(order="MIN")
        heure_max_dep = salemodel.get_min_max_heures_dep(order="MAX")

        # Vérifie que les valeurs sont valides
        if not all([heure_min_vente, heure_max_vente, heure_min_dep, heure_max_dep]):
            self.add_widget(Label(text="Aucune donnée disponible pour cette période."))
            return

        heure_min = f"{min(heure_min_vente, heure_min_dep):02d}:00:00"
        heure_max = f"{max(heure_max_vente, heure_max_dep):02d}:00:00"

        ventes = salemodel.get_heures_somme_stat(heure_min=heure_min, heure_max=heure_max)
        depense = salemodel.get_heures_depense_stat(heure_min=heure_min, heure_max=heure_max)

        if not ventes or not depense:
            self.add_widget(Label(text="Aucune donnée à afficher."))
            return

        dates_ventes = [row[0] for row in ventes]
        montants = [row[1] for row in ventes]
        depense_vals = [row[1] for row in depense]
        for i in range(20):
            for i in dates_ventes:
                print(i)

        min_len = min(len(dates_ventes), len(montants), len(depense_vals))
        if min_len == 0:
            self.add_widget(Label(text="Pas de données suffisantes pour générer le graphique."))
            return

        dates = dates_ventes[:min_len]
        montants = montants[:min_len]
        depense_vals = depense_vals[:min_len]

        fig, ax = plt.subplots(figsize=(10, 6))
        x = np.arange(min_len)
        bar_width = 0.35

        ax.bar(x - bar_width / 2, montants, width=bar_width, label='Vente', color='turquoise')
        ax.bar(x + bar_width / 2, depense_vals, width=bar_width, label='Dépense', color='mediumpurple')

        ax.set_title("Ventes vs Dépenses")
        ax.set_xlabel("Heure")
        ax.set_ylabel("Montant (Ar)")
        ax.set_xticks(x)
        ax.set_xticklabels([str(d) for d in dates], rotation=45)
        ax.legend()
        ax.grid(axis='y', linestyle="--", alpha=0.7)
        fig.tight_layout()

        self.add_widget(FigureCanvasKivyAgg(fig))


        salemodel = GestionModel()
        rows = salemodel.get_heures_somme_stat()

        heures = [datetime.strptime(str(row[0]), '%Y-%m-%d %H:%M:%S') for row in rows]
        montants = [row[1] for row in rows]

        # Grouper par tranche de 10 minutes
        donnees_par_10min = defaultdict(float)
        for heure, montant in zip(heures, montants):
            minute = (heure.minute // 10) * 10
            heure_arrondie = heure.replace(minute=minute, second=0, microsecond=0)
            donnees_par_10min[heure_arrondie] += montant

        heures_groupees = sorted(donnees_par_10min.keys())
        montant_groupes = [donnees_par_10min[h] for h in heures_groupees]

        couleurs_palette = ['#1abc9c', '#16a085']
        couleurs_alternees = [couleurs_palette[i % len(couleurs_palette)] for i in range(len(heures_groupees))]

        fig, ax = plt.subplots(figsize=(10, 5))
        bars = ax.bar(heures_groupees, montant_groupes, width=0.006, color=couleurs_alternees, edgecolor='black',
                      linewidth=0.5)

        for bar, montant in zip(bars, montant_groupes):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2.0, height + 0.5, f"{montant:.0f}", ha='center', va='bottom',
                    fontsize=9, color="#333")

        # Forcer l'affichage de 00:00 à 23:00
        if heures_groupees:
            jour = heures_groupees[0].date()
        else:
            jour = datetime.today().date()

        debut_journee = datetime.combine(jour, datetime.min.time())
        fin_journee = datetime.combine(jour, datetime.max.time()).replace(hour=23, minute=59, second=59)

        ax.set_xlim(debut_journee, fin_journee)

        # Ticks majeurs toutes les heures
        ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

        # Formatage et esthétique
        fig.autofmt_xdate()
        ax.grid(True, linestyle='--', alpha=0.4)
        fig.patch.set_facecolor("#f7f7f7")
        ax.set_facecolor('#f0f0f0')
        ax.set_ylabel("Prix ($)", fontsize=12)
        ax.set_xlabel("Heure", fontsize=12)
        plt.xticks(rotation=45)
        fig.tight_layout()

     self.add_widget(FigureCanvasKivyAgg(fig))

    def show_stat_du_jour(self):
        self.clear_widgets()

        salemodel = GestionModel()
        rows = salemodel.get_heures_stat

        heures = [datetime.strptime(str(row[0]),'%Y-%m-%d %H:%M:%S') for row in rows]
        montants = [row[1] for row in rows]
        donnees_par_heure = defaultdict(float)
        for heure,montant in zip(heures,montants):
                heure_arrondie=heure.replace(minute=0,second=0,microsecond=0)
                donnees_par_heure[heure_arrondie] +=montant
        heures_groupees = sorted(donnees_par_heure.keys())
        montant_groupes = [donnees_par_heure[h] for h in heures_groupees]

        couleurs_palette = ['#1abc9c','#16a085']
        couleurs_alternees = [couleurs_palette[i %len(couleurs_palette)] for i in range(len(heures_groupees))]


        fig, ax = plt.subplots(figsize=(10,5))
        bars = ax.bar(heures_groupees, montant_groupes, width=0.035, color=couleurs_alternees,edgecolor='black',linewidth=0.5)

        for bar,montant in zip(bars,montant_groupes):
            height=bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2.0, height +0.5 , f"{montant:.0f}", ha='center',va='bottom',fontsize=9,color="#333")



        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
        fig.autofmt_xdate()
        ax.grid(True,linestyle='--',alpha=0.4)
        fig.patch.set_facecolor("#f7f7f7")
        ax.set_facecolor('#f0f0f0')
        #ax.set_title("Shopify Inc", fontsize=16)
        ax.set_ylabel("Prix ($)", fontsize=12)
        ax.set_xlabel("Date", fontsize=12)
        plt.xticks(rotation=45)
        fig.tight_layout()


        self.add_widget(FigureCanvasKivyAgg(fig))"""
######### fin pour le show_state_du_jour#####################