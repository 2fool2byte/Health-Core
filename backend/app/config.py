#holds the instance we will use to get the needed variables from the .env file 
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')
    database_url: str
    supabase_url: str
    supabase_publishable_key: str

#create the settings instance to grab the env files and the helper function to call settings dict
#result cached so we dont need to keep reading the env file
@lru_cache
def get_settings():
    return Settings()
settings = get_settings()

