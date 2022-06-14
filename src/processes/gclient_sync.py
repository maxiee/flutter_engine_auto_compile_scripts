import os
import subprocess
from pathlib import Path


class ProcessGClientSync:

    def run(self) -> bool:
        dart_tools_path = Path().joinpath('engine').joinpath(
            'src').joinpath('third_party').joinpath('dart').joinpath('tools')
        new_python_path = f'$PATHONPATH:{dart_tools_path.absolute()}'
        print(new_python_path)
        os.environ['PYTHONPATH'] = new_python_path
        p = subprocess.Popen('gclient sync',
                             cwd=Path().joinpath('engine'),
                             shell=True)
        p.wait()
        # https://stackoverflow.com/questions/13744473/command-line-execution-in-different-folder
        # when sync success, will show:
        # Syncing projects: 100% (126/126), done.

        return True
