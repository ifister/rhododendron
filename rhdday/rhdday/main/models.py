# -*- coding: utf-8 -*-
from django.db import models
from cms.models import CMSPlugin
from django.db.models.signals import pre_delete, post_save
from cms.plugins.picture.models import Picture,Video,File
import os
#import datetime
from rhdday import settings 
#from random import randint
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
    MAX_PHOTOGALLERY_X_SIZE=1000
    picture_thumb=models.CharField(max_length=100,blank=True,default='')

    
    def save(self, force_insert=False, force_update=False):
        super(Photos, self).save(force_insert, force_update)
        try:
            imfilepath=os.path.join(settings.MEDIA_ROOT,str(self.picture))
            imfile=Image.open(imfilepath)
            xsize,ysize=imfile.size
            xyratio=float(ysize)/float(xsize)
            minsize=float(self.thumb_minsize)
            outim=imfile.resize((int(minsize),int(xyratio*minsize)))
            outim.save(os.path.join(settings.MEDIA_ROOT,str(self.picture)[:-4]+'_thumb.png'))
            self.picture_thumb=str(self.picture)[:-4]+'_thumb.png'
            if xsize>self.MAX_PHOTOGALLERY_X_SIZE:
                outim_main=imfile.resize((int(self.MAX_PHOTOGALLERY_X_SIZE),int(xyratio*self.MAX_PHOTOGALLERY_X_SIZE)))
                outim_main.save(os.path.join(settings.MEDIA_ROOT,str(self.picture)))
            else:
                pass
        except:
            pass
        finally:
            super(Photos, self).save(force_insert, force_update)

#class ArchiveContent(models.Model):
#    year=models.IntegerField(max_length=4)
#    content=PlaceholderField('archive_content')
#    lang=models.CharField(max_length=2,default='ru')
#    
#    

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

def do_del_cms_anything(sender, **kwargs): 
    # the object which is saved can be accessed via kwargs 'instance' key.
    obj = kwargs['instance']
    #try to remove if instance is Picture
    try: 
        os.remove(os.path.join(settings.MEDIA_ROOT,str(obj.image)))
    except:
        pass
    #try to remove if instance is Video
    try:
        os.remove(os.path.join(settings.MEDIA_ROOT,str(obj.movie)))
        os.remove(os.path.join(settings.MEDIA_ROOT,str(obj.image)))
    except:
        pass
    #try to remove if instance is File
    try:
        os.remove(os.path.join(settings.MEDIA_ROOT,str(obj.file)))
    except:
        pass
    
    


def resizelargephoto(sender,**kwargs):
    obj = kwargs['instance']
    MAX_PICTURE_X_SIZE=500
    try:
        imfilepath=os.path.join(settings.MEDIA_ROOT,str(obj.image))
        imfile=Image.open(imfilepath)
        xsize,ysize=imfile.size
        xyratio=float(ysize)/float(xsize)
        if xsize>MAX_PICTURE_X_SIZE:
            outim=imfile.resize((int(MAX_PICTURE_X_SIZE),int(xyratio*MAX_PICTURE_X_SIZE)))
            outim.save(imfilepath)
        else:
            pass
    except:
        print 'Exception rises when image from cms resizing...'
    
#def create_thumbnail(sender,**kwargs):
#    obj = kwargs['instance']
#    try:
#        imfilepath=os.path.join(settings.MEDIA_ROOT,str(obj.picture))
#        imfile=Image.open(imfilepath)
#        xsize,ysize=imfile.size
#        xyratio=float(ysize)/float(xsize)
#        minsize=float(obj.thumb_minsize)
#        outim=imfile.resize((int(minsize),int(xyratio*minsize)))
#        outim.save(os.path.join(settings.MEDIA_ROOT,str(obj.picture)[:-4]+'_thumb.png'))
#        obj.picture_thumb=str(obj.picture)[:-4]+'_thumb.png'
#        print 'caretta'
#    except:
#        pass
    

pre_delete.connect(do_del_photo, sender=Photos)
pre_delete.connect(do_del_cms_anything, sender=Picture)
pre_delete.connect(do_del_cms_anything, sender=Video)
pre_delete.connect(do_del_cms_anything, sender=File)

post_save.connect(resizelargephoto,sender=Picture)
#post_save.connect(create_thumbnail, sender=Photos)
