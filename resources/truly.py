from flask import Flask, Response
from flask_restplus import Resource

class Truly(Resource):
    """
    Easter egg ASCII art for Truly.
    """
    def get(self):
        with open('data_access/truly_logo.txt', 'r') as content_file:
            content = content_file.read()
        return Response(content, mimetype='text/plain')
