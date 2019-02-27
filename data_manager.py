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
    table_query = f"SELECT column_name FROM information_schema.columns WHERE table_name='{table}'"
    cursor.execute(table_query)
    requested_data = cursor.fetchall()
    return requested_data


@connection.connection_handler
def insert_to_table(cursor, table, data):
    table = ','.join(table)
    print(table, data)
    table_query = f"INSERT INTO {table} VALUES {data}"
    print(table_query)
    return cursor.execute(table_query)



@connection.connection_handler
def update_table(cursor, table, data):
    table_query = "UPDATE table_name='{}'" \
                  "SET colomn_name " \
                  "WHERE id = {} ".format(table)
    return cursor.execute(table_query)



@connection.connection_handler
def remove_table(cursor, table, data):
    pass