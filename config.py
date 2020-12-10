import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN","1419998054:AAG-sW4Yv7x3uhrWaRUpsHe6_W0Uay1Cl64")
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY","a71c791c-87ca-48ba-9534-3744916b0302")
    AUTHORIZED_USERS = [int(user) for user in os.environ.get("AUTHORIZED_USERS").split("1314948019")]
    TG_CHARACTER_LIMIT = 4000 
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME","herokuflixbot")
