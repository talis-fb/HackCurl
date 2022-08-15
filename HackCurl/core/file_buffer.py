import os
import uuid
from os.path import exists
from tempfile import TemporaryFile


class FileBuffer:
    DEFAULT_PATH = f"{os.environ['HOME']}/.local/share/HackCurl/"

    def __init__(self, fileName: str | None):
        if fileName is None:
            fileName = uuid.uuid4().hex[0:7]

        self.filePath = os.path.join(self.DEFAULT_PATH, fileName)

        # It only hold the last content saved in file, the only contact with file is now and in the save method
        # Ever operation of edit (besides save) is make in tempfile
        self.content_file = ""
        if exists(self.filePath):
            with open(self.filePath, "r") as file:
                self.content_file = file.read()
        else:
            with open(self.filePath, "w") as file:
                self.content_file = ""

        self.tempfile = TemporaryFile("w+t")

    def read(self) -> str:
        self._jump_to_begin()
        content = self.tempfile.read()
        return content

    def overwrite(self, content: str):
        self._jump_to_begin()
        self.tempfile.truncate(0)
        self.tempfile.write(content)

    def append(self, content: str):
        self._jump_to_end()
        self.tempfile.write(content)

    def save(self):
        content = self.read()
        with open(self.filePath, "w") as file:
            file.write(content)
            self.content_file = content

    def __del__(self):
        self.tempfile.close()

    def _jump_to_begin(self):
        self.tempfile.seek(0, 0)

    def _jump_to_end(self):
        self.tempfile.seek(0, 2)
