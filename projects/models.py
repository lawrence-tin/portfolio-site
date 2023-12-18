from django.db import models

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('Automation', 'Automation Project'),
        ('WebApp', 'Web App Development Project'),
        ('Backend', 'Backend Project'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    technologies_used = models.CharField(max_length=100)
    github_link = models.URLField()

    def __str__(self):
        return self.title
