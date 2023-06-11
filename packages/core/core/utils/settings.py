from core.constants.environment import Environment
from dotenv import load_dotenv
from dynaconf import Dynaconf, Validator

load_dotenv()


class Settings(Dynaconf):
    host: str


settings = Settings(
    envvar_prefix="CONDUIT",
    settings_files=["settings.toml"],
    environments=[environment.value for environment in Environment],
    validators=[Validator("HOST", required=True)],
)

__all__ = ["settings"]
