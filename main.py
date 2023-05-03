from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route('/', methods=['GET'])
def page():
    name = request.args.get('name')
    message = request.args.get('message')
    return "<p>Hello " + name + "!</p><p>" + message + "!</p>"

if __name__ == "__main__":
    app.run(debug=True)