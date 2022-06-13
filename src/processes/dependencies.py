from utils.sys_utils import SystemUtils


class ProcessDependenciesCheck:

    def _checkDependency(self, command: str) -> bool:
        if SystemUtils.hasCommand(command):
            return True
        else:
            print(f'{command} is not existed, please check your installation.')
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

        return True
