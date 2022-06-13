import subprocess
from pathlib import Path


class ProcessGClientSync:

    def run(self) -> bool:
        subprocess.Popen(['gclient', 'sync'], cwd=Path().joinpath('engine'))

        # https://stackoverflow.com/questions/13744473/command-line-execution-in-different-folder
        # when sync success, will show:
        # Syncing projects: 100% (126/126), done.

        return True
