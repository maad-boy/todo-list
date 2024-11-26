from flask import Blueprint, jsonify, request

from .usecase import create_user, get_all_users

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

@main.route('/user/all', methods=['GET'])
def _get_all_users():
    handler = get_all_users.get_handler()
    _req = handler.get_request(request)
    if not _req.is_valid():
        return jsonify({"message": "invalid request"}), 404
    res = handler.handle_request(_req)
    return res.to_json(), 200

@main.route('/user/data', methods=['GET'])
def _get_user_data_by_id():
    handler =  get_user_data_by_id.get_handler()
    _req = handler.get_request(request)
