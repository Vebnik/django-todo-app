from django.db import models


class TodoItem(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=200)
  created_at = models.DateField()

  def to_dict(self) -> dict:
    return {
      'name': self.name,
      'description': self.description,
      'created_at': self.created_at
    }
