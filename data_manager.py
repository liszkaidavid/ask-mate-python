import connection


@connection.connection_handler
def get_data(cursor):
    cursor.execute("""
                        SELECT * FROM question
        """)
    requested_info = cursor.fetchall()
    return requested_info


@connection.connection_handler
def get_title_names(cursor, table):
    table_query = "SELECT * FROM {} LIMIT 1".format(table)
    cursor.execute(table_query)
    requested_data = cursor.fetchall()
    return requested_data
