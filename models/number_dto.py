from flask_restplus import Namespace, fields

class NumberDto:
    api = Namespace('number', description='Phone Number related operations', validate=True)

    model = api.model('PhoneNumber',
    {
        'name' : fields.String(required=True, description='The name of the entity associated with this phone number'),
        'number' : fields.String(required=True, description='The phone number'),
        'context': fields.String(required=True, description='The context of the phone number entry')
    })

    resultsModel = api.model('Results', {
        'results': fields.List(fields.Nested(model))
    })