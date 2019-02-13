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
    return render_template("list.html", db=database)


# Todo : route - /question/<question_id>
@app.route("/question/")
def question_by_id():
    id = request.args.get('id', type=int)
    answers = data_manager.read_to_dict(answer_path)
    selected_data = data_manager.read_to_dict(placeholder_path)["rows"][id]
    passable_list = []
    for ans in answers["rows"]:
        if ans["question_id"] == str(id):
            passable_list.append(ans)
    return render_template("display-question.html", selected_data=selected_data, passable_list=passable_list)


# Todo : route - /add-question #1 + image
@app.route("/add-question", methods=["POST", "GET"])
def add_question():
    all = data_manager.read_to_dict(placeholder_path)
    headers = all['headers']
    if request.method == "POST":
        data_manager.add_new_row()
    return render_template("add-question.html", headers=headers)


@app.route("/update/", methods=["POST", "GET"])
def update_question():
    if request.method == "POST":
        data_manager.prepare_data_to_write(placeholder_path, request.form)
        return redirect("/")
    id = request.args.get('id', type=int)
    selected_data = data_manager.read_to_dict(placeholder_path)
    return render_template("edit.html", updata=selected_data["rows"][id], headers=selected_data["headers"])


# Todo : route - /question/<question_id>/new_answer + image
@app.route("/add-answer", methods=["POST", "GET"])
def add_answer():
    if request.method == "POST":
        data_manager.add_new_row()
    return render_template("add-answer.html")

# Todo : route - /list?order_by=title &order_direction=desc
@app.route("/list")
def order_by_title():
    order = request.args.get('order_by')
    direction = request.args.get('direction')
    return None


# Todo : route - /question/<question_id>/edit
@app.route("/question/<question_id>/edit", methods=["POST", "GET"])
def edit_question():
    if request.method == "post":
        id = request.args.get('id', type=int)
        print(id)
        form_data = request.form
        # data_manager.prepare_data_to_write(placeholder_path, form_data, "w")


# Todo : route - /question/<question_id>/delete
@app.route("/question/<question_id>/delete")
def delete_question():
    pass


#todo delete answer
@app.route('/answer/<answer_id>/delete')
def delete_posts():
    pass


#todo vote answer
@app.route('/question/<question_id>/vote-up')
@app.route('/question/<question_id>/vote-down')
def vote_for_answer():
    pass



if __name__ == '__main__':
    app.run()
