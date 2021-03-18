#from kivy.app import app
from kivy.animation import Animation
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

from kivy.core.window import Window
Window.size = (490, 700)


class Login(MDApp):
    l = StringProperty()

    def build(self):
        self.l = "C:\\Users\\hombr\\Desktop\\Medcheck\\medcheck.png"
        return
    def email(self):
        self.l = "C:\\Users\\hombr\\Desktop\\Medcheck\\email.png"
        return
    def password(self):
        self.l = "C:\\Users\\hombr\\Desktop\\Medcheck\\password.png"
        return


    def login(self, widget, widget1, widget2, widget22, widget3, widget4, widget5):
        self.l = "C:\\Users\\hombr\\Desktop\\Medcheck\\medcheck.png"
        animate1 = Animation(opacity=0, duration=0.5)
        animate1.start(widget)
        animate2 = Animation(opacity=0, duration=0.5)
        animate2.start(widget1)
        animate3 = Animation(opacity=0, duration=0.5)
        animate3.start(widget2)
        animate33 = Animation(opacity=0, duration=0.5)
        animate33.start(widget22)
        animate4 = Animation(pos_hint={"center_x": .5, "center_y": .05}, size_hint=(.3, .3), duration=1.5)
        animate4 += Animation(pos_hint={"center_x": .5, "center_y": .86}, size_hint=(.4, .4), duration=1.5)
        animate4.start(widget3)
        animate5 = Animation(pos_hint={"center_x": .5, "center_y": .64}, duration=3)
        animate5.start(widget4)
        animate6 = Animation(pos_hint={"center_x": .5, "center_y": .55}, duration=3)
        animate6.start(widget5)



if __name__ == '__main__':
    Login().run()