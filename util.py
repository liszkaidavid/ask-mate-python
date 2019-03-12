import data_manager
import bcrypt

def get_table_titles(table):
    table_titles = [title["column_name"] for title in data_manager.get_title_names(table)]
    return table_titles
