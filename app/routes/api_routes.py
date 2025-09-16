from flask import Blueprint, jsonify, request
from ..models import Task
from ..extensions import db

api_bp = Blueprint("api", __name__, url_prefix="/api")

@api_bp.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.order_by(Task.date_created.desc()).all()
    return jsonify([
        {"id": t.id, "content": t.content, "is_done": t.is_done, "date_created": t.date_created.isoformat()}
        for t in tasks
    ])

@api_bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json(silent=True) or {}
    if not data.get("content"):
        return jsonify({"error": "Content is required"}), 400
    task = Task(content=data["content"], is_done=data.get("is_done", False))
    db.session.add(task)
    db.session.commit()
    return jsonify({"id": task.id, "content": task.content, "is_done": task.is_done}), 201

@api_bp.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = Task.query.get_or_404(task_id)
    return jsonify({"id": task.id, "content": task.content, "is_done": task.is_done, "date_created": task.date_created.isoformat()})

@api_bp.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.get_json(silent=True) or {}
    if "content" not in data:
        return jsonify({"error": "Content is required"}), 400
    task.content = data["content"]
    task.is_done = data.get("is_done", task.is_done)
    db.session.commit()
    return jsonify({"id": task.id, "content": task.content, "is_done": task.is_done})

@api_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"})
