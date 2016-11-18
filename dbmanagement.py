from flask import jsonify, request, abort, g
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from ocorrencia import Ocorrencia
import os
import psycopg2
import requests
import urlparse
from usuario import Usuario

INSERT_OCCURRENCE_STATEMENT = "INSERT INTO OCORRENCIA (Email, Tipo, OcorrenciaTimestamp, LocalizacaoX, LocalizacaoY, Descricao) VALUES(%s, %s, %s, %s, %s, %s);"
INSERT_USER_FACEBOOK_STATEMENT = "INSERT INTO Usuario (Email, Username, RaioDeBusca, PosX, PosY) VALUES(%s, %s, %s, %s, %s);"
INSERT_USER_STATEMENT = "INSERT INTO Usuario (Email, Username, Hash, RaioDeBusca, PosX, PosY) VALUES(%s, %s, %s, %s, %s, %s);"
GET_USER_STATEMENT = "SELECT * from Usuario where Email=%s;"
GET_OCCURRENCES_STATEMENT = "SELECT * from Ocorrencia where ((LocalizacaoX-%s)*(LocalizacaoX-%s)+(LocalizacaoX-%s)*(LocalizacaoX-%s)) <= %s;"

SECRET_KEY = "Giuka maioral, Giuka sedutor. Que belo peitoral, Giuka meu amor"

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

    def registerUser(self, request):
        user = Usuario.fromRegisterUser(request)

        try:
            data = (user.email,)
            self.cur.execute(GET_USER_STATEMENT, data)
        except Exception as e:
            print(e)
            return "Failed to fetch from table"

        if self.cur.fetchone() is None:
            try:
                self.cur.execute(INSERT_USER_STATEMENT, user.getData())
                return "Success"
            except Exception as e:
                print(e)
                return "Failed to insert user into table"
        else:
            return "Invalid username! Existing user"
        

    def parseOccurrences(self, rows):
        result = {}
        for idx, row in enumerate(rows):
            rowDict = {}
            rowDict["id"] = row[0]
            rowDict["email"] = row[1]
            rowDict["type"] = row[2]
            rowDict["timestamp"] = row[3]
            rowDict["posx"] = row[4]
            rowDict["posy"] = row[5]
            rowDict["description"] = row[6]
            result[str(idx)] = rowDict
        return jsonify(**result)

    def fetchUser(self, email):
        try:
            data = (email,)
            self.cur.execute(GET_USER_STATEMENT, data)
        except Exception as e:
            print(e)
            return "Failed to fetch from table"

        userDBEntry = self.cur.fetchone()
        
        if userDBEntry is None:
            return None

        user = Usuario.fromUserDBEntry(userDBEntry)

        return user

    def getOccurrences(self, email):

        user = self.fetchUser(email)
        if user is None:
            return "There is no user with such an email."

        self.cur.execute(GET_OCCURRENCES_STATEMENT, user.getSearchAreaTuple())

        rows = self.cur.fetchall()

        return self.parseOccurrences(rows)

    def getOccurrencesCustom(self, posx, posy, radius):
        self.cur.execute(GET_OCCURRENCES_STATEMENT, (posx, posx, posy, posy, radius**2,))

        rows = self.cur.fetchall()

        return self.parseOccurrences(rows)

    # For standard login
    def generateAuthToken(self, email):
        s = Serializer(SECRET_KEY, expires_in=60)
        return s.dumps({'email': email})

    # For standard login
    def getToken(self):
        token = self.generateAuthToken(g.user.email)
        return jsonify({'token': token.decode('ascii'), 'duration': 60})

    # For standard login
    def verifyAuthToken(self, token):
        s = Serializer(SECRET_KEY)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None    # valid token, but expired
        except BadSignature:
            return None    # invalid token

        user = self.fetchUser(data['email'])
        
        return user

    # For standard login
    def verifyPassword(self, username_or_token, password):
        # first try to authenticate by token
        user = self.verifyAuthToken(username_or_token)
        if not user:
            # try to authenticate with username/password
            user = self.fetchUser(username_or_token)
            if not user or not user.verifyPassword(password):
                # print str(password)
                return False
        g.user = user
        return True

    def verifyFacebookLogin(self, token):
        r = requests.get('https://graph.facebook.com/me?fields=name,email&access_token=' + str(token))
        if r.status_code != 200:
            return False
        data = r.json()
        username = data['name']
        email = data['email']

        user = self.fetchUser(email)

        if user is None:
            user = Usuario.fromFacebookUser(email, username)
            self.cur.execute(INSERT_USER_FACEBOOK_STATEMENT, user.getDataFacebook())
        return True

    def getUserInfo(self, email):
        user = self.fetchUser(email)

        if user is None:
            return "No user with the specified email."
        
        return jsonify({'username': user.username, 'email': user.email, 'searchradius': user.searchRadius, 'posx': user.posX, 'posy': user.posY})








