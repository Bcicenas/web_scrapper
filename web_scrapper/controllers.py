from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from scrapper import scrapper
from kivy.loader import Loader
from kivy.clock import Clock
from threading import Thread

class ScrapperController(BoxLayout):
	'''Create a controller that receives a custom widget from the kv lang file.
	
	Add an action to be called from the kv lang file.
	'''
	def __init__(self, **kwargs):
		self.update()
		super(ScrapperController, self).__init__(**kwargs)
	
	url_input = ObjectProperty(rebind=True)	
	search_input = ObjectProperty(rebind=True)	
	result_label = ObjectProperty(rebind=True)
	scrape_result = 'Result'
	scrape_success = True
	def update(self):
		Clock.schedule_interval(self.update_ui_callback, 1)

	def update_ui_callback(self, dt):
		self.result_label.text = self.scrape_result
		self.url_input.text = self.url_input.text if self.scrape_success else 'Invalid URL'
		self.scrape_success = True

	def start_scrape(self):
		thread = Thread(target=self.scrape)
		# run the thread
		thread.start()
		# wait for the thread to finish
		print('Waiting for the thread...')
		thread.join()
		print('Thread finished.')

	def scrape(self):
		try:
			sc = scrapper.Scrapper('one', self.url_input.text.strip())
		except ValueError:
			self.scrape_success = False
		else:
			self.scrape_result = str(sc.find_all(self.search_input.text.strip()))
			self.scrape_success = True
