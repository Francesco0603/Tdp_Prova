from database.DB_connect import DBConnect
from model.classificazioni import Classificazione


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getClassif():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
from classification c """

        cursor.execute(query)

        for row in cursor:
            result.append(Classificazione(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getLocaliz():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """
select distinct c.Localization as l
from classification c """

        cursor.execute(query)

        for row in cursor:
            result.append(row["l"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getInteraz():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """
select c1.Localization as l1,c2.Localization as l2, count(distinct i.`Type`) as peso
from classification c1, interactions i, classification c2
where ((i.GeneID1 = c2.GeneID and i.GeneID2 = c1.GeneID) or (i.GeneID2 = c2.GeneID and i.GeneID1 = c1.GeneID))
and c2.Localization > c1.Localization and c2.GeneID <> c1.GeneID  
group by c1.Localization,c2.Localization"""

        cursor.execute(query)

        for row in cursor:
            result.append((row["l1"],row["l2"],row["peso"]))

        cursor.close()
        conn.close()
        return result



