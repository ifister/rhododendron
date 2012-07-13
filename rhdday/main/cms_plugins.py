# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.utils.translation import get_language
from models import Photos
from random import choice
from re import findall
from string import atoi
from django.http import Http404  
#import pdb

class MainPageService(CMSPluginBase):
    model = Photos
    name = _("Main Page Service Plugin")
    render_template = "cms/plugins/mainpageservice.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['cur_placeholder'] = placeholder
        
        years=[]
        ph_objs=Photos.objects.order_by('year')
        for k in ph_objs:
            years.append(k.year)
        years=list(set(years))
        context['LANG']=get_language()
        context['YEARS']=[]
        context['PHOTOS']=[]
        for k in years:
            context['YEARS'].append({'year': k})
                
        for k in xrange(10):
            objs=choice(ph_objs)
            context['PHOTOS'].append({'description':objs.description, 'year': objs.year, 'filepath':objs.filepath})
        return context

class GalleryService(CMSPluginBase):
    '''
    
    '''
    model = Photos
    name = _("Gallery Page Service Plugin")
    render_template = "cms/plugins/mainpageservice.html"
    request=context['request']
    
    try:
        theyear=findall(r'/\d\d\d\d/|\\\d\d\d\d\\',str(context['request'].get_full_path()))[-1]
        theyear=atoi(theyear)
        allphotos=Photos.objects.order_by('year'=theyear)
    except:
        raise Http404
    
    return context




plugin_pool.register_plugin(MainPageService)

