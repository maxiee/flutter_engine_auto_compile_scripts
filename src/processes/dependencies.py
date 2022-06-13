import subprocess
from pathlib import Path

from utils.sys_utils import SystemUtils


class ProcessDependenciesCheck:

    def _checkDependency(self, command: str) -> bool:
        if SystemUtils.hasCommand(command):
            return True
        else:
            print(f'{command} is not existed, please check your installation.')
            return False

    def _checkDepotTools(self) -> bool:
        if SystemUtils.hasCommand('gclient'):
            return True

        print('depot_tools is not installed, cloning...')
        subprocess.run([
            'git',
            'clone',
            'https://chromium.googlesource.com/chromium/tools/depot_tools.git'
        ])

        path = Path().joinpath('depot_tools')
        print('please add depot_tools to your PATH')
        print('You can run below if you use bash:')
        print(
            f"echo 'PATH={str(path.absolute())}:$PATH' >> ~/.bashrc && source ~/.bashrc")

        return False

    def run(self) -> bool:
        dependencies = [
            'ant',
            'ninja',
            'git'
        ]

        for dep in dependencies:
            if not self._checkDependency(dep):
                return False

        if not self._checkDepotTools():
            return False

        return True
