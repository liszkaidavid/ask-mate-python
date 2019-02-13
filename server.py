from flask import Flask, render_template, request, redirect, url_for
import connection, data_manager
# todo: lets seegvcxcbncbn,vc vvb


app = Flask(__name__)


@app.route('/')
@app.route("/list")
def home_page():
    placeholder_path = "sample_data/question.csv"
    kurvaanyad = data_manager.read_to_dict(placeholder_path)
    return render_template("list.html", a_jo=kurvaanyad)


# Todo : route - /question/<question_id>
@app.route("/question/")
def question_by_id():
    return render_template("display-question/{}.html")


# Todo : route - /add-question #1
@app.route("/add-question", methods=["POST", "GET"])
def add_question():
    if request.method == "POST":
        data_manager.ad
    return render_template("add-question.html")


# Todo : route - /question/<question_id>/new_answer


# Todo : route - /list?order_by=title &order_direction=desc


# Todo : route - /question/<question_id>/edit


# Todo : route - /question/<question_id>/delete


if __name__ == '__main__':
    app.run()
