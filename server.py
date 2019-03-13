from flask import Flask, render_template, request, redirect, session, escape
import data_manager
import util

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


def last_page(question_id):
    last_url = "/display/question/"
    last_url += str(question_id)
    return redirect(last_url)


@app.route('/')
def home_page():
    table_titles = util.get_table_titles('question')
    datas = data_manager.get_limited_questions()
    return render_template("list.html",
                           table_titles=table_titles,
                           table_datas=datas)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = data_manager.get_user(request.form.get('user_name'))
        print(user)
        if user is not None:
            session['user_name'] = request.form['user_name']
            session['user_id'] = user['id']
            session['user_rank'] = user['rank']
            is_valid_user = util.verify_password(request.form['password'], user['password'])
            print(is_valid_user)
            session['is_valid'] = is_valid_user
        return redirect('/list')
    return render_template('add-user.html', login=True)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route("/list")
def list():
    table_titles = util.get_table_titles('question')
    table_data = data_manager.get_data()
    return render_template("list.html",
                           table_titles=table_titles,
                           table_datas=table_data)


@app.route("/display/<type>/<id>")
def display(type, id):
    if type == "question":
        exceptions = ['id', 'question_id']
        selected_data = data_manager.get_question(id)
        answers = data_manager.get_answers_for_question(id)
        comment_data = data_manager.get_comments_by_question_id(id)
        if not not answers:
            for i, answer in enumerate(answers):
                answers[i]["user_id"] = data_manager.get_owner(answer["user_id"])["user_name"]
            for i, comment in enumerate(comment_data):
                print(comment)
                comment_data[i]["user_id"] = data_manager.get_owner(comment["user_id"])["user_name"]
        user_name = data_manager.get_owner(selected_data["user_id"])
        return render_template("display-question.html",
                               selected_data=selected_data,
                               passable_list=answers,
                               comment_data=comment_data,
                               question_id=id,
                               exceptions=exceptions,
                               table_title=util.get_table_titles(type),
                               owner=user_name)
    elif type == 'user':
        return render_template('/')
    return redirect('/')


@app.route("/add/<type>/<id>", methods=["POST", "GET"])
def add(type, id):
    if type == "question":
        if request.method == 'POST':
            question_title = request.form.get('title')
            question = request.form.get('message')
            print(session['user_id'])
            datas = {'view_number': 0,
                    'vote_number': 0,
                    'title': question_title,
                    'message': question,
                    'image': '',
                    'user_id': session['user_id']}
            data_manager.insert_into_question(datas)
            return redirect("/")
        return render_template('add-question.html')
    elif type == "answer":
        selected_data = data_manager.get_question(id)
        if request.method == 'POST':
            answer = request.form.get('message')
            datas = {'vote_number': 0,
                     'question_id': id,
                     'message': answer,
                     'image': '',
                     'user_id': session["user_id"]}
            # submission_time//, vote_number, question_id, message, image
            data_manager.insert_into_answer(datas)
            return last_page(id)
        return render_template('add-answer.html', selected_data=selected_data)
    elif type == "comment":
        if request.method == 'POST':
            comment = request.form.get('comment')
            question_id = data_manager.get_question_id_by_answer(id)["question_id"]
            datas = {'question_id': question_id,
                     'answer_id': id,
                     'message': comment,
                     'edited_count': 0,
                     'user_id': session['user_id']
                     }
            data_manager.insert_into_comment(datas)
            return last_page(question_id)
        return render_template('add-comment.html', answer_id=id)
    elif type == "user":
        if request.method == 'POST':
            user_name = request.form.get('user_name')
            hashed_password = util.hash_password(request.form.get('password'))
            datas = {
                'user_name': user_name,
                'password': hashed_password,
                'rank': 4
            }
            data_manager.register_user(datas)
            return redirect('/')
        return render_template('add-user.html', login=False)

@app.route("/edit/<type>/<id>", methods=["POST", "GET"])
def edit(type, id):
    if type == "question":
        selected_data = data_manager.get_question(id)
        if request.method == 'POST':
            question_title = request.form.get('title')
            question = request.form.get('message')
            datas = {'view_number': selected_data['view_number'],
                     'vote_number': selected_data['vote_number'],
                     'title': question_title,
                     'message': question,
                     'image': '',
                     'id': id}
            # submission_time//, view_number, vote_number, title, message, image
            data_manager.update_question(datas)
            return last_page(id)
        return render_template('edit-question.html', updata=selected_data, id=id)
    elif type == "answer":
        selected_data = data_manager.get_answer(id)
        if request.method == 'POST':
            answer = request.form.get('message')
            datas = {'vote_number': selected_data['vote_number'],
                     'question_id': selected_data['question_id'],
                     'message': answer,
                     'image': '',
                     'id': id}
            # submission_time//, vote_number, question_id, message, image
            data_manager.update_answer(datas)
            return last_page(selected_data['question_id'])
        return render_template('edit-answer.html', updata=selected_data, answer_id=id)
    elif type == "comment":
        selected_data = data_manager.get_comment_by_id(id)
        qid = data_manager.get_question_id_by_comment_id(id)["question_id"]
        if request.method == "POST":
            datas = {'message': request.form.get('message'),
                     'id': id,
                     'edited_count': selected_data['edited_count'] + 1}
            data_manager.update_comment(datas)
            return last_page(qid)
        return render_template("edit-comment.html", updata=selected_data, comment_id=id)


@app.route("/delete/<type>/<id>")
def delete(type, id):
    if type == "question":
        data_manager.delete_question(id)
        return redirect("/")
    elif type == "answer":
        qid = data_manager.get_question_id_by_answer(id)["question_id"]
        data_manager.delete_answer(id)
    elif type == "comment":
        qid = data_manager.get_question_id_by_comment_id(id)["question_id"]
        data_manager.delete_comment(id)
    return last_page(qid)


if __name__ == '__main__':
    app.run()
