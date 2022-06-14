import subprocess
from pathlib import Path

import click

from processes.dependencies import ProcessDependenciesCheck
from processes.gclient_init import ProcessInitGClient
from processes.gclient_sync import ProcessGClientSync
from script_utils.config_utils import ConfigUtils


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
    else:
        print('compile failed, please review the exception first.')
        exit(1)


@click.command()
@click.argument('version')
def checkout(version):
    """Checkout engine to specified version ('v*.*.*',defined in config.yaml)"""
    config = ConfigUtils.loadConfig()
    tag = config['tags'][version]
    checkout_cmd = subprocess.Popen(
        f'git checkout {tag}',
        shell=True,
        cwd=Path().joinpath('engine').joinpath('src').joinpath('flutter'))
    checkout_cmd.wait()


@click.command()
@click.argument('build_type')
def build(build_type: str):
    """Build flutter with out type defined in config.yaml"""
    config = ConfigUtils.loadConfig()
    config_type = config['build'][build_type]
    gn_cmd = subprocess.Popen(
        f'./flutter/tools/gn {config_type["gn"]}',
        cwd=Path().joinpath('engine').joinpath('src'),
        shell=True)
    gn_cmd.wait()

    ninja_cmd = subprocess.Popen(
        f'ninja -C out/{config_type["out"]}',
        cwd=Path().joinpath('engine').joinpath('src'),
        shell=True)
    ninja_cmd.wait()


if __name__ == '__main__':
    cli.add_command(sync)
    cli.add_command(build)
    cli.add_command(checkout)
    cli()
