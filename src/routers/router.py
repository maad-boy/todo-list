from flask import Blueprint, jsonify, request

from .usecase import create_user

main = Blueprint('main', __name__)

@main.route('/health')
def health():
    return jsonify({'status': 'ok'})

@main.route('/user/create')
def create_user(req: request):
    handler = create_user.get_handler()
    _req = handler.get_request(req)
    if not _req.is_valide():
        return jsonify({"message": "invalid request"}), 404
    res = handler.handle_request(_req)
    return res, 200
