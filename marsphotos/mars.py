# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 10:31:06 2024

@author: Nguyen Minh Triec
"""

import reflex as rx
from .data import marsdata
from .components.actionbar import actionbar, bottombar
from .state import MarsPhotoState

# from .templates.template import template
     
        
@rx.page(route='/mars', title='Mars Photos Overview')  
def photos_overview():
    
    return rx.box(
        
        actionbar(),           
        photo_grid(MarsPhotoState.page_content),            
        bottom_nav(),
        bottombar(),
        
        margin_top='3em',
        # position='fixed',
        # top='5vh',
        # height='90vh',
        # overflow_y='auto',
    )        
    

def bottom_nav():
    return rx.flex(
        rx.icon(
            'chevron-first',
            on_click=MarsPhotoState.first
        ),
        rx.icon(
            'chevron-left',
            on_click=MarsPhotoState.previous_page
        ),
        rx.icon(
            'chevron-right',
            on_click=MarsPhotoState.next_page
        ),
        rx.icon(
            'chevron-last',
            on_click=MarsPhotoState.last
        ),
        rx.select(
            ['8', '16', '24', '32', '40'],
            value=MarsPhotoState.page_size.to_string(),
            on_change=MarsPhotoState.set_page_size
        ),
        rx.text(
            f"{MarsPhotoState.current_page}/{MarsPhotoState.total_pages}",
        ),
        position='fixed',
        bottom='5vh',                
        width='100%',
        height='5vh',
        spacing='5',
        align='center',
        justify='center',
        background_color=rx.color('mauve', 3),
        z_index='100'       
    )

def date_selection():
    return (
        rx.hstack(
            rx.form.root(
                rx.input(name='date', type='date',
                    value=MarsPhotoState.selected_date,                        
                    on_change=MarsPhotoState.set_selected_date),
                    max_width='30%'
            ),                                   
            rx.link(
                rx.button(
                    'Show Mars photos', 
                    on_click=MarsPhotoState.get_nasa_source,
                    variant='soft',
                ),
                href='/mars'
            ),
            
            position='fixed',
            bottom='5vh',            
            z_index='1',
            justify_content='center',
            align_items='center',
            spacing='5',
            width='100%',
            height='5vh',
            
            background_color=rx.color('mauve', 2)
        )
    )
    

def photo_grid(photos: list[marsdata.MarsPhoto]) -> rx.Component:
    return (
        rx.grid(
            rx.foreach(
                photos, 
                lambda photo: photo_card(photo)                
            ),
            columns='4',
            spacing='2',
            width='100%', 
            margin_top='2em',
        )
    )

@rx.page(route='/details', title='Photos Details')
def photos_scroller() -> rx.Component:
    return rx.box(
        actionbar(),
        rx.grid(
            rx.foreach(
                MarsPhotoState.page_content, 
                lambda photo: photo_card_details(photo)                
            ),
            columns='1',
            spacing='3',
            width='100%', 
            margin_top='2em',            
        ),
        bottom_nav(),
        bottombar(),
        margin_top='3em'
    )


def photo_card(photo):
    return(           
        rx.card(
            rx.link(
                rx.text(photo.id),                    
                font_size=".75em", 
                position='absolute', 
                top='0em',
                _hover={
                    "color": rx.color('accent', 10),
                    "text_decoration": "underline",                        
                },
                href='/details'
            ),                  
                                
            rx.inset(
                rx.image(
                    src=photo.img_src
                ),
                side='bottom',               
            )
        )                             
    )


def photo_card_details(photo: marsdata.MarsPhoto) -> rx.Component:   
    return(
        rx.card(
            rx.box(
                rx.text(photo.id),
                rx.text('Date: ', photo.earth_date),
                rx.text("Camera: ", photo.camera_name),
                padding_bottom='.5em' 
            ),
            rx.inset(
                rx.image(src=photo.img_src),
                side='bottom'
            ),            
            max_width='100%'               
        )                   
    )

