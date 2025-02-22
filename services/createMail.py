import requests

from config import settings


class CreateMail:

    def create(self):
        url = f"{settings.MAIL_API_URL}"
        body = {"passwd": settings.MAIL_PASSWD}

        response = requests.post(url, json=body)

        if response.status_code == 200:
            return "Все збс ദ്ദിി"
        else:
            raise
