# -*- coding: utf-8 -*-
from django.db import models
from cms.models import CMSPlugin
from django.db.models.signals import pre_delete
import os 
import datetime
from rhdday.settings import MEDIA_ROOT
from random import randint


class Photos(models.Model):
    
    def uploadto(self,filename):
        '''
        Rename user photo.
        '''
        done=False
        while not done:
            filename='%s'%randint(0,10000)
            if not os.path.exists(os.path.join(MEDIA_ROOT,filename)):
                done=True
            else:
                pass
        _filepath=os.path.join('photos','%s'%self.year,self.filename)
        self.filepath=models.CharField(max_length=20,default=_filepath)

    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    description_ru = models.CharField(max_length=350,default='')
    description_en = models.CharField(max_length=350,default='')
    year=models.IntegerField(max_length=4)
    filepath=models.CharField(max_length=20,default='')
    picture=models.FileField(upload_to=uploadto,blank=True,default='NULL')
    readonly_fields=['filepath']