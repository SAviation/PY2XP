import kivy
from kivy.app import App
from kivy.lang import Builder
kivy.require('2.1.0')
from kivy.uix.screenmanager import ScreenManager, Screen

class MainScreen(Screen):
    pass

class ChangeGraphics(Screen):
    pass

class ChangeScenery(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file('./resources/main.kv')

class SAXPM(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    saxpm = SAXPM()
    saxpm.run()