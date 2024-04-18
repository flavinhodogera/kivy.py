from kivy.app import App
from kivy.uix.button import Button
class Myapp(App):
    def bulid(self):
        return Button(text="Hello world! This is my first program in kivy \n I'm a SESIANO Student, and I Love my Teacher ")
if __name__ == '__main__':
    Myapp ().run()