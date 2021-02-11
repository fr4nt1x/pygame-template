import os


def get_data_dir():
    return os.path.split(os.path.abspath(__file__))[0]