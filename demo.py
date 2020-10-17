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

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),'gerbers'))

copper=load_layer(os.path.join(BASE_DIR,'copper.GTL'))
mask=load_layer(os.path.join(BASE_DIR,'soldermask.GTS'))
silk=load_layer(os.path.join(BASE_DIR,'silkscreen.GTO'))
drill=load_layer(os.path.join(BASE_DIR,'ncdrill.DRD'))

new=GerberCairoContext()
new_settings=RenderSettings(color=theme.COLORS['red'],alpha=0.8)
white_text_settings=RenderSettings(color=theme.COLORS['white'],alpha=0.8)
new.render_layer(copper,settings=new_settings)
new.render_layer(mask)
new.render_layer(silk,settings=white_text_settings)
new.render_layer(drill)

new.dump(os.path.join(BASE_DIR,'front.png'))    

new.clear()
copper_bottom=load_layer(os.path.join(BASE_DIR,'bottom_copper.GBL'))
mask_bottom=load_layer(os.path.join(BASE_DIR,'bottom_mask.GBS'))

new.render_layer(copper_bottom,settings=new_settings)
new.render_layer(mask_bottom)
new.render_layer(drill)

new.dump(os.path.join(BASE_DIR,'back.png')) 



