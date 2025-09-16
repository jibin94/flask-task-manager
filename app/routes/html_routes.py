from flask import Blueprint, render_template, request, redirect, url_for
from ..models import Task
from ..extensions import db

html_bp = Blueprint("html", __name__)

@html_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        content = request.form.get("content", "").strip()
        is_done = bool(request.form.get("is_done"))
        if not content:
            return "Task content cannot be empty", 400
        task = Task(content=content, is_done=is_done)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("html.index"))

    tasks = Task.query.order_by(Task.date_created.desc()).all()
    return render_template("index.html", tasks=tasks)

@html_bp.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    task = Task.query.get_or_404(id)
    if request.method == "POST":
        task.content = request.form.get("content", "").strip()
        task.is_done = bool(request.form.get("is_done"))
        db.session.commit()
        return redirect(url_for("html.index"))
    return render_template("update.html", task=task)

@html_bp.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("html.index"))
