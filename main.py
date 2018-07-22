from flask import Flask
from flask_restplus import Api

from resources.number_resource import NumberResource
from resources.truly import Truly
from models.number_dto import NumberDto

app = Flask(__name__)
api = Api(app,
    title='Caller ID Service',
    version='1.0',
    description='Microservice used for looking up caller ID by phone number',
    default='truly',
    default_label='Truly ASCII art for your viewing pleasure')

api.add_namespace(NumberDto.api, '/api')
api.add_resource(Truly, '/truly')

if __name__ == '__main__':
    app.run()
