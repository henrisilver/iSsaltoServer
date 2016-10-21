from flask import jsonify, request
from ocorrencia import Ocorrencia
import os
import psycopg2
import urlparse
from usuario import Usuario

INSERT_OCCURRENCE_STATEMENT = "INSERT INTO OCORRENCIA (Username, Tipo, OcorrenciaTimestamp, LocalizacaoX, LocalizacaoY, Descricao) VALUES(%s, %s, %s, %s, %s, %s);"
GET_USER_STATEMENT = "SELECT * from Usuario where Username=%s;"
GET_OCCURRENCES_STATEMENT = "SELECT * from Ocorrencia where LocalizacaoX >= %s AND LocalizacaoX <= %s AND LocalizacaoY >= %s AND LocalizacaoY <= %s;"

# Class providing database management tools
class dbmanager():
    def __init__(self):

        urlparse.uses_netloc.append("postgres")
        url = urlparse.urlparse(os.environ["DB_URL"])
        self.conn = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )

        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    def insertOccurrence(self, request):
        occurrence = Ocorrencia(request)
        try:
            self.cur.execute(INSERT_OCCURRENCE_STATEMENT, occurrence.getData())
            return "Success"
        except Exception as e:
            print(e)
            return "Failed to insert occurence into table"

    def getOccurrence(self, username):
        try:
            data = (username,)
            self.cur.execute(GET_USER_STATEMENT, data)
        except Exception as e:
            print(e)
            return "Failed to fetch from table"

        userDBEntry = self.cur.fetchone()

        user = Usuario(userDBEntry)
        self.cur.execute(GET_OCCURRENCES_STATEMENT, user.getSearchAreaTuple())

        rows = self.cur.fetchall()

        result = {}
        for idx, row in enumerate(rows):
            rowDict = {}
            rowDict["id"] = row[0]
            rowDict["username"] = row[1]
            rowDict["type"] = row[2]
            rowDict["timestamp"] = row[3]
            rowDict["posx"] = row[4]
            rowDict["posy"] = row[5]
            rowDict["description"] = row[6]
            result[str(idx)] = rowDict
        return jsonify(**result)











