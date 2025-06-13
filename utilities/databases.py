import mysql.connector
from utilities.outils import Connexion as co

def to_database(query, parameters=()):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234567',
        database="gestion",
        port=3307
    )

    print("✅ Connexion réussie à MySQL !")
    c = conn.cursor()

    try:
        c.execute(query, parameters)
        query_type = query.strip().split()[0].upper()

        if query_type == 'SELECT':
            result = c.fetchall()
        else:
            conn.commit()
            result = None
    finally:
        c.close()
        conn.close()

    return result

"""
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
"""