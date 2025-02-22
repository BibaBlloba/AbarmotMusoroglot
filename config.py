from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_API: str
    ALLOWED_USER_ID: int
    MAIL_API_URL: str
    MAIL_PASSWD: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
