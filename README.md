# FlaskProjects
Repo consists of Flask basics with simple projects



**// Requirements for Flask**
1. Python 3
2. VS Code
3. Virtual Environment - to avoid installing flask globally which protects from any disturbances in different versions of technologies(here flask and python)





**// Create Virtual Environment**
- command - 1: pip install virtualenv
- command - 2: python -m virtualenv venv // here virtualenv name is venv
- command - 3: Set-ExecutionPolicy unrestricted // for errors in script running // run this command in Powershell
- command - 4: .\venv\Scripts\activate.ps1 // to activate env in Powershell





**// Install Flask**

command : pip install flask

**Default Flask app Runs at http://127.0.0.1:5000**








**// static folder is at FlaskProjects\static**

files in static folder are downloaded with http://127.0.0.1:5000/static/file_name (e.g: file_name = felix.webp)

files can also be rendered using http://127.0.0.1:5000/static/file_name (e.g: file_name = test.txt)






**// templates folder is at FlaskProjects\templates**

One can render templates at route endpoints by placing html files in templates folder.
Render templates/file.html by returning render_template('file.html')



**// Number Guessing**

send a randomly generated number and guess of user to template

if guess > generated number or guess < generated number return an alert specifying guess should be smaller or larger 

if guess == generated number print a success message


**// To Do list** 

templates/index.html
1. form - to add a todo task with input fields - Todo Title, Todo Description
2. table - to view todo list

To store the todo tasks we use flask-sqlalchemy
- command : pip install flask-sqlalchemy
- run commands:
    1. python
    2. from minimal_app import db, app
    3. with app.app_context():
        db.create_all() // ensures that db.create_all() is called only when app is running

