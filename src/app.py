from flask import Flask, request, jsonify
from models import Task

app = Flask(__name__)

tasks = []
current_id = 1

@app.route("/tasks", methods=["POST"])
def create_task():
    global current_id
    data = request.json
    title = data.get("title")
    description = data.get("description")

    if not title:
        return jsonify({"error": "Título obrigatório"}), 400

    task = Task(current_id, title, description)
    tasks.append(task)
    current_id += 1

    return jsonify({"message": "Tarefa criada com sucesso"}), 201

@app.route("/tasks", methods=["GET"])
def list_tasks():
    return jsonify([
        {"id": t.id, "title": t.title, "description": t.description}
        for t in tasks
    ])

@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    data = request.json
    for task in tasks:
        if task.id == id:
            task.title = data.get("title", task.title)
            task.description = data.get("description", task.description)
            return jsonify({"message": "Tarefa atualizada"})
    return jsonify({"error": "Tarefa não encontrada"}), 404

@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    global tasks
    tasks = [t for t in tasks if t.id != id]
    return jsonify({"message": "Tarefa removida"})

if __name__ == "__main__":
    app.run(debug=True)
