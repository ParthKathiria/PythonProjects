#Tester File

#importing the Flight class
from Flight import *
#importing the Airport class
from Airport import *
#allAirports list is created which is initially empty.
allAirports = []
#allFlights dictionary is created which is initially empty.
allFlights = {}

#loadData function defined with airportFile (airport.txt) and flightFile(flights.txt) as paramenets.
def loadData(airportFile,flightFile):
    #try statement which tries to execute the code indented in it, if it is able to execute, it returns True
    try:
        #opening airports.txt in read mode
        infile = open(airportFile,"r")
        #for statement reading and striping spaces and spliting through ','s for every line
        for line in infile:
            x = line.strip().split(",")
            #stripping extra spaces for every word in the line
            for i in range(len(x)):
                x[i] = x[i].strip()
            #appending different indexes (code,city,country) of the stripped list(x) to our empty allAirports list.
            allAirports.append(Airport(x[0],x[2],x[1]))

        #opening flights.txt in read mode
        infile2 = open(flightFile, "r")
        #for statement reading every line in the file
        for line in infile2:
            #initially empty flightList list
            flightList = []
            x = line.strip().split(",")
            for i in range(len(x)):
                x[i] = x[i].strip()
            openfile = open(flightFile,"r")
            for linez in openfile:
                #stripping spaces and splitting through the ',' for every line in flights.txt
                cut = linez.strip().split(",")
                for i in range(len(cut)):
                    cut[i] = cut[i].strip()
                #if statement checking if both of the sides of the equality are equal, which will always be.
                if cut[1] == x[1]:
                    #opening airports.txt in read mode.
                    openair = open(airportFile,"r")
                    #reads and strips spaces and splits through the ',' for airports.txt file.
                    for lines in openair:
                        cutter = lines.strip().split(",")
                        for i in range(len(cutter)):
                            cutter[i] = cutter[i].strip()
                        #checks if city (0th index in cutter list) from airports.txt is equal to origin city at index 1 in cut list from flights.txt.
                        if cut[1] == cutter[0]:
                            #country is set to index 1 & city to index 2 in cutter list for airports.txt
                            country = cutter[1]
                            city = cutter[2]
                        #checks if city (0th index in cutter list) from airports.txt is equal to destination city at index 2 in cut list from flights.txt.
                        if cut[2] == cutter[0]:
                            #destination country & city set to index 1 & 2 respectively for airports.txt.
                            countryReach = cutter[1]
                            cityReach = cutter[2]
                    #appending as per the format using the classes Flight and Airport to flightList list.
                    flightList.append(Flight(cut[0],Airport(cut[1],city,country),Airport(cut[2],cityReach,countryReach)))
            #assigning values to allFlights dictionary.
            allFlights[x[1]] = flightList
        return True
    #in case of any exception caused, it returns the value False.
    except Exception:
        return False

#getAirportByCode function defined with 'code' as the parameter.
def getAirportByCode(code):
    #opens airports.txt in read mode.
    infile = open("airports.txt","r")
    #assigns the variably y intially with value 0, variable created for further code, if no airport is found.
    y = 0
    for line in infile:
        x = line.strip().split(",")
        for i in range(len(x)):
            x[i] = x[i].strip()
        #if index position 0 of stripped and splitted list x is code.
        if x[0] == code:
            #y is changed to value 1 and Airport class is returned in desired manner (code(city,country)).
            y = 1
            return Airport(x[0],x[2],x[1])
    #if y is still 0, the value -1 is returned.
    if y == 0:
        return -1

#findAllCityFlights function defined with 'city' as parameter.
def findAllCityFlights(city):
    #intially empty cityflights list.
    cityflights = []
    infile = open("airports.txt","r")
    infile2 = open("flights.txt","r")
    #intially empty country and citycode variables
    country = ""
    citycode = ""

    for line in infile:
        xo = line.strip().split(",")
        for i in range(len(xo)):
            xo[i] = xo[i].strip()
        #previously explained
        if xo[2] == city:
            country = xo[1]
            citycode = xo[0]
    #closes the file airports.txt to avoid errors.
    infile.close()

    for line in infile2:
        x = line.strip().split(",")
        for i in range(len(x)):
            x[i] = x[i].strip()
        #if index positions 1 and 2 of stripped and splitted are equal to citycode from airports.txt.
        if x[1] == citycode or x[2] == citycode:
            #cityflights is appended the following values using Flight and Airport function.
            cityflights.append(Flight(x[0],Airport(x[1],citycode,country),Airport(x[2],citycode,country)))
    #returns cityflights list
    return cityflights

#findAllCountryFlights function defined with country as the parameter.
#similar code as the previous function but this is for the countries with just change in index positions.
def findAllCountryFlights(country):
    #empty countryflights, codesas the list and city,countrycode as empty variables.
    countryflights = []
    infile = open("airports.txt","r")
    infile2 = open("flights.txt","r")
    city = ""
    countrycode = ""
    codes = []

    for line in infile:
        xo = line.strip().split(",")
        for i in range(len(xo)):
            xo[i] = xo[i].strip()
        if xo[1] == country:
            city = xo[2]
            countrycode = xo[0]
            #appends the countrycode string to the codes list
            codes.append(countrycode)
    infile.close()

    for line in infile2:
        x = line.strip().split(",")
        for i in range(len(x)):
            x[i] = x[i].strip()
        for code in codes:
            #if any code from codes list is equal to splitted and stripped x lists 1st or 2nd index.
           if code == x[1] or code == x[2]:
               #appends as desired in the question to countryflights list
               countryflights.append(Flight(x[0],Airport(x[1],city,country),Airport(x[2],city,country)))
    #returns the list countryflights
    return countryflights

#findFlightBetween function defined with origAirport and destAirport as the parameters.
def findFlightBetween(origAirport,destAirport):
    #uses function getCode() from Airport.py to get codes for origin and destination variable
    origin = origAirport.getCode()
    destination = destAirport.getCode()
    infile2 = open("flights.txt","r")
    for line in infile2:
        x = line.strip().split(",")
        for i in range(len(x)):
            x[i] = x[i].strip()
        #if 1st and 2nd index of list x is origin or destination
        if x[1] == origin and x[2] == destination:
            #returns the following string.
            return f"Direct Flight: {origin} to {destination}"

    infile2 = open("flights.txt","r")
    #creates an empty set names flightset
    flightset = set()
    for line in infile2:
        x = line.strip().split(",")
        for i in range(len(x)):
            x[i] = x[i].strip()
        #if origin is equal to the index position 1 of the list x, opens flights.txt, strips and splits it.
        if origin == x[1]:
            infile2 = open("flights.txt","r")
            for lines in infile2:
                z = lines.strip().split(",")
                #strips extra spaces for every word in the list z
                for i in range(len(z)):
                    z[i] = z[i].strip()
                #if the following are equal, adds x[2] to the set flightset
                if destination == z[2] and z[1] == x[2]:
                    flightset.add(x[2])
    #if length of flightset is more than 0, which it should be, it returns the flightset
    if len(flightset) > 0:
        return flightset
    #otherwise it returns the value -1
    else:
        return -1

#function findReturnFlight defined with parameter firstFlight
def findReturnFlight(firstFlight):
    #uses getOrigin() and getDestination() functions from Flight.py and getCode() function from Airport.py.
    dest = firstFlight.getOrigin().getCode()
    orig = firstFlight.getDestination().getCode()
    infile = open("flights.txt","r")
    #similar stripping and splitting and equalizing values as in the previous functions
    for line in infile:
        xo = line.strip().split(",")
        for i in range(len(xo)):
            xo[i] = xo[i].strip()
        if orig == xo[1] and dest == xo[2]:
            infile2 = open("airports.txt","r")
            for line2 in infile2:
                yo = line2.strip().split(",")
                for j in range(len(yo)):
                    yo[j] = yo[j].strip()
                if yo[0] == orig:
                    corig = yo[1]
                    ciorig = yo[2]
                if yo[0] == dest:
                    cdest = yo[1]
                    cidest = yo[2]
            #returns the following
            return Flight(xo[0],Airport(orig,ciorig,corig),Airport(dest,cidest,cdest))
    #else returns -1
    return -1
