# Class representing a user
class Usuario():
    def __init__(self, userDBEntry):
        self.username = userDBEntry[0]
        self.hash = userDBEntry[1]
        self.searchRadius = float(userDBEntry[2])
    	self.posX = float(userDBEntry[3])
        self.posY = float(userDBEntry[4])

    def getSearchAreaTuple(self):
        return (self.posX - self.searchRadius, self.posX + self.searchRadius, self.posY - self.searchRadius, self.posY + self.searchRadius,)