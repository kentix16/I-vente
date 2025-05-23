import matplotlib.pyplot as plt

import matplotlib.dates as mdates
from models.gestionModel import GestionModel

salemodel=GestionModel()
rows=salemodel.get_heures_stat
heures=[row[0] for row in rows]
somme=[valeur[1] for valeur in rows]

plt.figure(figsize=(10, 6))
plt.plot(heures, somme, color='green', linewidth=2)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=1))
plt.gcf().autofmt_xdate()

plt.title("Shopify Inc", fontsize=16)
plt.ylabel("Prix ($)", fontsize=12)
plt.xlabel("Date", fontsize=12)
plt.grid(True)

# Rotation des dates
plt.xticks(rotation=45)

# Afficher le graphique
plt.tight_layout()
plt.show()
