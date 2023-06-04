#Flight.py

#Airport class is imported
from Airport import *
#A class named 'Flight' is defined.
class Flight:
    #init constructor with flightNo, origin, destination as the parameters.
    def __init__(self, flightNo, origin, destination):
        #if origin and destination are not instances of Airport class,then raise TypeError
        if not isinstance(origin, Airport) or not isinstance(destination, Airport):
            raise TypeError("The origin and destination must be Airport objects")
        #else statement creates multiple different instances
        else:
            self._origin = origin
            self._destination = destination
            self._flightNo = flightNo
            self._cityorigin = origin.getCity()
            self._citydest = destination.getCity()
            self._countryorigin = origin.getCountry()
            self._countrydest = destination.getCountry()

    #repr function which represents the printable representation of the given object.
    def __repr__(self):
        #calls isDomesticFlight() function from the code below, if origin and destination country are same, returns the following statement.
        if self.isDomesticFlight() == True:
            return f"Flight: {self._flightNo} from {self._cityorigin} to {self._citydest} {{domestic}}"
        #else returns the following statement if origin and destination countries are different
        else:
            return f"Flight: {self._flightNo} from {self._cityorigin} to {self._citydest} {{international}}"
    #eq function which checks if both of the origin or destination codes are same, by calling the getter getCode() function from Airport class.
    def __eq__(self, other):
        #if they are equal, returns True
        if self._origin.getCode() == other._origin.getCode() and self._destination.getCode() == other._destination.getCode():
            return True
        #otherwise returns False
        else:
            return False
    #getter statement which returns flightNo
    def getFlightNumber(self):
        return self._flightNo

    #getter statement which returns origin.
    def getOrigin(self):
        return self._origin

    #getter statement which returns destination
    def getDestination(self):
        return self._destination

    #isDomesticFlight() funciton is defined which checks if origin and destination countries are same,returns True if they are, else returns False.
    def isDomesticFlight(self):
        if self._countryorigin == self._countrydest:
            return True
        else:
            return False

    #setter statement which sets the value of the origin parameter to origin value.
    def setOrigin(self, origin):
        self._origin = origin

    #setter statement which sets the value of the destination parameter to destination value.
    def setDestination(self,destination):
        self._destination = destination

