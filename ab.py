from telegram.ext import *


def stm(u,c):
    u.message.reply_text("Yes Bro")

def upt(u,c):
    a = str(c.bot.get_file(u.message.photo[-1]).download())
    u.message.reply_text(a)


uu = Updater("5895389339:AAFxtHGcFItvazTYkYiSDN2EARcRluWVE9U",use_context=True)

uu.dispatcher.add_handler(CommandHandler("start",stm))
uu.dispatcher.add_handler(MessageHandler(Filters.photo,upt))


uu.start_polling()
uu.idle()
