class train:
    def __init__(self):
        self.seats = 78
        self.fare = 180

    def bookticket(self):
        self.seats -= 1

    def getStatus(self):
        print(self.seats)

    def getfareInfo(self):
        print(self.fare)

tr = train()  
tr.getfareInfo()
tr.getStatus()


