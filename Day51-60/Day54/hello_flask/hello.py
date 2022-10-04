from flask import Flask

# name is a special attribute in python, what is the current class, function, method, descriptor or generator instance
# if __name__ == "__main__" that means this script itself is run
app = Flask(__name__)

# / here means the homepage
# @ - python decorator : add some functionality to existing function. Functions can be passed as args, nested inside other funcs and returned 
@app.route("/")
def hello_world():
    return "Hello World!"

# this decorator indicates that app if visitor visits /bye webpage then execute following function
@app.route("/bye")
def say_bye():
    return "Bye!"

if __name__ == "__main__":
    app.run()

# tutorial on decorators

# import time

# def delay_decorator(function):
#     # this is a nested function
#     def wrapper_function():
#         # this is the additional functionality
#         time.sleep(2)
#         # this executes the function that was included in argument
#         function()
#     return wrapper_function

# @delay_decorator
# def say_hello():
#     print("Hello")

# @delay_decorator
# def say_bye():
#     print("Bye")

# @delay_decorator
# def say_greeting():
#     print("Hello")

# say_hello()
# say_bye()
# say_greeting()
