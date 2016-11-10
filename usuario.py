from flask import request

# Class representing a user
class Usuario():
    def __init__(self, userData):
        self.username = userData[0]
        self.hash = userData[1]
        self.searchRadius = float(userData[2])
    	self.posX = float(userData[3])
        self.posY = float(userData[4])

    @classmethod
    def fromUserDBEntry(cls, userDBEntry):
        return  cls(userDBEntry)

    @classmethod
    def fromRegisterUser(cls, request):
        userData = []
        userData.append(request.form['username'])
        userData.append(request.form['hash'])
        userData.append(float(request.form['searchradius'])
        userData.append(float(request.form['posx']))
        userData.append(float(request.form['posy']))

        return  cls(userData)

    def getSearchAreaTuple(self):
        return (self.posX - self.searchRadius, self.posX + self.searchRadius, self.posY - self.searchRadius, self.posY + self.searchRadius,)

    def getData(self):
        return (self.username, self.hash, self.searchRadius, self.posX, self.posY,)