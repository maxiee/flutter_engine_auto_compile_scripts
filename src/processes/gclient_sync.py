import subprocess
from pathlib import Path


class ProcessGClientSync:

    def run(self) -> bool:
        subprocess.Popen(['gclient', 'sync'], cwd=Path().joinpath('engine'))

        return True
