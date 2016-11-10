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

    def getSearchAreaTuple(self):
        return (self.posX - self.searchRadius, self.posX + self.searchRadius, self.posY - self.searchRadius, self.posY + self.searchRadius,)