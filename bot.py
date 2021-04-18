from telegram.ext import Updater, CommandHandler
import logging
import os
import telegram

#Configure logging
logging.basicConfig(
    level=logging.INFO,format="%(asctime)s - %(name)s - %(levelname)s - %(message)s,"
)
logger = logging.getLogger()

#soicitar TOKEN
TOKEN = os.getenv("TOKEN")
print(TOKEN)

def start(update, context):
    print(update)

if __name__ == "__main__":
    #Obtener informacion de nuestro bot
    my_bot = telegram.Bot(token=TOKEN)
    print(my_bot.getMe())
    
#enlazamos el update con el bot
updater = Updater(my_bot.token, use_context=True)

#crear despachador
dp = updater.dispatcher

#crear manejadores
dp.add_handler(CommandHandler("start", start))

#
updater.start_polling()

#permite finalizar con Ctrl+C
updater.idle()



