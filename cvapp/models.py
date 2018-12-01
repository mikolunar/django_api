from django.db import models

# Create your models here.


class CV(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    email = models.EmailField(blank=True)
    mobile = models.CharField(blank=True, max_length=12)
    facebook = models.URLField(blank=True)

    # image=models.ImageField()
    description = models.TextField(blank=True)

    file = models.FileField(blank=True, null=True)
    remark = models.CharField(blank=True, max_length=20)
    #timestamp = models.DateTimeField(blank=True,  auto_now_add=True)

    CV_TYPE_CHOICES = [('SARCH', 'Solution Architect'),
                       ('DEV', 'Developer'), ('SENG', 'Software Engineer')]
    cv_type = models.CharField(
        max_length=5, choices=CV_TYPE_CHOICES, default='SENG')

    CV_LANG_TYPES = [('EN', 'English'), ('PL', 'Polish'), ('ES', 'Spanish')]
    cv_lang = models.CharField(
        max_length=3, choices=CV_LANG_TYPES, default='EN')

    active = models.BooleanField()

    COLOR_CHOICES = [('RED', 'Red'), ('WHITE', 'White'),
                     ('BLUE', 'Blue'), ('BLACK', 'Black')]
    color = models.CharField(
        max_length=5, choices=COLOR_CHOICES, default='WHITE')

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    host_url = models.URLField(blank=True)

    def __str__(self):
        return self.first_name+' '+self.last_name+' '+self.cv_type + ' ' + self.cv_lang+' ' + str(self.created_date)+' ' + str(self.updated_date)
