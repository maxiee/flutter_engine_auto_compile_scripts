from pathlib import Path

solutions = """
solutions = [
  {
    "managed": False,
    "name": "src/flutter",
    "url": "https://github.com/flutter/engine.git",
    "custom_deps": {},
    "deps_file": "DEPS",
    "safesync_url": "",
  },
]
"""


class ProcessInitGClient:

    def run(self) -> bool:
        path = Path().joinpath('engine')
        path.mkdir(parents=True, exist_ok=True)
        path = path.joinpath('.gclient')

        with open(path, 'w') as f:
            f.write(str(solutions))

        return True
