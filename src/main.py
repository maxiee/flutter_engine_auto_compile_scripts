from cProfile import run
from re import L

from processes.dependencies import ProcessDependenciesCheck
from processes.gclient_init import ProcessInitGClient
from processes.gclient_sync import ProcessGClientSync

if __name__ == '__main__':
    # check dependencies
    if ProcessDependenciesCheck().run() \
            and ProcessInitGClient().run() \
            and ProcessGClientSync().run():
        print('success!')
        exit(0)

    print('compile failed, please review the exception first.')
    exit(1)
