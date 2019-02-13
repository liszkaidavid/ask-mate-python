from flask import Flask, render_template, request, redirect, url_for
import data_manager
# todo: let's TODO!


app = Flask(__name__)

placeholder_path = "sample_data/question.csv"
answer_path = 'sample_data/answer.csv'

@app.route('/')
@app.route("/list")
def home_page():
    placeholder_path = "sample_data/question.csv"
    database = data_manager.read_to_dict(placeholder_path)
    for title in database["headers"]:
        pass
    return render_template("list.html", db=database)


# Todo : route - /question/<question_id>
@app.route("/question/")
def question_by_id():
    id = request.args.get('id', type=int)
    answers = data_manager.read_to_dict(answer_path)
    selected_data = data_manager.read_to_dict(placeholder_path)["rows"][id]
    passable_list = []
    for ans in answers["rows"]:
        if ans["id"] == str(id):
            passable_list.append(ans)
    return render_template("display-question.html", selected_data=selected_data, passable_list=passable_list)


# Todo : route - /add-question #1
@app.route("/add-question", methods=["POST", "GET"])
def add_question():
    if request.method == "POST":
        data_manager.add_new_row()
    return render_template("add-question.html")


# Todo : route - /question/<question_id>/new_answer


# Todo : route - /list?order_by=title &order_direction=desc


# Todo : route - /question/<question_id>/edit


# Todo : route - /question/<question_id>/delete


if __name__ == '__main__':
    app.run(
        debug=True
    )
