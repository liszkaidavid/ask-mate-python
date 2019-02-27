import connection


@connection.connection_handler
def get_data(cursor):
    cursor.execute("""
                        SELECT * FROM question
        """)
    requested_info = cursor.fetchall()
    return requested_info


@connection.connection_handler
def get_limited_questions(cursor):
    cursor.execute("""
                        SELECT * FROM question LIMIT '5';
        """)
    requested_info = cursor.fetchall()

    print(requested_info)

    return requested_info


@connection.connection_handler
def get_title_names(cursor, table):
    table_query = f"SELECT column_name FROM information_schema.columns WHERE table_name='{table}'"
    cursor.execute(table_query)
    requested_data = cursor.fetchall()
    return requested_data


@connection.connection_handler
def insert_into_question(cursor, datas):
    cursor.execute("""
                    INSERT INTO question (submission_time, view_number, vote_number, title, message, image) VALUES (%s, %s, %s, %s, %s, %s)
    """, (datas["submission_time"], datas["view_number"], datas["vote_number"], datas["title"], datas["message"], datas["image"]))


@connection.connection_handler
def insert_into_answer(cursor, datas):
    cursor.execute("""
                    INSERT INTO answer (submission_time, view_number, vote_number, title, message, image) VALUES (%s, %s, %s, %s, %s, %s)
    """, (datas["submission_time"], datas["view_number"], datas["vote_number"], datas["title"], datas["message"], datas["image"]))


@connection.connection_handler
def update_question(cursor, datas):
    cursor.execute(""" UPDATE question
                        SET first_name=%s, last_name=%s, phone_number=%s, email=%s, application_code=%s
                        WHERE id=%s
    """, (datas["first_name"], datas["last_name"], datas["phone_number"], datas["email"], datas["application_code"], int(datas["id"])))


@connection.connection_handler
def update_answer(cursor, datas):
    cursor.execute(""" UPDATE answer
                        SET first_name=%s, last_name=%s, phone_number=%s, email=%s, application_code=%s
                        WHERE id=%s
    """, (datas["first_name"], datas["last_name"], datas["phone_number"], datas["email"], datas["application_code"], int(datas["id"])))


@connection.connection_handler
def delete_question(cursor, datas):
    print(datas)
    cursor.execute("""
                    DELETE FROM question WHERE first_name=%s AND last_name=%s
    """, (datas["first_name"], datas["last_name"]))


@connection.connection_handler
def delete_answer(cursor, datas):
    print(datas)
    cursor.execute("""
                    DELETE FROM answer WHERE first_name=%s AND last_name=%s
    """, (datas["first_name"], datas["last_name"]))