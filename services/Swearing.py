import random

from config import bot, settings


class Swearing:

    def naxui(self, message):

        mess: str

        match random.randint(1, 5):
            case 1:
                mess = "Сам пошел"
                bot.send_message(message.chat.id, mess)
            case 2:
                bot.send_sticker(
                    chat_id=message.chat.id,
                    sticker="CAACAgIAAxkBAAM3Z7r3sY_iWQ_x0kiprdBkNr2GHAUAAr9YAAKgbblKtfHoQV2hgYs2BA",
                )
            case 3:
                mess = "Кусай захуй"
                bot.send_message(message.chat.id, mess)
            case 4:
                mess = "Хуй соси губой тряси"
                bot.send_message(message.chat.id, mess)
            case 5:
                bot.send_sticker(
                    chat_id=message.chat.id,
                    sticker="CAACAgIAAxkBAANPZ7r8QmgwYggRgnQWVnt6VKh-zcUAAplPAAIZN7lKYR4YNM-Vb2Y2BA",
                )
