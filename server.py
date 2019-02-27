from flask import Flask, render_template, request, redirect, url_for
import data_manager
import util

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def home_page():
    table_titles = [title["column_name"] for title in data_manager.get_title_names('question')]
    datas = data_manager.get_limited_questions()
    print(datas)
    return render_template("list.html", table_titles=table_titles, table_datas=datas)


@app.route("/experimental")
def experiment():
    table_titles = [title["column_name"] for title in data_manager.get_title_names('question')]
    table_data = data_manager.get_data()
    return render_template("experimental.html", table_titles=table_titles, table_datas=table_data)

#     database = data_manager.read_to_dict(placeholder_path)
#     for elem in database['rows']:
#         submission_time = elem['submission_time']
#         submission_time = util.make_timestamp_readable(int(submission_time))
#         elem['submission_time'] = submission_time
#     return render_template("list.html", db=database)
#
#
# # Todo : route - /question/<question_id>
# @app.route("/question/")
# def question_by_id():
#     id = request.args.get('id', type=int)
#     answers = data_manager.read_to_dict(answer_path)
#     selected_data = data_manager.read_to_dict(placeholder_path)["rows"][id]
#     passable_list = []
#     for ans in answers["rows"]:
#         if ans["question_id"] == str(id):
#             passable_list.append(ans)
#     return render_template("display-question.html", selected_data=selected_data, passable_list=passable_list)
#
#
# # Todo : route - /add-question #1 + image
# @app.route("/add-question", methods=["POST", "GET"])
# def add_question():
#     all = data_manager.read_to_dict(placeholder_path)
#     headers = all['headers']
#     if request.method == "POST":
#         last_id = data_manager.read_to_dict(placeholder_path)['rows'][-1]['id']
#         id = int(last_id) + 1
#         submission_time = util.make_timestamp()
#         title  = request.form['title']
#         message = request.form['message']
#         view_number, vote_number = 0, 0
#         image = ''
#         data = {}
#         form_list = [id, submission_time, view_number, vote_number,title, message, image]
#         for elem in range(len(headers)):
#             data[headers[elem]] = form_list[elem]
#         data_manager.add_new_row(placeholder_path, data, headers)
#         return redirect('/list')
#     return render_template("add-question.html", headers=headers)
#
#
# @app.route("/update/", methods=["POST", "GET"])
# def update_question():
#     if request.method == "POST":
#         data_manager.prepare_data_to_write(placeholder_path, request.form)
#         return redirect("/")
#     id = request.args.get('id', type=int)
#     selected_data = data_manager.read_to_dict(placeholder_path)
#     return render_template("edit.html", updata=selected_data["rows"][id], headers=selected_data["headers"])
#
#
# # Todo : route - /question/<question_id>/new_answer + image
# @app.route("/add-answer", methods=["POST", "GET"])
# def add_answer():
#     if request.method == "POST":
#         data_manager.add_new_row()
#     return render_template("add-answer.html")
#
# # Todo : route - /list?order_by=title &order_direction=desc
# @app.route("/list")
# def order_by_title():
#     order = request.args.get('order_by')
#     direction = request.args.get('direction')
#     return None
#
#
# # Todo : route - /question/<question_id>/edit
# @app.route("/question/<question_id>/edit", methods=["POST", "GET"])
# def edit_question():
#     if request.method == "post":
#         id = request.args.get('id', type=int)
#         print(id)
#         form_data = request.form
#         # data_manager.prepare_data_to_write(placeholder_path, form_data, "w")
#
#
# # Todo : route - /question/<question_id>/delete
# @app.route("/question/<question_id>/delete")
# def delete_question():
#     pass
#
#
# #todo delete answer
# @app.route('/answer/<answer_id>/delete')
# def delete_posts():
#     pass
#
#
# #todo vote answer
# @app.route('/question/<question_id>/vote-up')
# @app.route('/question/<question_id>/vote-down')
# @app.route('/vote')
# def vote_for_answer():
#     vote_data = data_manager.read_to_dict(answer_path)
#     print(vote_data["rows"][0]['vote_number'])
#     return redirect("/list")
#

if __name__ == '__main__':
    app.run()
