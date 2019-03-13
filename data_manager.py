import connection
from datetime import datetime

##GET##

@connection.connection_handler
def get_data(cursor):
    cursor.execute("""
                        SELECT * FROM question
        """)
    requested_info = cursor.fetchall()
    return requested_info

@connection.connection_handler
def get_answers(cursor):
    cursor.execute("""
                            SELECT * FROM answer
            """)
    requested_info = cursor.fetchall()
    return requested_info


@connection.connection_handler
def get_answers_for_question(cursor, question_id):
    cursor.execute("""
                            SELECT * FROM answer WHERE question_id=%s
            """, [question_id])
    requested_info = cursor.fetchall()
    return requested_info


@connection.connection_handler
def get_question(cursor, question_id):
    cursor.execute("""
                            SELECT * FROM question WHERE id=%s
            """, [question_id])
    requested_info = cursor.fetchone()
    return requested_info

@connection.connection_handler
def get_answer(cursor, answer_id):
    cursor.execute("""
                            SELECT * FROM answer WHERE id=%s
            """, [answer_id])
    requested_info = cursor.fetchone()
    return requested_info

@connection.connection_handler
def get_limited_questions(cursor):
    cursor.execute("""
                        SELECT * FROM question LIMIT '5';
        """)
    requested_info = cursor.fetchall()
    return requested_info


@connection.connection_handler
def get_question_id_by_answer(cursor, answer_id):
    cursor.execute("""
                            SELECT question_id FROM answer WHERE id=%s
            """, [answer_id])
    requested_info = cursor.fetchone()
    return requested_info


@connection.connection_handler
def get_comments_by_question_id(cursor, question_id):
    cursor.execute("""
                            SELECT * FROM comment WHERE question_id=%s
            """, [question_id])
    requested_info = cursor.fetchall()
    return requested_info


@connection.connection_handler
def get_comment_by_id(cursor, comment_id):
    cursor.execute("""
                            SELECT * FROM comment WHERE id=%s
            """, [comment_id])
    requested_info = cursor.fetchone()
    return requested_info

@connection.connection_handler
def get_title_names(cursor, table):
    table_query = f"SELECT column_name FROM information_schema.columns WHERE table_name='{table}'"
    cursor.execute(table_query)
    requested_data = cursor.fetchall()
    return requested_data


@connection.connection_handler
def get_question_id_by_comment_id(cursor, comment_id):
    cursor.execute("""
                                SELECT question_id FROM comment WHERE id=%s
                """, [comment_id])
    requested_info = cursor.fetchone()
    return requested_info

##INSERT##

@connection.connection_handler
def insert_into_question(cursor, datas):
    submission_time = datetime.now()
    cursor.execute("""
                    INSERT INTO question (submission_time, view_number, vote_number, title, message, image, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (submission_time, datas["view_number"], datas["vote_number"], datas["title"], datas["message"], datas["image"], datas["user_id"]))


@connection.connection_handler
def insert_into_comment(cursor, datas):
    submission_time = datetime.now()
    cursor.execute("""
                    INSERT INTO comment (question_id, answer_id, message, submission_time, edited_count, user_id) VALUES (%s, %s, %s, %s, %s, %s)
    """, (datas["question_id"], datas["answer_id"], datas["message"], submission_time, datas['edited_count'], datas['user_id']))


@connection.connection_handler
def insert_into_answer(cursor, datas):
    submission_time = datetime.now()
    cursor.execute("""
                    INSERT INTO answer (submission_time, vote_number, question_id, message, image, user_id) VALUES (%s, %s, %s, %s, %s, %s)
    """, (submission_time, datas["vote_number"], datas["question_id"], datas["message"], datas["image"], datas['user_id']))


##UPDATE##

@connection.connection_handler
def update_comment(cursor, datas):
    submission_time = datetime.now()
    cursor.execute(""" UPDATE comment
                        SET submission_time=%s, message=%s, edited_count=%s
                        WHERE id=%s
    """, (submission_time,  datas["message"], datas["edited_count"], datas['id']))


@connection.connection_handler
def update_question(cursor, datas):
    submission_time = datetime.now()
    cursor.execute(""" UPDATE question
                        SET submission_time=%s, view_number=%s, vote_number=%s, title=%s, message=%s, image=%s
                        WHERE id=%s
    """, (submission_time, datas["view_number"], datas["vote_number"], datas["title"], datas["message"], datas["image"], datas["id"] ))


@connection.connection_handler
def update_answer(cursor, datas):
    submission_time = datetime.now()
    cursor.execute(""" UPDATE answer
                        SET submission_time=%s, vote_number=%s, question_id=%s, message=%s, image=%s
                        WHERE id=%s
    """, (submission_time, datas["vote_number"], datas["question_id"], datas["message"], datas["image"], datas['id']))


##DELETE##

@connection.connection_handler
def delete_question(cursor, question_id):
    cursor.execute("""
                    DELETE FROM question WHERE id=%s
    """, [question_id])


@connection.connection_handler
def delete_answer(cursor, question_id):
    cursor.execute("""
                    DELETE FROM answer WHERE id=%s
    """, [question_id])


@connection.connection_handler
def delete_question_tag(cursor, question_tag_id):
    cursor.execute("""
                    DELETE FROM question_tag WHERE question_id=%s
    """, [question_tag_id])


@connection.connection_handler
def delete_comment(cursor, comment_id):
    cursor.execute("""
                    DELETE FROM comment WHERE id=%s
    """, [comment_id])


##USER_RELATED##

@connection.connection_handler
def register_user(cursor, datas):
    registration_time = datetime.now()
    cursor.execute('''
    INSERT INTO user_list(registration_time, user_name, password, rank) VALUES  (%s, %s, %s, %s)
    ''', (registration_time, datas['user_name'], datas['password'], datas['rank']))

@connection.connection_handler
def list_users(cursor):
    cursor.execute('''
    SELECT * FROM user_list
    ''')
    users = cursor.fetchall()
    return users


@connection.connection_handler
def get_user(cursor, user_name):
    cursor.execute('''
    SELECT id, password, rank FROM user_list WHERE user_name=%s
    ''', [user_name])
    users = cursor.fetchone()
    return users


@connection.connection_handler
def get_users(cursor):
    cursor.execute('''
    SELECT id, user_name FROM user_list
    ''')
    users = cursor.fetchall()
    return users


@connection.connection_handler
def get_owner(cursor, id):
    cursor.execute('''
    SELECT user_name FROM user_list WHERE id=%s
    ''', [id])
    owner = cursor.fetchone()
    return owner
