# Rename this file to `settings.py` in deployment
import datetime
from configurer import config

# Days until Avengers 4 releases (26th Apr, 2019)
date_format = "%m/%d/%Y" #MM/DD/YYYY
Avengers4_release_date = datetime.date(2019, 4, 26)
today = datetime.date.today()
no_of_days = Avengers4_release_date - today
days_until_a4_releases = no_of_days.days

# reddit app
username = config.get_configuration("username")
password = config.get_configuration("password")
app_key = config.get_configuration("app_key")
app_secret = config.get_configuration("app_secret")
search_limit = int(config.get_configuration("search_limit"))

# bot account
bot_name = config.get_configuration("bot_name")

# subreddit information
subreddit = config.get_configuration("subreddit_name")
user_agent = config.get_configuration("user_agent")
