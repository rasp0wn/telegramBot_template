from telegram.ext import (Updater, CommandHandler)

# Credits to https://tecnonucleous.com/2021/04/04/como-crear-nuestro-bot-de-telegram-con-python/

def start(update, context):
	#''' START '''
	# When /start is received send "Welcome" text.
	context.bot.send_message(update.message.chat_id, "Welcome")


def main():
	TOKEN="TOKEN_VALUE_FROM @BotFather in Telegram"

	updater=Updater(TOKEN, use_context=True)
	dp=updater.dispatcher

	# Events hanbdler, send /start and the bot answers you
	dp.add_handler(CommandHandler('start',	start))

	# Start bot
	updater.start_polling()

	# Bot listening.
	updater.idle()

if __name__ == '__main__':
    main()
