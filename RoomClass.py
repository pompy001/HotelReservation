# Room Class
from CalendarClass import Calendar

class Room():
    
    reservedStatus = {}
    #Available Room
    reservedStatus['1'] = 1
    #Reserved room
    reservedStatus['2'] = 0
    
    def __init__(self,suite,n):
        
        self.suiteType = suite
        self.status = Room.reservedStatus['1']
        self.roomCal = Calendar(n)
        self.rFlag = 0
        self.rangeStart = None
        self.rangeEnd = None
        self.bookFlag = 0
        
        #Set price based on suite type (S or D or E)
        if self.suiteType == 'S':
            self.price = 100
        elif self.suiteType == 'D':
            self.price = 200
        elif self.suiteType == 'E':
            self.price = 300
    
    def returnRoomCalendar(self):
        return self.roomCal.returnAllbookingDays()

    def returnRoomCalendarRange(self):
        return self.roomCal.returnAvailableDateRange()
    
    def returnRoomPrice(self):
        return self.price
    
    def bookCustomer(self,ID):
            for i in range(self.rangeStart,self.rangeEnd):
                self.roomCal.returnAllbookingDays()[i][1]=ID

    def checkReservationDates(self,chkInDate,chkOutDate):
        #Re-initialize at the start
        self.rFlag = 0
        self.rangeStart = None
        self.rangeEnd = None
        #list comprehension to get only all the dates in the list (remove the ID section)
        datesOnly = [date[0] for date in self.roomCal.returnAllbookingDays()]
        #check if the customer's check in and out dates fall within the range
        for i in range (len(datesOnly)):
            if datesOnly[i] == chkInDate:
                self.rangeStart = i
            elif datesOnly[i] == chkOutDate:
                self.rangeEnd = i
        if (self.rangeStart and self.rangeEnd)!=None:
            #now check if the room is available for the date range (all values should be 'none')
            idOnly = [days[1] for days in self.roomCal.returnAllbookingDays()[self.rangeStart:self.rangeEnd]]
            result = all(elem == 'none' for elem in idOnly)
            if result:
                self.status = Room.reservedStatus['1']  
                self.rFlag = 1
            else:
                self.status = Room.reservedStatus['2']
                self.rFlag = 0
        else:
            print('Dates out of range or invalid values')
            self.rFlag = 0
        return self.rFlag, self.status
    
    def cancelBookingByID(self,ID):
        for i in range(0,len(self.roomCal.returnAllbookingDays())):
            if self.roomCal.returnAllbookingDays()[i][1]==ID:
                self.roomCal.returnAllbookingDays()[i][1] = 'none'