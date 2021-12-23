from flask import Flask

# __name__ is essentially the current folder the file is in, so flask treats all rendering and importing of files relative to that folder
app = Flask(__name__)

DB = "calorie_tracker"