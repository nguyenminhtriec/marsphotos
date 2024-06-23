# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:07:39 2024

@author: Nguyen Minh Triec
"""

import reflex as rx
from .data import marsdata

# from .templates.template import template


class MarsPhotoState(rx.State):
    # normal vars
    selected_date: str = '2019-10-19'
    
    data: list[marsdata.MarsPhoto]
    pos: int = 0
    page_size: int = 8
    
    # computed vars
    @rx.var
    def page_content(self) -> list[marsdata.MarsPhoto]: 
        
        return self.data[self.pos:min(self.pos+self.page_size, len(self.data))]
    
    @rx.var
    def total_pages(self) -> int:
        
        if len(self.data) % self.page_size:
            return len(self.data) // self.page_size + 1
        return len(self.data) // self.page_size
    
    @rx.var
    def current_page(self):                
        return self.pos // self.page_size + 1
        
    
    # event handlers
    def next_page(self):
        if self.pos + self.page_size <= len(self.data):
            self.pos = self.pos + self.page_size
        
    def previous_page(self):
        self.pos = max(0, self.pos - self.page_size)
        
    def first(self):
        self.pos = 0
        
    def last(self):
        if len(self.data) % self.page_size == 0:
            self.pos = len(self.data) - self.page_size
        else:    
            self.pos = len(self.data) - (len(self.data) % self.page_size)
        
    # event handler    
    def get_nasa_source(self) -> list[marsdata.MarsPhoto]: 
        self.data = marsdata.get_nasa_source(            
            selected=self.selected_date            
        )
        self.pos = 0