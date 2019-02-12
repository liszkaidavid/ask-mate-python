from flask import Flask, render_template, request, redirect, url_for
# todo: lets seegvcxcbncbn,vc vvb


app = Flask(__name__)


@app.route('/')
@app.route("/list")
def hello_world():
    return 'Hello World!'




if __name__ == '__main__':
    app.run()
