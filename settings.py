from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )
    ANTHROPIC_API_KEY: str | None = None
    DEFAULT_CLAUDE_MODEL: str | None = "claude-opus-4-8"


settings = Settings()
