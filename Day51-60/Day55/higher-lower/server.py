from flask import Flask
import random

app = Flask(__name__)

correct_num = random.randint(0,9)

# homepage
@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route("/<int:number>")
def user_number(number):
    if number < correct_num:
        return "<h1>Too low</h1><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif number > correct_num:
        return "<h1>Too high</h1><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return "<h1>You got it!</h1><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"

if __name__ == "__main__":
    #turn on debugger mode to avoid start and stop program
    app.run(debug=True)