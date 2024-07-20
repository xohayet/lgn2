import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7389659795:AAGNKQxX_2zCjoPkNRGDdMc65CAxySAaQpI")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24906331"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "866e8e4637fb269388b50202fb0f169c")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://ps705112:rahul@cluster0.td75ayj.mongodb.net/?retryWrites=true&w=majority")
