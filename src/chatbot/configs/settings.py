from functools import lru_cache

from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    YamlConfigSettingsSource,
)

from chatbot.configs.constants import APP_DIR


class AppSettings(BaseSettings):

    app_name: str = "IAT AI Chatbot"

    debug: bool = True
    introspection: bool = True

    cors_allow_origins: list[str] = ["*"]
    cors_allow_methods: tuple[str, ...] = (
        "GET",
        "POST",
        "DELETE",
        "PUT",
        "PATCH",
        "HEAD",
        "OPTIONS",
    )
    cors_allow_headers: list[str] = ["*"]
    cors_allow_credentials: bool = False
    cors_max_age: int = 600

    model_config = SettingsConfigDict(yaml_file=f"{APP_DIR}/production.yaml")

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        """
        Use YAML as the single source of truth for settings.
        Expects YAML file to be located in src/{app_env}.yaml
        """
        return (YamlConfigSettingsSource(settings_cls),)


# setting related function
@lru_cache
def get_application_settings() -> AppSettings:
    return AppSettings()
