# -*- coding: utf-8 -*-
"""
Created on Wed May 15 10:21:59 2024

@author: Nguyen Minh Triec
"""

import reflex as rx
from .components.actionbar import actionbar, bottombar
from .mars import date_selection


@rx.page(route='/', title='Home')
def index() -> rx.Component:
    return rx.center(
        actionbar(),
        
        rx.image(
            src='/424907.png', 
            width=['90%', '80%', '80%', '80%', '60%'], 
            display='inline-block', 
            margin_y='5em',
        ),
        
        date_selection(),
        bottombar()        
    )