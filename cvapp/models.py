from django.db import models

from django import forms
from . toolkit import dict_creator
from . cv_toolbox import load_PDF_text
import json


class Project(models.Model):
    # dictionaries for CV App

    name = models.CharField('Project Name', max_length=50)
    role = models.CharField('Role', max_length=50)
    descr = models.TextField('Project Description', editable=True, blank=True)
    start_date = models.DateField('Start date', blank=True, null=True)
    finish_date = models.DateField('Start date', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Education(models.Model):

    degrees_choices = dict_creator('univ_degree.csv').items()

    school_name = models.CharField(max_length=50, blank=True, null=True)
    degree = models.CharField(
        max_length=20, choices=degrees_choices, default='A.A.', null=True, blank=True)
    start_date = models.DateField('Start date', blank=True, null=True)
    finish_date = models.DateField('Start date', blank=True, null=True)
    description = models.TextField(
        'Description', blank=True, null=True, default='Provide your description')

    class Meta:
        ordering = ["start_date"]
        verbose_name_plural = 'Education'

    def __str__(self):
        return str(self.start_date)+' ---> '+str(self.finish_date) + ' '+self.school_name+' - '+self.get_degree_display()


class Location (models.Model):
    country = models.CharField('Country', max_length=50, blank=True, null=True)

    def __str__(self):
        return self.country


class CV(models.Model):

    RR = 'REMOTE_READY'
    RO = 'REMOTE_ONLY'
    REMOTE_WORK_TYPES = [(RR, 'Remote Ready'), (RO, 'Remote Only')]

    # ----------------------------------
    EN = "English"
    PL = "Polish"
    ES = "Spanish"
    CV_LANG_TYPES = [(EN, 'English'), (PL, 'Polish'), (ES, 'Spanish')]

    RED = "RED"
    WHITE = "WHITE"
    BLUE = "BLUE"
    BLACK = "BLACK"

    COLOR_CHOICES = [(RED, 'Red'), (WHITE, 'White'),
                     (BLUE, 'Blue'), (BLACK, 'Black')]

    # ---------------------------------------
    CV_TYPE_CHOICES = [('SARCH', 'Solution Architect'),
                       ('DEV', 'Developer'), ('SENG', 'Software Engineer')]

    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)

    email = models.EmailField('Email', blank=True)
    mobile = models.CharField('Mobile', blank=True, max_length=12)

    birth_year = models.DateField(
        verbose_name="Birth Date", auto_now=False, blank=True, null=True)

    facebook = models.URLField('LinkedIn Profile', blank=True)

    image = models.ImageField('Photo', blank=True, null=True)
    description = models.TextField(blank=True)

    remote_work = models.CharField(
        max_length=20, choices=REMOTE_WORK_TYPES, default=RR)

    file = models.FileField('CV attachment', blank=True, null=True)
    remark = models.CharField(blank=True, max_length=20)
    # timestamp = models.DateTimeField(blank=True,  auto_now_add=True)

    cv_type = models.CharField(
        max_length=5, choices=CV_TYPE_CHOICES, default='SENG')

    cv_lang = models.CharField(
        max_length=10, choices=CV_LANG_TYPES, default='EN')

    # current_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    active = models.BooleanField()

    color = models.CharField(
        max_length=5, choices=COLOR_CHOICES, default='WHITE')

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    host_url = models.URLField(blank=True)

    projects = models.ManyToManyField(Project)

    education = models.ManyToManyField(Education)

    def __str__(self):
        return self.first_name+' '+self.last_name+' '+self.cv_type + ' ' + self.cv_lang+' ' + str(self.created_date)+' ' + str(self.updated_date)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('cv', kwargs={'pk': self.pk})


class RawData(models.Model):

    text = load_PDF_text('cv.pdf')
    cv_source_data = models.TextField(
        'CV Source Data', blank=True, null=True, default=text)
