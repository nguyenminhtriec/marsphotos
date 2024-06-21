"""The Home page of the Mars Photos web app."""


import reflex as rx
from .mars import photos_overview, photos_scroller
from . import index


app = rx.App(
    theme=rx.theme(
        appearance='dark',
        accent_color='blue',
    )
)
# app.add_page(index, route='/', title='Home')


