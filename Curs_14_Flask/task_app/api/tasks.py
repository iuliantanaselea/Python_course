from flask import Blueprint, abort, jsonify, request, Response
from repository import tasks as tasks_repo

bp = Blueprint("tasks", __name__, url_prefix="/tasks")


@bp.route("/")
def get_all():
    tasks = tasks_repo.get_tasks()
    if not tasks:
        abort(404)
    return jsonify(tasks)  # jsonify transforma din obiect de tip cod in obiect tip json


@bp.route("/", methods=["POST"])
def add_task():
    task_data = request.json
    tasks_repo.add_task(task_data)
    return Response("Ok", 201)


@bp.route("/<title>", methods=["PATCH"])
def update_task(title):
    task_data = request.json
    tasks_repo.update_task(title, task_data)
    return Response("Ok", 200)


@bp.route("/<title>", methods=["DELETE"])
def delete_task(title):
    tasks_repo.delete_task(title)
    return Response("Ok", 200)
