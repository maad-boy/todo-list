from typing import Optional
import yaml

from .config import Config


_config: Optional[Config] = None

def _load_config(file_path: str):
    with open(file_path, 'r') as file:
        config_data = yaml.safe_load(file)
        return Config(**config_data)

def init_config(file_path: str):
    global _config
    _config = _load_config(file_path)

def get_config() -> Config:
    if _config is None:
        raise RuntimeError("Config not initialized")
    return _config