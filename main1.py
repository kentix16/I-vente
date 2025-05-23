from datetime import datetime, timedelta

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as mdates
from models.gestionModel import GestionModel

# Exemple de données (tu peux remplacer avec tes vraies données)
#dates = pd.date_range(start="2024-01-01", periods=19, )
#prices = np.cumsum(np.random.randn(100)) + 100 # Simulation de données boursières
salemodel=GestionModel()
rows=salemodel.get_heures_stat
heures=[rows[0] for row in rows]
somme=[rows[1] for valeur in rows]
#heures = [str(timedelta(minutes=30*i)) for i in range(12,17)]
#somme = [3,1,4,7,5]

# Création du graphique
plt.figure(figsize=(10, 6))
plt.plot(heures, somme, color='green', linewidth=2)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=1))
plt.gcf().autofmt_xdate()
# Ajout de titres et axes
plt.title("Shopify Inc", fontsize=16)
plt.ylabel("Prix ($)", fontsize=12)
plt.xlabel("Date", fontsize=12)
plt.grid(True)

# Rotation des dates
plt.xticks(rotation=45)

# Afficher le graphique
plt.tight_layout()
plt.show()
