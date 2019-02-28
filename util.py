import data_manager

def get_table_titles():
    table_titles = [title["column_name"] for title in data_manager.get_title_names('question')]
    return table_titles
