import os
from dotenv import load_dotenv

load_dotenv()


def _read_secret(path):
    try:
        with open(path) as f:
            return f.read().strip()
    except FileNotFoundError:
        return None


class Config:
    _password = (
        _read_secret(os.environ.get("DB_PASSWORD_FILE", ""))
        or os.environ.get("DB_PASSWORD", "postgres")
    )
    _user = os.environ.get("POSTGRES_USER", "postgres")
    _host = os.environ.get("DB_HOST", "localhost")
    _port = os.environ.get("DB_PORT", "5432")
    _name = os.environ.get("POSTGRES_DB", "devops_site")

    SQLALCHEMY_DATABASE_URI = f"postgresql://{_user}:{_password}@{_host}:{_port}/{_name}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
