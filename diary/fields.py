import os

from cryptography.fernet import Fernet
from django.db import models


class EncryptedTextField(models.TextField):
    def get_prep_value(self, value):
        value = super().get_prep_value(value)

        if value is None:
            return None
        
        key = os.environ["DIARY_ENCRYPTION_KEY"].encode()
        encryption = Fernet(key)

        return encryption.encrypt(value.encode()).decode()

    def from_db_value(self, value, expression, connection):
        if value is None:
            return None
        
        key = os.environ["DIARY_ENCRYPTION_KEY"].encode()
        encryption = Fernet(key)

        return encryption.decrypt(value.encode()).decode()