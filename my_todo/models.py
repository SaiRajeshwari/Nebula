from django.db import models

# Create your models here.
class Todo(models.Model):
    todo = models.CharField(max_length=85, help_text="This field is mandatory")
    done = models.BooleanField(default=False)
    def __str__(self):
        return self.todo

