import speech_recognition as sr
import telebot
from pydub import AudioSegment

from config import settings
from services.base import Services

bot = telebot.TeleBot(settings.BOT_API)


@bot.message_handler(content_types=["voice"])
def handle_voice_message(message):
    # Проверяем, что сообщение пришло от авторизованного пользователя
    if message.from_user.id != settings.ALLOWED_USER_ID:
        bot.reply_to(
            message,
            f"Извините, только определенный пользователь может отправлять голосовые сообщения.",
        )
        return

    # Получаем файл голосового сообщения
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    # Сохраняем аудиофайл
    with open("temp.ogg", "wb") as f:
        f.write(downloaded_file)

    recognized_text = Services().recognize_from_audio_file("./temp.ogg")

    if recognized_text is not None:
        bot.reply_to(message, recognized_text)
    else:
        bot.reply_to(message, "Нипоооон ¯\(°_o)/¯")


bot.polling(none_stop=True)
