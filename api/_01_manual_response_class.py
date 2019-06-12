import json
from flask import Flask, Response, request, abort
from .utils import json_response, JSON_MIME_TYPE, search_book
#import Parameters
import socket
app = Flask(__name__)

@app.route('/hit_backend',  methods=['POST'])
def user_list():
    if request.content_type != JSON_MIME_TYPE:
        error = json.dumps({'error': 'Invalid Content Type'})
        return json_response(error, 400)
    data = request.json
    username = data['username']
    target = data['target']
    resp = [{
        'pod_id': socket.gethostname(),
        'service_name': 'backend-3',
        'username': username
    }]
    response = Response(
        json.dumps(resp), status=200, mimetype=JSON_MIME_TYPE)
#    response.set_cookie("USERNAME", value=username)
    return response


@app.errorhandler(404)
def not_found(e):
    return '', 404
