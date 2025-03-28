from django.db import models
from django.urls import reverse

class Task(models.Model):
    id = models.AutoField(primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField(max_length=80)
    desc = models.TextField(max_length=400)
    priority = models.IntegerField()
    done = models.BooleanField(max_length=4)

    def get_absolute_url(self):
        return reverse("task:detail", kwargs={"pk": self.pk})
