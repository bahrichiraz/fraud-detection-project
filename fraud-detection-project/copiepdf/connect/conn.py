from mysql.connector import errors
import mysql.connector

def connexion():
    cnx = mysql.connector.connect(
        host="",
        user="",
        password="",
        database="beta_as_solutions",
        port=3306,  # Ensure it's an integer
        autocommit=True,
    )
    return cnx


def selectallquery(query):
    try:
        db = connexion()
        cursor = db.cursor()
        cursor.execute(query)
        actions = cursor.fetchall()
        sequence = cursor.column_names
        result = [dict(zip(sequence, action)) for action in actions]
        cursor.close()
        return result
    except (errors.InterfaceError, errors.OperationalError, ConnectionError) as e :
        print(str(e))


def selectquery(query):
    try:
        db = connexion()
        cursor = db.cursor()
        cursor.execute(query)
        actions = cursor.fetchone()
        sequence = cursor.column_names
        if actions :
            result = dict(zip(sequence, actions))
        else :
            result = {}
        cursor.close()
        return result
    except (errors.InterfaceError, errors.OperationalError, ConnectionError) as e :
        print(str(e))