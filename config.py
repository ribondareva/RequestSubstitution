from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    # Страница, которую откроет браузер
    URL: str
    # Конкретный запрос, который хотим подменить.
    REPLACED_URL: str
    # Тело ответа, которое мы вернём вместо настоящей страницы
    BODY: str

    class Config:
        env_file = ".env"


settings = Settings()
