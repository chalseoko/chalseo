from flask import Flask, request
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    render_template('index.html')

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
