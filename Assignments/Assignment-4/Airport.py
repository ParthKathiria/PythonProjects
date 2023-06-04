#A class named Airport is defined.
class Airport:
    #init constructor method is defined with self, code,city and country as its parameters.
    def __init__(self, code, city, country):
        self._code = code
        self._city = city
        self._country = country
    #repr function which represents the printable representation of the given object.
    def __repr__(self):
        return f"{self._code}({self._city},{self._country})"
    #getter statement which returns/gets the code.
    def getCode(self):
        return self._code
    #getter statement which returns/gets the city.
    def getCity(self):
        return self._city

    #getter statement which returns/gets the country.
    def getCountry(self):
        return self._country

    #setter statement which sets the value of city parameter to city value.
    def setCity(self, city):
        self._city = city

    #setter statement which sets the value of country parameter to country value.
    def setCountry(self, country):
        self._country = country