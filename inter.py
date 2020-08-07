from kiky.app import App
from kivy.unix.button import Button

class Test(App):
	def build(self):
		return Button(text = 'Ola Mundo!')
Test().run()
