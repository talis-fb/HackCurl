import os
from io import TextIOWrapper

from HackCurl.core.file_buffer import FileBuffer


def _read_file(file: TextIOWrapper):
    file.seek(0)
    return file.read()


def test_file_exist():
    this_folder = os.path.dirname(__file__)
    file_target_name = "file.txt"
    file_target_path = this_folder + "/" + file_target_name

    FileBuffer.DEFAULT_PATH = this_folder

    with open(file_target_path, "r") as actual_file:
        assert _read_file(actual_file) == "Initial text"

        file_buffer = FileBuffer(file_target_path)
        file_buffer.overwrite("Hello World")
        file_buffer.overwrite("New Value to overwrite above one")

        assert _read_file(actual_file) == "Initial text"
        assert file_buffer.read() != _read_file(actual_file)

        file_buffer.save()
        assert file_buffer.read() == "New Value to overwrite above one"

        file_buffer.overwrite("Now, ")
        file_buffer.append("just append")

        # Before saving
        assert file_buffer.read() != _read_file(actual_file)

        # After saving
        file_buffer.save()
        assert file_buffer.read() == _read_file(actual_file)
        assert file_buffer.read() == "Now, just append"

        # Reset for start
        file_buffer.overwrite("Initial text")
        file_buffer.save()
        assert _read_file(actual_file) == "Initial text"


def test_file_dont_exist():
    this_folder = os.path.dirname(__file__)
    file_target_name = "file_shouldnt_exist.txt"
    file_target_path = this_folder + "/" + file_target_name

    FileBuffer.DEFAULT_PATH = this_folder

    file_buffer = FileBuffer(file_target_name)

    with open(file_target_path, "r") as actual_file:
        assert _read_file(actual_file) == ""

        file_buffer.overwrite("Hello World")
        file_buffer.overwrite("New Value to overwrite above one")

        assert _read_file(actual_file) == ""
        assert file_buffer.read() != _read_file(actual_file)

        file_buffer.save()
        assert file_buffer.read() == "New Value to overwrite above one"

        file_buffer.overwrite("Now, ")
        file_buffer.append("just append")

        # Before saving
        assert file_buffer.read() != _read_file(actual_file)

        # After saving
        file_buffer.save()
        assert file_buffer.read() == _read_file(actual_file)
        assert file_buffer.read() == "Now, just append"

    # Reset for start
    os.remove(file_target_path)
