import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from app import app

def test_create_task():
    client = app.test_client()

    response = client.post(
        "/tasks",
        data=json.dumps({"title": "Teste", "description": "Tarefa teste"}),
        content_type="application/json"
    )

    assert response.status_code == 201
