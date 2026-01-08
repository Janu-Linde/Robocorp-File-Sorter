from robocorp.tasks import task
from RPA.FileSystem import FileSystem

@task
def minimal_task():
    create_folders()
    move_file_into_folders()


def get_file_extensions():
    fs = FileSystem()
    directory = r"C:\Users\janul\Downloads"
    extensions = []

    for file in fs.list_files_in_directory(directory): 
        extension = fs.get_file_extension(file)
        extensions.append(extension)

    return list(dict.fromkeys(extensions))


def create_folders():
    fs = FileSystem()
    directory = r"C:\Users\janul\Downloads"

    extensions = get_file_extensions()

    for ext in extensions:
        folder_path = f"{directory}\\{ext}"
        fs.create_directory(folder_path)


def move_file_into_folders():
    fs = FileSystem()
    directory = r"C:\Users\janul\Downloads"

    for file in fs.list_files_in_directory(directory):
        ext = fs.get_file_extension(file)
        fs.move_file(
            f"{file}",
            f"{directory}\\{ext}\\{fs.get_file_name(file)}"
        )