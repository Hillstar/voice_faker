
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

voice_file = f"voice_msg.ogg"
  
updater = Updater("5763468370:AAFK1zzd0RRZ_pKGTXwatmDuUh90r0RzO_o",
                  use_context=True)

def get_voice(update: Update, context: CallbackContext):
    # get basic info about the voice note file and prepare it for downloading
    new_file = context.bot.get_file(update.message.voice.file_id)
    # download the voice note as a file
    new_file.download(voice_file)
    update.message.reply_text(
        "Got ur message!")

    # SOME KIND OF MAGIC MUST BE HERE

    context.bot.sendAudio(chat_id=update.message.chat_id, audio=open(voice_file, "rb"), timeout=360)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello sir, Welcome to the Bot.Please write\
        /help to see the commands available.")
  
def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /youtube - To get the youtube URL""")
  
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)
  
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)
  
  
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands
  
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text)) # Filters out unknown messages
updater.dispatcher.add_handler(MessageHandler(Filters.voice, get_voice))
  
updater.start_polling()