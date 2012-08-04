# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pagemodel import Page
from cms.plugin_rendering import render_placeholder

from django.utils.translation import ugettext_lazy as _
from django import forms
from django.utils.translation import get_language
from models import Photos,Foo
from random import choice
from re import findall
from string import atoi
from django.http import Http404  
import pdb



def get_year_from_request(obj,reqest):
    try:
        theyear=findall(r'/?(\d\d\d\d)$',str(reqest.get_full_path()))[-1]
    except:
        try:
            objs=obj.objects.order_by('year')[0]
            theyear=objs.year
        except:
            pass
    return theyear

class MainPageService(CMSPluginBase):
    model = Foo
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
        years.sort()
        context['LANG']=get_language()
        context['YEARS']=[]
        context['PHOTOS']=[]
        for k in years:
            context['YEARS'].append({'year': k})
  #      pdb.set_trace()
  #      for k in xrange(10):
  #          objs=choice(ph_objs)
  #          context['PHOTOS'].append({'description':objs.description, 'year': objs.year, 'filepath':objs.filepath})
            
        return context

class GalleryService(CMSPluginBase):
    model = Foo
    name = _("Gallery Page Service Plugin")
    render_template = "cms/plugins/mainpageservice.html"
    def render(self, context, instance, placeholder):
        context['cur_placeholder'] = placeholder
        try:
            theyear=get_year_from_request(Photos,context['request'])
            allphotos=Photos.objects.filter(year=theyear)
            context['PHOTOS']=allphotos
        except:
            raise Http404
        return context

class GetArchiveYears(CMSPluginBase):
    model = Foo
    name = _("Get Archive Years Plugin")
    render_template = "cms/plugins/mainpageservice.html"
    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['cur_placeholder'] = placeholder
        years=[]
        try:
            arch_objs=Page.objects.filter(template='archive.html',published=True)
            for k in arch_objs:
                years.append(str(k))
                
            years=list(set(years))
            years.sort()
            context['LANG']=get_language()
            context['YEARS']=[]
            for k in years:
                context['YEARS'].append({'year': k})
            print context['YEARS']
        except:
            pass
  #      pdb.set_trace()
  #      for k in xrange(10):
  #          objs=choice(ph_objs)
  #          context['PHOTOS'].append({'description':objs.description, 'year': objs.year, 'filepath':objs.filepath})
            
        return context
    
#class ArchiveService(CMSPluginBase):
#    model = Foo
#    name = _("Archive service plugin")
#    render_template = "cms/plugins/mainpageservice.html"
#    def render(self, context, instance, placeholder):
#        context['cur_placeholder'] = placeholder
#        context['LANG']=get_language()
#        try:
#            theyear=get_year_from_request(ArchiveContent,context['request'])
#            print theyear,get_language()
#            archive=ArchiveContent.objects.filter(year=theyear).filter(lang=get_language())[0]
#            print "archive lang is=",archive.lang,id(archive.content)
#            rew=render_placeholder(archive.content,context)
#            print rew,id(archive.content)
#            context['ARHCIVE']=rew
#        except:
#            raise Http404
#        return context


plugin_pool.register_plugin(MainPageService)
plugin_pool.register_plugin(GalleryService)
plugin_pool.register_plugin(GetArchiveYears)

