import os
import qrcode
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from telegram import ChatAction

INPUT_TEXT = 0


def start(update, context):
    update.message.reply_text('Hola, bienvenido, que deseas hacer? \n Usa qr para generar.')
    print('start')


def qr_command_handler(update, context):
    update.message.reply_text('Envia texto.')
    return INPUT_TEXT


def generate_qr(text):
    filename = text + '.jpg'
    img = qrcode.make(text)
    img.save(filename)
    return filename


def send_qr(filename, chat):
    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO,
        timeout=None
    )
    chat.send_photo(
        photo=open(filename, 'rb')
    )
    os.unlink(filename)


def input_text(update, context):
    text = update.message.text
    chat = update.message.chat
    filename = generate_qr(text)
    print(chat)
    send_qr(filename, chat)
    return ConversationHandler.END


if __name__ == '__main__':
    updater = Updater(token='1784474668:AAG6DffL1G2VBkzzMH1X74ZEBQGsii9i8-Y', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('qr', qr_command_handler)
        ],
        states={
            INPUT_TEXT: [
                MessageHandler(Filters.text, input_text)
            ]
        },
        fallbacks=[]
    ))

    updater.start_polling()
    updater.idle()
