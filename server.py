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
    return render_template("display-question.html",
                           selected_data=selected_data,
                           passable_list=answers)


@app.route("/display/<type>/<id>")
def display(type, id):
    table_data = data_manager.get_data()
    if type == "question":
        exceptions = ['id', 'question_id']
        selected_data = data_manager.get_question(id)[0]
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
    selected_data = data_manager.get_question(id)[0]
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
        table_data = data_manager.get_data()
        selected_data = table_data[int(id)-1]
        if request.method == 'POST':
            question_title = request.form.get('title')
            question = request.form.get('message')
            datas = {'view_number': 0,
                     'vote_number': 0,
                     'title': question_title,
                     'message': question,
                     'image': '',
                     'id':id}
            # submission_time//, view_number, vote_number, title, message, image
            data_manager.update_question(datas)
            return redirect('/')
        return render_template('edit-question.html', updata=selected_data, id=id)
    elif type == "answer":
        pass
    elif type == "comment":
        pass
    return redirect('/')

@app.route("/delete/<type><id>")
def delete(type, id):
    if type == "question":
        data_manager.delete_question(id)
    elif type == "answer":
        data_manager.delete_answer(id)
    elif type == "comment":
        pass
    return redirect("/list")


if __name__ == '__main__':
    app.run()
