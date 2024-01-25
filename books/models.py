from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    author = models.CharField(max_length=100, null=False, blank=False)
    gender = models.CharField(max_length=100, null=False, blank=False)
    pages = models.IntegerField(null=False, blank=False)
    copies = models.IntegerField(null=False, blank=False)
    isbn = models.IntegerField(null=False, blank=False)
    description = models.CharField(max_length=250, null=False, blank=False)
    publishing_company = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
