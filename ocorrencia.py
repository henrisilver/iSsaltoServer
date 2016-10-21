from flask import request

# Class representing an occurrence
class Ocorrencia():
    def __init__(self, request):
        self.user = request.form['username']
        self.occurrenceType = int(request.form['type'])
        self.timestamp = request.form['timestamp']
        self.posx = float(request.form['posx'])
        self.posy= float(request.form['posy'])
        self.description = request.form['description']

    def getData(self):
        return (self.user, self.occurrenceType, self.timestamp, self.posx, self.posy, self.description,)