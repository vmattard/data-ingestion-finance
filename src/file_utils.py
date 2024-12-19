from pathlib import Path


def get_project_root() -> Path:
    """Returns project root folder."""
    return Path(__file__).parent.parent


def get_data_folder() -> Path:
    """
    Returns project data folder.
    Creates the folder if it doesn't exist.
    """
    folder_path = get_project_root() / "data"
    folder_path.mkdir(parents=True, exist_ok=True)
    return folder_path


def get_logs_folder() -> Path:
    """
    Returns project log folder.
    Creates the folder if it doesn't exist.
    """
    folder_path = get_project_root() / "logs"
    folder_path.mkdir(parents=True, exist_ok=True)
    return folder_path


def get_symbols_folder() -> Path:
    """
    Returns project log folder.
    Creates the folder if it doesn't exist.
    """
    folder_path = get_data_folder() / "symbols"
    folder_path.mkdir(parents=True, exist_ok=True)
    return folder_path
