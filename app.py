from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# List to store tasks
tasks = []

# Route for the home page
@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

# Route to add a task
@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    if task:
        tasks.append(task)
    return redirect(url_for("home"))

# Route to remove a task
@app.route("/remove/<int:task_id>")
def remove_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
