import re, csv

from ..models.status import Status

class NumberService:
    def __init__(self, numberDao, filename=None):
        """
        Initialize number DAO and read in seed entries
        file.
        """
        self.numberDao = numberDao
        if filename is not None:
            self.__initFile(filename)

    def retrieveById(self, id):
        """
        Retrieve phone number by ID.
        """
        return self.numberDao.retrieveById(id)
    
    def searchByNumber(self, number):
        """
        Retrieve all entries with the phone number given.
        """
        if not self.__isE164Number(number):
            number = self.__toE164Format(number)
        prefix = number + '-'
        results = self.numberDao.searchByNumber(prefix)
        return results

    def create(self, entry):
        """
        Create an entry in the numbers dictionary.
        """
        entryId = self.__id(entry['number'], entry['context'])
        if self.numberDao.retrieveById(entryId) is not None:
            return Status.EXISTS

        numberEntry = self.__toEntry(entry['number'], entry['context'], entry['name'])

        self.numberDao.create(entryId, numberEntry)
        return Status.CREATED

    def __initFile(self, filename):
        print 'Reading in file ' + str(filename) + '...'
        with open(filename, 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                self.numberDao.create(self.__id(row[0], row[1]), self.__toEntry(row[0], row[1], row[2]))

        print 'Done with init file ' + str(filename) + '!'

    def __toEntry(self, number, context, name):
        """
        Convert to entry.
        """
        return {
            'number': self.__toE164Format(number),
            'context': context.lower(),
            'name': name
        }

    def __id(self, number, context):
        """
        Create ID from number and context.
        """
        return str(self.__toE164Format(number) + '-' + context.lower())

    def __isE164Number(self, number):
        """
        Check if is E164 number. Regex according to Twilio.
        """
        return re.match(r'^\+[1-9]\d{1,14}$', number)

    def __toE164Format(self, number):
        """
        Convert number to E164 format.
        """
        if self.__isE164Number(number):
            return number
        else:
            stripped = re.sub(r'[^0-9]', '', number)
            return '+' + stripped