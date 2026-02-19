import os


class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))

    DATA_DIR = os.getenv(
        "DATA_DIR",
        os.path.join(PROJECT_ROOT, "data")
    )

    MEDIA_DIR = os.getenv(
        "MEDIA_DIR",
        os.path.join(PROJECT_ROOT, "media")
    )

    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(MEDIA_DIR, exist_ok=True)

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        f"sqlite:///{os.path.join(DATA_DIR, 'revista.db')}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

