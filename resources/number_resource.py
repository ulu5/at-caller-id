from flask import Flask, jsonify, request
from flask_restplus import Resource

import re

from ..dependency import Dependency
from ..models.number_dto import NumberDto
from ..models.status import Status

api = NumberDto.api
model = NumberDto.model
resultsModel = NumberDto.resultsModel

numberService = Dependency.numberService

@api.route('/number')
class NumberResource(Resource):
    @api.doc('Create a phone number resource')
    @api.expect(model, validate=True)
    def post(self):
        """
        Create a phone number resource for the given context if
        one does not yet exist. If it does, return a 409 CONFLICT
        and specify that a resource with the given context and number
        already exists.
        """
        status = numberService.create(api.payload)
        return self.__status_to_response(status, api.payload)

    def __status_to_response(self, status, payload):
        """
        Convert the DAO status to a proper HTTP response.
        """
        mimeType = 'application/json'
        if status == Status.CREATED:
            response = jsonify(message='Resource created')
            response.status_code = 201
            return response
        elif status == Status.EXISTS:
            response = jsonify(message='Resource already exists')
            response.status_code = 409
            return response
        response = jsonify(message='Internal server error')
        response.status_code = 500
        return response

@api.route('/query')
class QueryResource(Resource):
    @api.doc('Search for a phone number resource')
    @api.param('number', description = 'Phone number to search for',
        _in = 'query')
    @api.marshal_with(resultsModel, code=200, description='Success')
    def get(self):
        """
        Retrieve all phone number entries that match the given phone
        number query.
        """
        number = request.args.get('number')

        if number is None:
            return jsonify(error='Missing required parameter "number"'), 400

        results = numberService.searchByNumber(number)
        resources = {'results' : results}
        return resources, 200