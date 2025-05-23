import os
import mysql.connector
from utilities.outils import Connexion as co

def to_database(query,parameters=()):
    conn = mysql.connector.connect(
        host=co.host,
        user=co.user,
        password=co.password,
        database='gestion')
    c = conn.cursor()
    c.execute(query,parameters)
    if query.split(' ')[0] != 'SELECT' :
        conn.commit()
        c.close()
        conn.close()
        return None
    res = c.fetchall()
    c.close()
    conn.close()
    return res

#print(to_database('SELECT * from client'))
