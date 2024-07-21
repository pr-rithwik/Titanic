from . import get_project_root


def get_config_details():
    root_dir = get_project_root()
    config_path = root_dir / "conf"
    return str(config_path)