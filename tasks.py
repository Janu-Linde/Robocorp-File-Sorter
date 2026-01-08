from robocorp.tasks import task
from RPA.FileSystem import FileSystem

# For the sake of time this project currently does not sort file but rather prints the names of the files in the directory.

@task
def minimal_task():
    read_file_names()


def read_file_names():
    fs = FileSystem()
    directory = r"C:\Users\janul\Downloads"

    for file in fs.list_directories_in_directory(directory):
        name = fs.get_file_name(file)
        print(name)