from flask import Blueprint, jsonify, request
from .usecase import create_list

todo_list = Blueprint("todo_list", __name__)


@todo_list.route('/list/create_list', methods=['POST'])
def _create_list():
    handler = create_list.get_handler()
    _req = handler.get_request(request)
    if not _req.is_valid():
        return jsonify({"message": "invalid request"}), 404
    res = handler.handle_request(_req)
    return res.to_json(), 200

@todo_list.route("/list/add_item", method=["POST"])
def add_item():
    handler = add_item.get_handler()
    _req = handler.get_request(request)
    if not _req.is_valid():
        return jsonify({"message": "invalid request"}), 404
    res = handler.handle_request(_req)
    return res.to_json(), 200