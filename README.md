# flutter_engine_auto_compile_scripts
A script for compiling Flutter Engine automatically.

## dependencies

This script is written in Python, some dependencies are needed:

1. Python3, I'm using Python3.10
2. Python related dependencies: Pipenv
3. Flutter compiling: ant

## Install

1. clone repo
2. this project use Pipenv for management, install pipenv
3. install dependencies: `pipenv install`
4. `pipenv shell`
5. in virtual environment,`python src/main.py`

## Usage

```
Options:
  --help  Show this message and exit.

Commands:
  build     Build flutter with out type defined in config.yaml
  checkout  Checkout engine to specified version ('v*.*.*',defined in...
  sync      Check dependencies and sync flutter engine source
```

## Sync Flutter Engine Source

You first need to sync the code of flutter engine. run:

```
python src/main.py sync
```

The size of code is about 20 GiB, so sit back and relax. 

### Proxy

If the cloning speed is too slow, you can try with a proxy, for example:

```
export https_proxy=http://127.0.0.1:8888
export http_proxy=http://127.0.0.1:8888
export all_proxy=socks5://127.0.0.1:8888

python src/main.py
```

## Checkout Engine version

If you haven't sync code, do sync first.

The default code is the head of master. If you want to checkout to a specific version of engine, you can run:

```
python src/main.py checkout v3.0.2
```

The script will checktout to the specific commit automatically.

All the tag-commit_hash pairs are recored in the config.yaml. If you can't find the version you want in config.yaml, please submit a issue or PR.

## Engine Building

This script simplifies the build parameters through the config.yaml config file.

First edit config.yaml, under the `build` section, you can define a `type`. Then you can define gn parameters and the output path for ninja.

For example:

```yaml
build:
  host:
    gn: '--no-lto --build-glfw-shell --linux --fuchsia --runtime-mode debug'
    out: 'host_debug'
```

You can build the engine with defined type:

```
python src/main.py build host
```

This script will run gn and ninja automatically.

That's all, happy hacking Flutter Engine.

If you have any good idea, please let me know!

My twitter: @MaxieeWong
My sina weibo: @Maeiee