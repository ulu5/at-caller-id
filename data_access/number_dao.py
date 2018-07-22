import re, csv

class NumberDao:
    def __init__(self):
        """
        Initialize number entries.
        """
        self.numbers = dict()

    def retrieveById(self, id):
        """
        Retrieve phone number by ID.
        """
        return self.numbers.get(id)
    
    def searchByNumber(self, numberPrefix):
        """
        Retrieve all entries with the phone number given.
        """
        return [ v for k,v in self.numbers.items() if k.startswith(numberPrefix)]

    def create(self, id, entry):
        """
        Create an entry in the numbers dictionary.
        """
        self.numbers[id] = entry