#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 10:51:14 2020

@author: gurkirpal
"""

import gerber
from gerber.render.cairo_backend import GerberCairoContext
from gerber.render import RenderSettings, theme
from gerber import load_layer
import os
import threading
import time

def final(copper,mask,drill,colour,name,silk=None):
    new_settings=RenderSettings(color=colour,alpha=0.8)
    new=GerberCairoContext()
    
    new.render_layer(copper,settings=new_settings)
    new.render_layer(mask,settings=new_settings)
    if(silk!=None):
        new.render_layer(silk)
    new.render_layer(drill)
    new.dump(os.path.join(BASE_DIR,name))

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),'gerbers'))

copper=load_layer(os.path.join(BASE_DIR,'copper.GTL'))
mask=load_layer(os.path.join(BASE_DIR,'soldermask.GTS'))
silk=load_layer(os.path.join(BASE_DIR,'silkscreen.GTO'))
drill=load_layer(os.path.join(BASE_DIR,'ncdrill.DRD'))

copper_bottom=load_layer(os.path.join(BASE_DIR,'bottom_copper.GBL'))
mask_bottom=load_layer(os.path.join(BASE_DIR,'bottom_mask.GBS'))

col=[theme.COLORS['red'],theme.COLORS['white'],theme.COLORS['blue'],theme.COLORS['green'],
     theme.COLORS['black'],theme.COLORS['red'],theme.COLORS['white'],
     theme.COLORS['blue'],theme.COLORS['green'],theme.COLORS['black']]
name=['1.png','2.png','3.png','4.png','5.png','5.png','back1.png','back2.png','back3.png','back4.png','back5.png']

back=[]
t=[]
for i in range(10):
    if(i<5):
        t.append(threading.Thread(target=final,args=(copper,mask,drill,col[i],name[i],silk)))
    else:
        back.append(threading.Thread(target=final,args=(copper_bottom,mask_bottom,drill,col[i],name[i])))

for i in t:
    i.start()    
for i in back:
    i.start()