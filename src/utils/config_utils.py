from typing import Dict

from yaml import Loader, load


class ConfigUtils:

    @staticmethod
    def loadConfig() -> Dict:
        with open('config.yaml', 'r') as f:
            return load(f.read(), Loader=Loader)
