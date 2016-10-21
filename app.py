from dbmanagement import dbmanager
from flask import Flask, request

app = Flask(__name__)

manager = dbmanager()

@app.route('/')
def hello():
    return "This is iSsalto. Welcome. Made by iSsaltantes."

@app.route('/inserirOcorrencia/', methods=['POST'])
def insertOccurrence():
    return manager.insertOccurrence(request)
    
        
@app.route('/ocorrencias/u=<username>')
def getOccurrences(username):
    return manager.getOccurrence(username)

if __name__ == '__main__':
    app.run()







