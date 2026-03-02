from app import db, logger
from app.models.task_model import Task

def calculate_priority(title, description):
    text = f"{title} {description}".lower()

    high_keywords = ["urgent", "asap", "exam", "deadline", "interview", "submission"]
    medium_keywords = ["project", "assignment", "meeting"]

    for word in high_keywords:
        if word in text:
            return "high"

    for word in medium_keywords:
        if word in text:
            return "medium"

    return "low"


def create_task(data):
    try:
        title = data.get("title")
        description = data.get("description")

        if not title:
            return {"error": "Title is required"}, 400

        priority = calculate_priority(title, description)

        task = Task(
            title=title,
            description=description,
            priority=priority
        )

        db.session.add(task)
        db.session.commit()

        logger.info(f"Task created: {title} with priority {priority}")

        return task.to_dict(), 201

    except Exception as e:
        logger.error(str(e))
        return {"error": "Failed to create task"}, 500


def get_all_tasks():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return [t.to_dict() for t in tasks]


def update_task_status(task_id, status):
    task = Task.query.get(task_id)

    if not task:
        return {"error": "Task not found"}, 404

    task.status = status
    db.session.commit()

    logger.info(f"Task {task_id} updated to {status}")

    return task.to_dict(), 200