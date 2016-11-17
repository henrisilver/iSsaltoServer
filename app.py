from dbmanagement import dbmanager
from flask import Flask, request

app = Flask(__name__)

manager = dbmanager()

@app.route('/')
def hello():
    return "This is iSsalto. Welcome. Made by iSsaltantes."

@app.route('/registrarUsuario/', methods=['POST'])
def registerUser():
    return manager.registerUser(request)

@app.route('/inserirOcorrencia/', methods=['POST'])
def insertOccurrence():
    return manager.insertOccurrence(request)
    
@app.route('/ocorrencias/u=<username>')
def getOccurrences(username):
    return manager.getOccurrences(username)
        
@app.route('/ocorrencias/x=<float:posx>&y=<float:posy>&r=<float:radius>')
def getOccurrencesCustom(posx, posy, radius):
    return manager.getOccurrencesCustom(posx,posy,radius)

if __name__ == '__main__':
    app.run()







