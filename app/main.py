
from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(
    title="DevOps Task Manager API",
    description="A hands-on DevOps capstone application",
    version="1.0.0"
)

tasks = [
    {
        "id": 1,
        "title": "Learn Docker",
        "completed": False
    },
    {
        "id": 2,
        "title": "Build Jenkins Pipeline",
        "completed": False
    }
]

@app.get("/")
def root():
    return {
        "message": "DevOps Capstone API is running",
        "version": "1.0.0"
    }

@app.get("/info")
def get_info():
    return {
        "application": "DevOps Demo API",
        "environment": "development",
        "version": "1.0.0"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


@app.get("/users")
def get_users():
    return [
        {"id": 1, "name": "Joseph"},
        {"id": 2, "name": "DevOps Engineer"}
    ]


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks")
def create_task(task: dict):
    new_task = {
        "id": len(tasks) + 1,
        "title": task["title"],
        "completed": False
    }

    tasks.append(new_task)

    return new_task