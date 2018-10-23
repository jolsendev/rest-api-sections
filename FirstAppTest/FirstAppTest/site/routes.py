from flask import Blueprint

mod = Blueprint('api', __name__)

@mod.route('/getStuff')
def getStuff():
    return '{"result" : "Youa re in the API"}'