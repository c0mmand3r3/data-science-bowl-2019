import os


def get_file_path(path):
    _path = []
    for directory, _, files in os.walk(path):
        for filename in files:
            _path.append(os.path.join(directory, filename))
    return _path
