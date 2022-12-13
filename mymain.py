from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from random import random
import time

from kivy.clock import Clock
from functools import partial

def set_color(button, color, *args):
    button.color = color

class MemorizeGame(GridLayout):
    button5: Button

    def __init__(self, **kwargs):
        super(MemorizeGame, self).__init__(**kwargs)
        self.cols = 3

        #create buttons
        self.button1 = Button(text='', background_color=(0,0,1,1))
        self.button2 = Button(text='', background_color=(0,1,1,1))
        self.button3 = Button(text='', background_color=(1,0,1,1))
        self.button4 = Button(text='', background_color=(0,1,1,1))
        self.button5 = Button(text='', background_color=(0, 1, 0, 1))
        self.button6 = Button(text='', background_color=(1, 1, 0, 1))
        self.buttonList = [self.button1, self.button2, self.button3, self.button4, self.button5, self.button6]

        #add buttons to the screen
        for button in self.buttonList:
            self.add_widget(button)

    def blinkSquare(self):
        self.button1.background_color = (1, 1, 1, 1)
        def reset_color(*args):
            self.button1.background_color = (0, 0, 1, 1)
        Clock.schedule_once(reset_color, 1)

        # alternative:
        # Clock.schedule_once(partial(set_color, self.button1, (0, 0, 1, 1)))

    def on_touch_down(self, touch):
        self.blinkSquare()


class MemorizeApp(App):

    def build(self):
        game= MemorizeGame()
        return game

if __name__ == "__main__":
    MemorizeApp().run()
