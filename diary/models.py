from django.db import models
from django.contrib.auth.models import User
#A02 fix: from .fields import EncryptedTextField

class DiaryEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    #A02: Cryptographic failures
    #Private diary content is stored in plaintext in the db
    content = models.TextField()
    #fix: use an encrypted field to protect the content in the db
    #content = EncryptedTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
