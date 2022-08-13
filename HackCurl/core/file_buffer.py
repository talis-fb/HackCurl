from os.path import exists
from tempfile import TemporaryFile

DEFAULT_PATH = "~/.local/HackCurl/"


class FileBuffer:
    def __init__(self, filePath: str, create_temp_opy: bool = True):
        if not exists(filePath):
            filePath = DEFAULT_PATH + filePath
            if not exists(filePath):
                raise Exception("File doens't exist")

        with open(filePath, "w+t") as file:
            self.file = file

        if create_temp_opy:
            self.tempfile = TemporaryFile("w+t")

    def append(self, content: str):
        if self.tempfile:
            self.tempfile.write(content)
        else:
            self.file.write(content)

    def update(self):
        if self.tempfile:
            content = self.tempfile.read()
            self.file.write(content)
