from flask import Flask, render_template, request, redirect, url_for
import data_manager
import util

app = Flask(__name__)


@app.route('/')
def home_page():
    table_titles = util.get_table_titles('question')
    datas = data_manager.get_limited_questions()
    return render_template("list.html",
                           table_titles=table_titles,
                           table_datas=datas)


@app.route("/list")
def list():
    table_titles = util.get_table_titles('question')
    table_data = data_manager.get_data()
    return render_template("list.html",
                           table_titles=table_titles,
                           table_datas=table_data)


@app.route("/display-question/<question_id>")
def display_question(id):
    table_data = data_manager.get_data()
    selected_data = table_data[int(id)]
    answers = data_manager.get_answers()
    print('ezis?')
    return render_template("display-question.html",
                           selected_data=selected_data,
                           passable_list=answers)


@app.route("/display/<type>/<id>")
def display(type, id):
    table_data = data_manager.get_data()
    if type == "question":
        exceptions = ['id', 'question_id']
        selected_data = table_data[int(id)]
        answers = data_manager.get_answers_for_question(id)
        return render_template("display-question.html",
                               selected_data=selected_data,
                               passable_list=answers,
                               question_id=id,
                               exceptions=exceptions,
                               table_title=util.get_table_titles(type))
    elif type == "answer":
        selected_data = table_data[int(id)]
        answers = data_manager.get_answers()
        return render_template("display-answer.html",
                               selected_data=selected_data,
                               passable_list=answers)
    elif type == "comment":
        selected_data = table_data[int(id)]
        answers = data_manager.get_answers()
        return render_template("display-comment.html",
                               selected_data=selected_data,
                               passable_list=answers)
    return redirect('/')


@app.route("/add/<type>/<id>", methods=["POST", "GET"])
def add(type, id):
    table_data = data_manager.get_data()
    selected_data = table_data[int(id)]
    if type == "question":
        if request.method == 'POST':
            question_title = request.form.get('title')
            question = request.form.get('message')
            datas = {'view_number': 0,
                    'vote_number': 0,
                    'title': question_title,
                    'message': question,
                    'image': ''}
            #submission_time//, view_number, vote_number, title, message, image
            data_manager.insert_into_question(datas)
            return redirect('/')
        return render_template('add-question.html')
    elif type == "answer":
        if request.method == 'POST':
            answer = request.form.get('message')
            datas = {'vote_number': 0,
                     'question_id': id,
                     'message': answer,
                     'image': ''}
            # submission_time//, vote_number, question_id, message, image
            data_manager.insert_into_answer(datas)
            return redirect('/')
        return render_template('add-answer.html', selected_data=selected_data)
    elif type == "comment":
        if request.method == 'POST':
            comment = request.form.get('comment')
            #question_id, answer_id, message, submission_time, edited_count
            datas = {'question_id': 0,
                     'answer_id': id,
                     'message': comment,
                     'edited_count': 0
                     }
            data_manager.insert_into_comment(datas)
            return redirect('/')
        return render_template('add-comment.html')


@app.route("/edit/<type>/<id>", methods=["POST", "GET"])
def edit(type, id):
    if type == "question":
        pass
    elif type == "answer":
        pass
    elif type == "comment":
        pass


@app.route("/delete/<id>")
def delete(id):
    return redirect("/list")

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
