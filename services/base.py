import speech_recognition as sr
from pydub import AudioSegment
from transformers import pipeline

from services.createMail import CreateMail


class Services:
    nlp = pipeline("zero-shot-classification")

    def process_command(self, command):
        candidate_labels = [
            "создать почту",
            "сделать почту",
        ]
        result = self.nlp(command, candidate_labels)
        return result

    def execute_action(self, command):

        prompt: str = command.get("labels")[0]

        if "создать почту" in prompt or "сделать почту" in prompt:
            print("\nСоздаю почту\n")
            return CreateMail().create()

    def convert_ogg_to_wav(self, filename, new_filename):
        audio = AudioSegment.from_ogg(filename)
        audio.export(new_filename, format="wav")

    def convert_mp3_to_wav(self, filename, new_filename):
        audio = AudioSegment.from_mp3(filename)
        audio.export(new_filename, format="wav")

    def recognize_from_audio_file(self, filename):
        recognizer = sr.Recognizer()

        if filename.endswith(".ogg"):
            wav_filename = "temp.wav"
            self.convert_ogg_to_wav(filename, wav_filename)
            filename = wav_filename

        if filename.endswith(".mp3"):
            wav_filename = "temp.wav"
            self.convert_mp3_to_wav(filename, wav_filename)
            filename = wav_filename

        # Загружаем аудио файл
        with sr.AudioFile(filename) as source:
            print("Слушаю аудиофайл...")
            audio_data = recognizer.record(source)  # Считываем все данные из аудиофайла

        try:
            # Используем Google API для распознавания речи
            text = recognizer.recognize_google(audio_data, language="ru-RU")
            print(f"Распознанный текст: {text}")
            return text
        except sr.UnknownValueError:
            print("Не удалось распознать речь")
            return None
        except sr.RequestError:
            print("Ошибка соединения с сервисом распознавания")
            return None
