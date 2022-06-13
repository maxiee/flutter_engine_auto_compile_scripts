import shutil


class SystemUtils:

    @staticmethod
    def hasCommand(command: str) -> bool:
        return shutil.which(command) is not None
