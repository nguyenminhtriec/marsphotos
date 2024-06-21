# -*- coding: utf-8 -*-
"""
Created on Mon May 13 14:07:48 2024

@author: Nguyen Minh Triec
"""

import reflex as rx
from reflex.page import get_decorated_pages
from .. import styles



def drop_down_menu(trigger: rx.Component) -> rx.Component:
    return rx.menu.root(
        rx.menu.trigger(trigger),
        rx.menu.content(
            *[
                menu_item(p['title'], p['route'])
                for p in get_decorated_pages()
            ],
            min_width='15em'
        )
    )


def menu_item(text: str, href: str) -> rx.Component:
    return rx.menu.item(
        rx.link(
            text.capitalize(),
            href=href,
            color='inherit',    
        ),
        _hover={
            "color": styles.accent_color,
            "background_color": styles.accent_text_color,
        },        
    )