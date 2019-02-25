import connection


@connection.connection_handler
def get_data(cursor):
    cursor.execute("""
                        SELECT * FROM question
        """)
    requested_info = cursor.fetchall()
    return requested_info
