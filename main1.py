from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
from models.gestionModel import GestionModel

# Instancier le modèle
salemodel = GestionModel()

# Récupérer les données
rows = salemodel.get_heures_stat

# Séparer les heures et les sommes
heures = [datetime.strptime(str(row[0]), '%Y-%m-%d %H:%M:%S') for row in rows]
somme = [row[1] for row in rows]

# Création du graphique
plt.figure(figsize=(10, 6))
plt.plot(heures, somme, color='green', linewidth=2)

# Formatage de l’axe X pour les heures
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=1))
plt.gcf().autofmt_xdate()

# Ajout de titres et axes
plt.title("Statistiques journalières", fontsize=16)
plt.ylabel("Somme", fontsize=12)
plt.xlabel("Heure", fontsize=12)
plt.grid(True)
plt.xticks(rotation=45)

# Afficher le graphique
plt.tight_layout()
plt.show()
