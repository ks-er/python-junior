import os

def bad_open(file_path, mode):
    """Некорректная функция открытия файла"""
    raise Exception


def open_and_close_file(file_path):
    """Открывает и закрывает файл

    Args:
        file_path: путь до файла
    """
    ###
    # Добавьте свой код сюда
    ###
    absolute_path = os.getcwd() + "\\scope\\task_4\\" +file_path
    with open(absolute_path, 'r') as f:
        f.close()
