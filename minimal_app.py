from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} -> {self.title}"
    



@app.route("/", methods=['GET', 'POST']) # route is to navigate to endpoints like /, /products
def hello_world():
    if request.method == "POST":
        todo_title = request.form["title"]
        todo_desc = request.form["desc"]
        todo = Todo(title=todo_title, desc=todo_desc)
        db.session.add(todo)
        db.session.commit()
    allTodo = Todo.query.all()
    return render_template('index.html', allTodo = allTodo)

@app.route("/sample")
def sample():
    return render_template('test.html') # render templates using render_template

@app.route("/show")
def products():
    allTodo = Todo.query.all()
    print(allTodo)
    return "This is products page"

if __name__=="__main__":
    app.run(debug = True, port = 4000) # app will run automaticall upon saving chnages in script with debug = True # port will change the original port 5000 to desired one

# The output is seen on http://127.0.0.1:5000 