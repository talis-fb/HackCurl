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

        self.tempfile = TemporaryFile("w+t")

    def write(self, content: str):
        self.tempfile.write(content)

    def read(self) -> str:
        self.tempfile.seek(0, 0)
        content = self.tempfile.read()
        return content

    def save(self):
        content = self.read()
        with open(self.filePath, "w") as file:
            file.write(content)
            self.content_file = content
