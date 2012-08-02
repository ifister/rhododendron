# -*- coding: utf-8 -*-
from django.db import models
from cms.models import CMSPlugin
from django.db.models.signals import pre_delete, pre_save
import os ,pdb
import datetime
from rhdday import settings 
from random import randint
import Image

def photoupload(instance,filename):
    '''
    Rename user photo.
    '''
    try:
        cpath=os.path.join(settings.MEDIA_ROOT,'photo','%s'%instance.year)
        if os.path.exists(cpath):
            return u'photo/%s/%s'%(instance.year,filename)
        else:
            dirtomake=os.path.join(settings.MEDIA_ROOT,'photo','%s'%instance.year)
            os.mkdir(dirtomake)
            return u'photo/%s/%s'%(instance.year,filename)
    except:
        return u'photo/misc/%s'%filename

class Photos(models.Model):
    '''
    Base Photo 
    '''
    name_ru = models.CharField(max_length=100,blank=True)
    name_en = models.CharField(max_length=100,blank=True)
    description_ru = models.CharField(max_length=350,default='',blank=True)
    description_en = models.CharField(max_length=350,default='',blank=True)
    year=models.IntegerField(max_length=4)
    picture=models.ImageField(upload_to=photoupload,default='NULL')
    thumb_minsize=models.IntegerField(max_length=3,default=200)
    picture_thumb=models.CharField(max_length=100,blank=True,default='')

class Foo(CMSPlugin):
    pass
    
def do_del_photo(sender, **kwargs): 
    # the object which is saved can be accessed via kwargs 'instance' key.
    obj = kwargs['instance']
    try:
        whatberemoved=os.path.join(settings.MEDIA_ROOT,str(obj.picture))
        print  'Image %s has been removed.'%whatberemoved
        os.remove(os.path.join(settings.MEDIA_ROOT,str(obj.picture)))
        os.remove(os.path.join(settings.MEDIA_ROOT,str(obj.picture)[:-4]+'_thumb.png'))
    except:
        print 'Exception raises.'


def create_thumbnail(sender,**kwargs):
    obj = kwargs['instance']
    try:
        imfilepath=os.path.join(settings.MEDIA_ROOT,str(obj.picture))
        imfile=Image.open(imfilepath)
        xsize,ysize=imfile.size
        xyratio=float(ysize)/float(xsize)
        minsize=float(obj.thumb_minsize)
        outim=imfile.resize((int(minsize),int(xyratio*minsize)))
        outim.save(os.path.join(settings.MEDIA_ROOT,str(obj.picture)[:-4]+'_thumb.png'))
        obj.picture_thumb=str(obj.picture)[:-4]+'_thumb.png'
    except:
        pass
    

pre_delete.connect(do_del_photo, sender=Photos)
pre_save.connect(create_thumbnail, sender=Photos)
