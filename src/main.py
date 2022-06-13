from processes.dependencies import ProcessDependenciesCheck


def print_error():
    print('compile failed, please review the exception first.')


if __name__ == '__main__':
    # check dependencies
    if not ProcessDependenciesCheck().run():
        print_error()
        exit(1)
