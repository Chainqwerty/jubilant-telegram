from fastapi import FastAPI
from app.pow import generate_task, verify_solution
from app.miniapp import router as miniapp_router


app = FastAPI()

app.include_router(miniapp_router)

@app.get("/")
def read_root():
    return {"message": "BitHash Backend работает!"}

@app.get("/task")
def get_task():
    task = generate_task(difficulty=4)
    return {"random_string": task["random_string"], "target": task["target"]}

@app.post("/solve")
def solve_task(random_string: str, solution: str, target: str):
    task = {"random_string": random_string, "target": target}
    if verify_solution(task, solution):
        return {"success": True, "message": "Решение верное!"}
    else:
        return {"success": False, "message": "Неправильное решение!"}
