from data_access.number_dao import NumberDao
from services.number_service import NumberService

class Dependency:
    numberDao = NumberDao()
    numberService = NumberService(numberDao, 'data_access/interview-callerid-data.csv')