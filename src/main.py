from cProfile import run
from re import L

import click

from processes.dependencies import ProcessDependenciesCheck
from processes.gclient_init import ProcessInitGClient
from processes.gclient_sync import ProcessGClientSync


@click.group()
def cli():
    pass


@click.command()
def sync():
    """Check dependencies and sync flutter engine source"""
    if ProcessDependenciesCheck().run() \
            and ProcessInitGClient().run() \
            and ProcessGClientSync().run():
        print('success!')
        exit(0)

    print('compile failed, please review the exception first.')
    exit(1)


if __name__ == '__main__':
    cli.add_command(sync)
    cli()
