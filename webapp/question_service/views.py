from flask import Blueprint


blueprint = Blueprint('kanal_service', __name__)

@blueprint.route('/')
def index():
    return "App Run"