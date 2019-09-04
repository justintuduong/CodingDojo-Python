from django.db import models


class Movie(models.Model):
    # every class comes with an id
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__ (self):
        return f"<Movie object: {self.title} ({self.id})>"