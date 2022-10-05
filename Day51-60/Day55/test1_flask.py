from flask import Flask

app = Flask(__name__)

# homepage
@app.route("/")
def hello_world():
    return "Hello World!"

# creating varibale url
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}!, you are {number} years old!"


if __name__ == "__main__":
    #turn on debugger mode to avoid start and stop program
    app.run(debug=True)