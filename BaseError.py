from flask_api import FlaskAPI
from flask import Flask, request, jsonify, render_template, make_response

api = FlaskAPI(__name__)

class BaseError(Exception):
    """Base Error Class"""

    def __init__(self, code=400, message='', status='', field=None):
        Exception.__init__(self)
        self.code = code
        self.message = message
        self.status = status
        self.field = field

    def to_dict(self):
        return {'code': self.code,
                'message': self.message,
                'status': self.status,
                'field': self.field, }

class NotFoundError(BaseError):
    def __init__(self,field, message='Not found'):
        BaseError.__init__(self)
        self.code = 404
        self.message = message
        self.status = 'NOT_FOUND'
        self.field = field

class FileWriteError(BaseError):
    def __init__(self,field, message='Write error'):
        BaseError.__init__(self)
        self.code = 404
        self.message = message
        self.status = 'WRITE_FAILED'
        self.field = field

class ConnectionError(BaseError):
    def __init__(self,field, message="Couldn't connect"):
        BaseError.__init__(self)
        self.code = 404
        self.message = message
        self.status = 'NO_CONNECTION'
        self.field = field

class NotAuthorizedError(BaseError):
    def __init__(self, message='Unauthorized'):
        BaseError.__init__(self)
        self.code = 401
        self.message = message
        self.status = 'NOT_AUTHORIZED'


class ValidationError(BaseError):
    def __init__(self, field, message='Invalid field'):
        BaseError.__init__(self)
        self.code = 400
        self.message = message
        self.status = 'INVALID_FIELD'
        self.field = field

class InvalidServiceError(BaseError):
    def __init__(self, field, message='Invalid field'):
        BaseError.__init__(self)
        self.code = 400
        self.message = message
        self.status = 'INVALID_SERVICE'
        self.field = field

class ServerError(BaseError):
    def __init__(self, message='Internal server error'):
        BaseError.__init__(self)
        self.code = 500
        self.message = message
        self.status = 'SERVER_ERROR'

@api.errorhandler(NotFoundError)
@api.errorhandler(NotAuthorizedError)
@api.errorhandler(ValidationError)
@api.errorhandler(InvalidServiceError)

def handle_error(error):
    code=getattr(error,'code')
    status = getattr(error, 'status')
    field = [getattr(error, 'field')]
    code = getattr(error, 'code')
    message = getattr(error, 'message')
    success = False
    return make_error(status,field,code,message,success)
    # ,code,message)


@api.errorhandler
def default_error_handler(error):
    """Returns Internal server error"""
    return error.to_dict(), getattr(error, 'code', 500)

def make_error(status,field,code,message,success):
    response = jsonify({
        'status': status,
        'code': code,
        'message': field,
        'error': message,
        'success' : success
    })
    return response







