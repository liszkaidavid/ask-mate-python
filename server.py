from flask import Flask, render_template, request, redirect, url_for
import connection, data_manager
# todo: lets seegvcxcbncbn,vc vvb


app = Flask(__name__)


@app.route('/')
@app.route("/list")
def home_page():
    kurvaanyad = data_manager.read_to_dict()
    for title in kurvaanyad["headers"]:
        print(title)
    return render_template("list.html", a_jo=kurvaanyad)


# Todo : route - /question/<question_id>


# Todo : route - /add-question


# Todo : route - /question/<question_id>


# Todo : route - /list?order_by=title &order_direction=desc


# Todo : route - /question/<question_id>/edit


# Todo : route - /question/<question_id>/delete


if __name__ == '__main__':
    app.run()
