from dbmanagement import dbmanager
from flask import Flask, request
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

app = Flask(__name__)

manager = dbmanager()

@app.route('/')
def hello():
    return "This is iSsalto. Welcome. Made by iSsaltantes."

@app.route('/registrarUsuario/', methods=['POST'])
def registerUser():
    return manager.registerUser(request)

@app.route('/inserirOcorrencia/', methods=['POST'])
@auth.login_required
def insertOccurrence():
    return manager.insertOccurrence(request)
    
@app.route('/ocorrencias/e=<email>')
@auth.login_required
def getOccurrences(email):
    return manager.getOccurrences(email)

@app.route('/userinfo/e=<email>')
@auth.login_required
def getUserInfo(email):
    return manager.getUserInfo(email)
        
@app.route('/ocorrencias/x=<posx>&y=<posy>&r=<radius>')
def getOccurrencesCustom(posx, posy, radius):
    return manager.getOccurrencesCustom(float(posx), float(posy), float(radius))

# Nao esta sendo utilizado
@app.route('/token')
@auth.login_required
def getToken():
    return manager.getToken()

# TODO: integrate standard login (disabled) and Facebook login
@auth.verify_password
def login(token, unused):
    return manager.verifyFacebookLogin(token)

if __name__ == '__main__':
    app.run()







