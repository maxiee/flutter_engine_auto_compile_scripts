import json
from pathlib import Path


class ProcessInitGClient:

    def run(self) -> bool:
        solutions = [
            {
                "managed": False,
                "name": "src/flutter",
                "url": "https://github.com/flutter/engine.git",
                "custom_deps": {},
                "deps_file": "DEPS",
                "safesync_url": "",
            }
        ]

        path = Path().joinpath('engine')
        path.mkdir(parents=True, exist_ok=True)
        path = path.joinpath('.gclient')

        with open(path, 'w') as f:
            json.dump(solutions, f, indent=4)

        return True
