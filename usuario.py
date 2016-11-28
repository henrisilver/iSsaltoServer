from flask import request
from passlib.apps import custom_app_context as pwd_context

# Class representing a user
class Usuario():
    def __init__(self, userData):
        self.email = userData[0]
        self.username = userData[1]
        self.hash = userData[2]
        self.searchRadius = float(userData[3])
    	self.posX = float(userData[4])
        self.posY = float(userData[5])

    def verifyPassword(self, password):
        return pwd_context.verify(password, self.hash)

    @classmethod
    def fromUserDBEntry(cls, userDBEntry):
        return  cls(userDBEntry)

    @classmethod
    def fromRegisterUser(cls, request):
        userData = []
        userData.append(request.form['email'])
        userData.append(request.form['username'])
        userData.append(pwd_context.encrypt(request.form['hash']))
        userData.append(float(request.form['searchradius']))
        userData.append(float(request.form['posx']))
        userData.append(float(request.form['posy']))

        return  cls(userData)

    @classmethod
    def fromFacebookUser(cls, email, username):
        userData = []
        userData.append(email)
        userData.append(username)
        userData.append("") # nao ha hash/senha para dados do facebook. Login feito pela APi do Facebook
        userData.append(10.0) # raio de busca padrao
        userData.append(-22.0058591669393) # posX padrao (Sao Carlos)
        userData.append(-47.8975900635123) # posY padrao (Sao Carlos)

        return  cls(userData)

    def getSearchAreaTuple(self):
        return (self.posX , self.posX , self.posY, self.posY, self.searchRadius**2)

    def getData(self):
        return (self.email, self.username, self.hash, self.searchRadius, self.posX, self.posY,)

    def updateData(self):
        return (self.searchRadius, self.posX, self.posY, self.email,)

    def getDataFacebook(self):
        return (self.email, self.username, self.searchRadius, self.posX, self.posY,)