from flask import Flask

application = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Flask on AWS!"

if __name__ == '__main__':
    application.run(debug=True)