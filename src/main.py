from re import L

from processes.dependencies import ProcessDependenciesCheck
from processes.gclient_init import ProcessInitGClient


def print_error():
    print('compile failed, please review the exception first.')
    exit(1)


if __name__ == '__main__':
    # check dependencies
    if not ProcessDependenciesCheck().run():
        print_error()

    if not ProcessInitGClient().run():
        print_error()

    print('success!')
