import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "28182720"))
    API_HASH = os.environ.get("API_HASH", "5360e97ddd3e771e124aa50c6c33ec3a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5870406957:AAEdvFwNYdsXjaukiBNiaBPdobnQR1pmIrg")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOHoBuwFg4N9t8kboKsHYZJkOcVVwcH2LZZDyweRHbwGvKtexb6u-4lO8jSlPd3XciZWHD3q6IiXQAcaOlHHK0JF0Y6QImSZXSEX48vmNOG56wxa6dgiDOEhkW1YiP9UGaKM39aGGoDwsDUmkXSnOd9JoTS-78ujeGDuxu_8NACW_Ru51LCEl1SpPEN31zhe3Fj8_Q_8YZ1qeuEw76uxa5DgwJBBrLm0yYLY4OaaW17U0YEzkDP3wIZNpiVl0glsYzlzoIfcPa5cXy1CNY1UHUiG_y3yeF1H6V2OdzhaQt-c2JD4unUDMbZpjUmgGvA2wu5pneEAbzRW4HmedhAMaZ8EPua8=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "lexsibot")
    SUPPORT = os.environ.get("SUPPORT", "lexaaaanih") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "lexaaaanih") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
