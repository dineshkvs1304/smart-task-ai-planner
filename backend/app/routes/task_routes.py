from flask import Blueprint, request, jsonify
from app.services.task_service import create_task, get_all_tasks, update_task_status

task_bp = Blueprint("tasks", __name__)

@task_bp.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok", "message": "Backend running"})


@task_bp.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    result, status = create_task(data)
    return jsonify(result), status


@task_bp.route("/tasks", methods=["GET"])
def fetch_tasks():
    tasks = get_all_tasks()
    return jsonify(tasks), 200


@task_bp.route("/tasks/<int:task_id>", methods=["PUT"])
def update_status(task_id):
    data = request.json
    status_val = data.get("status", "pending")
    result, status = update_task_status(task_id, status_val)
    return jsonify(result), status