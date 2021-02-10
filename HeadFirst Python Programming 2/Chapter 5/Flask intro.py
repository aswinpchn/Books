from flask import Flask

app = Flask(__name__)


@app.route('/')  # This is called route decorator. Route decorator is attached with a function next line.
def hello() -> str:
    return 'Hello world from Flask!'


app.run()
