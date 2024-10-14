from flask import Blueprint, jsonify, request

from .usecase import create_user

main = Blueprint('main', __name__)

@main.route('/health')
def health():
    return jsonify({'status': 'ok'})

@main.route('/user/create', methods=['POST'])
def _create_user():
    handler = create_user.get_handler()
    _req = handler.get_request(request)
    if not _req.is_valid():
        return jsonify({"message": "invalid request"}), 404
    res = handler.handle_request(_req)
    return res.to_json(), 200
