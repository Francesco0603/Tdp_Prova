from database.DB_connect import DBConnect
from model.teams import Team


class DAO():
    def __init__(self):
        pass
    @staticmethod
    def getSquadre():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from teams t
                    order by t.name """

        cursor.execute(query)

        for row in cursor:
            result.append(Team(**row))

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getGiocatori(codiceSquadra,y1,y2):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from teams t
                    order by t.name """

        cursor.execute(query,(codiceSquadra,y1,y2))

        for row in cursor:
            result.append(row["peso"])

        cursor.close()
        conn.close()
        return result


