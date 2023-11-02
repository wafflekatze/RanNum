import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

kivy.require('2.2.1')

class MyApp(App):

    def build(self):
        return BoxLayout()
    
randomapp = MyApp()
randomapp.run()
