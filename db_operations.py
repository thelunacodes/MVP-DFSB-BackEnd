import sqlite3

def openConnection() -> sqlite3.Connection:

    """Creates an active connection with the database.

    Returns:
        sqlite3.Connection: An active connection to the database.
    """
    conn = sqlite3.connect("games.db")

    return conn

def createGamesTable(conn:sqlite3.Connection) -> None:
    
    """Creates the "games" table (if it doesn't exist).

    Args:
        conn (sqlite3.Connection): An active connection to the database.
    """
    
    cursor = conn.cursor()
    
    with open('createGamesTable.sql', 'r') as sql_file:
        sql_script = sql_file.read()

        try:
            cursor.execute(sql_script)
            conn.commit()
        except Exception as ex:
            print(ex)
            conn.rollback()
        finally:
            cursor.close()

def executeSQL(sql:str, conn:sqlite3.Connection)-> None:
    """Runs the SQL script provided as a parameter

    Args:
        sql (str): The SQL script
        conn (sqlite3.Connection): An active connection to the database.
    """
    cursor = conn.cursor()

    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as ex:
        print(ex)
        conn.rollback()
    finally:
        cursor.close()

def executeSQLAndFetch(sql:str, conn:sqlite3.Connection):
    cursor = conn.cursor()

    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    except Exception as ex:
        print(ex)
        conn.rollback()
    finally:
        cursor.close()