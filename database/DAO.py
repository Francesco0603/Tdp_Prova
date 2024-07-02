from database.DB_connect import DBConnect
from model.geni import Gene


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getGeniEssenziali():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
from genes g 
where g.Essential = "Essential" 
"""

        cursor.execute(query)

        for row in cursor:
            result.append(Gene(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getInteractions():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select i.GeneID1 as g1 ,i.GeneID2 as g2, abs(i.Expression_Corr) as peso 
from interactions i, genes g1, genes g2
where i.GeneID1 = g1.GeneID 
and i.GeneID2 = g2.GeneID
and i.GeneID1 != i.GeneID2"""

        cursor.execute(query)

        for row in cursor:
            result.append((row["g1"],row["g2"],row["peso"]))

        cursor.close()
        conn.close()
        return result

