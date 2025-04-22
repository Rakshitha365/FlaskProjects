from flask import Flask

app = Flask(__name__)

@app.route("/") # route is to navigate to endpoints like /, /products
def hello_world():
    return "Hello, World!"

@app.route("/products")
def products():
    return "This is products page"

if __name__=="__main__":
    app.run(debug = True, port = 4000) # app will run automaticall upon saving chnages in script with debug = True # port will change the original port 5000 to desired one

# The output is seen on http://127.0.0.1:5000 