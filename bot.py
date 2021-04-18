from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import os
import telegram
import random

#Configure logging
logging.basicConfig(
    level=logging.INFO,format="%(asctime)s - %(name)s - %(levelname)s - %(message)s,"
)
logger = logging.getLogger()

#soicitar TOKEN
TOKEN = os.getenv("TOKEN")
print(TOKEN)

def start(update, context):
    #print(update)
    logger.info(f"El usuario {update.effective_user['id']}, ha iniciado una convesacion")
    name = update.effective_user['first_name']
    update.message.reply_text(f"Hola {name} soy tu bot")

def random_number(update, context):
    user_id = update.effective_user['id']
    number = random.randint(0,10)
    logger.info(f"El usuario {user_id}, ha solicitado numero aleatorio : {number}")
    context.bot.sendMessage(chat_id=user_id, parse_mode="HTML",text=f"<b>Numero</b> aleatorio: \n{number}")

def echo(update, context):
    user_id = update.effective_user['id']
    logger.info(f"El usuario {user_id}, escribio un mensaje de texto")
    text = update.message.text
    context.bot.sendMessage(
        chat_id=user_id, 
        parse_mode="MarkdownV2",
        text=f"*Escibiste:* \n _{text}_")

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
dp.add_handler(CommandHandler("random", random_number))
dp.add_handler(MessageHandler(Filters.text, echo))

#
updater.start_polling()
print("BOT CARGADO")

#permite finalizar con Ctrl+C
updater.idle()



