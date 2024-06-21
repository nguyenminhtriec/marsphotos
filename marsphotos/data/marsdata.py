# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 23:03:14 2024

@author: Nguyen Minh Triec
"""
import reflex as rx
import urllib3
# import os


class MarsPhoto(rx.Base):
    id: int = 0
    img_src: str = ''
    earth_date: str = ''
    camera_name: str = ''
    
    
nasa_photos_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
api_key = 'DEMO_KEY'   # os.getenv('NASA_API_KEY') 


def get_nasa_source(url=nasa_photos_url, selected=''):
    items = []
    resp = urllib3.request("GET", url, fields={'earth_date': selected, 'api_key': api_key})
    nasa_photos = resp.json()['photos']
    
    if not nasa_photos:
        return [MarsPhoto(id= -1, img_src= '/polar-bear.jpg')]
    
    for d in nasa_photos:
        items.append(
            MarsPhoto(
                id= d['id'],
                img_src= d['img_src'].replace('http://', 'https://'),
                earth_date= d['earth_date'],
                camera_name= d['camera']['full_name']
            )           
        )
          
    return items
   