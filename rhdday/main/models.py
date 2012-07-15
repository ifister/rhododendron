# -*- coding: utf-8 -*-
from django.db import models
from cms.models import CMSPlugin
from django.db.models.signals import pre_delete
import os 
import datetime
from rhdday.settings import MEDIA_ROOT
from random import randint


def photoupload(instance,filename):
    '''
    Rename user photo.
    '''
    try:
        cpath=os.path.join(MEDIA_ROOT,'photo','%s'%instance.year)
        if os.path.exists(cpath):
            return u'photo/%s/%s'%(instance.year,filename)
        else:
            res=atoi('%s'%instance.year)
            os.path.mkdir(os.path.join(MEDIA_ROOT,'photo','%s'%instance.year))
            return u'photo/%s/%s'%(instance.year,filename)
    except:
        return u'photo/misc/%s'%filename


class Photos(models.Model):

    '''
    Base Photo 
    '''
    readonly_fields=['filepath']


    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    description_ru = models.CharField(max_length=350,default='')
    description_en = models.CharField(max_length=350,default='')
    year=models.IntegerField(max_length=4)
    picture=models.FileField(upload_to=photoupload,blank=True,default='NULL')

class Foo(CMSPlugin):
    pass
    