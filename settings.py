from pathlib import Path


def get_project_root() -> Path:
    """Returns project root folder."""
    return Path(__file__).parent.parent


PORT = 8000

def get_model_path():
    MODEL_PATH = './res/model/'
    return MODEL_PATH

def get_image_path():
    IMAGE_PATH = './res/image/'
    return IMAGE_PATH