__author__ = 'EUNGI'
from abc import ABCMeta, abstractmethod
from pico2d import *

class ClickableImage:
    __metaclass__ = ABCMeta #추상 클래스로 선언
    def __init__(self):
        self.x
        self.y
        self.x_start
        self.x_end
        self.y_start
        self.y_end
        self.focus = 0
    def draw(self):
        pass
    def click_left(self):
        pass
    def click_right(self):
        pass
    def handle(self, event):
        # for event in events:
        if event.type == SDL_MOUSEMOTION:
            x, y = event.x, event.y
            if self.x_start < x and x <self.x_end and self.y_start < y and y < self.y_end:
                self.focus = 1
                # print(self.nameOfBeacon + ' : focus %d',self.focus)
            else:
                self.focus = 0
        if event.type == SDL_MOUSEBUTTONDOWN and self.focus == 1:
            if event.button == SDL_BUTTON_LEFT:
                self.click_left()
            elif event.button == SDL_BUTTON_RIGHT:
                self.click_right()