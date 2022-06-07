from django.db import models

class Articles(models.Model):
    title=models.CharField(max_length= 100)
    slug=models.SlugField()
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        this function shows registered title in list of articles, it can be body, or every data that we have inserted in admin page
        :return:
        """
        return self.title

    def snippet(self):
        """when a text is too long we can show only a certain character of it """
        return self.body[:50]+"..."