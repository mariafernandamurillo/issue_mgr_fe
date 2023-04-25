from flask import Flask, render_template
from datetime   import datetime
import requests

app = Flask(__name__)
BACKEND_URL="http://127.0.0.1:5000"

@app.get("/")
def index():
    timestamp = datetime.now().strftime("%F %H:%M:%S")
    return render_template("index.html", ts=timestamp)

@app.get("/about")
def about_me():
    me = {
        "first_name": "Fernanda",
        "last_name": "Murillo",
        "hobbies": "Something",
    }
    return render_template("about.html", about=me)

@app.get("/tasks")
def display_all_tasks():
    url = "%s/%s" % (BACKEND_URL, "tasks")
    resp = requests.get(url)
    if resp.status_code==200:
        task_data = resp.json()
        return render_template("task_list.html", tasks=task_data["tasks"])
    return render_template("error.html", err_code=resp.status_code), resp.status_code