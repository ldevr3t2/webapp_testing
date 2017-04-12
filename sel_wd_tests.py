import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestWebApp(unittest.TestCase):
	
	def setUp(self):
		#set up firefox for testing
		self.driver = webdriver.Firefox()
		#set security so that we can test the microphone
		self.driver.set_preference ('media.navigator.permission.disabled', True)
		self.driver.update_preferences()

	#unittest for music recognition button consistency
	def test_music_recognition_buttons(self):
		driver = self.driver
		#go to the site
		driver.get("https://ldevr3t2.github.io")
		#confirm that the title contains 'VT Musica'
		self.assertIn("VT Musica", driver.title)
		#find music button
		record_elem = driver.find_element_by_id("record")
		#find pause button
		pause_elem = driver.find_element_by_id("pause")
		#find stop and reset button
		stop_elem = driver.find_element_by_id("stop")
		#find search button
		search_elem = driver.find_element_by_id("search")
			
		#test consistency
		assert record_elem.is_enabled()	
		assert not pause_elem.is_enabled()
		assert not stop_elem.is_enabled()
		assert not search_elem.is_enabled()

		#now we will click the record button and check if they are enabled
		record_elem.click()
		assert record_elem.is_enabled()	
		assert pause_elem.is_enabled()
		assert stop_elem.is_enabled()
		assert search_elem.is_enabled()

		#now we will click the pause button and check if they are all still enabled
		pause_elem.click()
		assert record_elem.is_enabled()	
		assert pause_elem.is_enabled()
		assert stop_elem.is_enabled()
		assert search_elem.is_enabled()		

		#now we will click the stop and reset button and check if they reset
		pause_elem.click()
		assert record_elem.is_enabled()	
		assert not pause_elem.is_enabled()
		assert not stop_elem.is_enabled()
		assert not search_elem.is_enabled()	

	#unittest for music recognition search functionality
	def test_music_recognition_search(self):
		driver = self.driver
		#go to the site
		driver.get("https://ldevr3t2.github.io")
		#confirm that the title contains 'VT Musica'
		self.assertIn("VT Musica", driver.title)
		#find music button
		record_elem = driver.find_element_by_id("record")
		#find pause button
		pause_elem = driver.find_element_by_id("pause")
		#find search button
		search_elem = driver.find_element_by_id("search")

		#find the match div
		match = driver.find_element_by_id("match")

		#check for visibility of the response div
		assert not match.is_displayed()

		#record and then send
		record_elem.click()
		pause_elem.click()
		search_elem.click()

		#wait to make sure that the ajax call pushes
		ff.implicitly_wait(10) # seconds
		#check for visibility of the response div
		assert match.is_displayed()

		#unittest for reset button
	def test_artist_recommendation_reset_button(self):
		driver = self.driver
		#go to the site
		driver.get("https://ldevr3t2.github.io")
		#confirm that the title contains 'VT Musica'
		self.assertIn("VT Musica", driver.title)
		#get artist
		artist_elem = driver.find_element_by_id("artist-0")
		#get reset
		reset_elem = driver.find_element_by_id("reset")

		#add artist info and then attempt to clear
		assert artist_elem.text == ""
		artist_elem.send_keys("Van Halen")
		assert artist_elem.text == "Van Halen"
		reset_elem.click()
		assert artist_elem.text == ""

	#unittest for artist recommendation
	def test_artist_recommendation(self):
		driver = self.driver
		#go to the site
		driver.get("https://ldevr3t2.github.io")
		#confirm that the title contains 'VT Musica'
		self.assertIn("VT Musica", driver.title)
		#get artist
		artist_elem = driver.find_element_by_id("artist-0")
		#find the match div
		match = driver.find_element_by_id("recommendationMatch")

		#check for visibility of the response div
		assert not match.is_displayed()

		#add artist and send
		artist_elem.send_keys("Van Halen")
		#submit form
		artist_elem.send_keys(Keys.RETURN)
		#wait to make sure that the ajax call pushes
		ff.implicitly_wait(10) # seconds
		#check for visibility of the response div
		assert match.is_displayed()


	#unittest to add multiple artists to the search
	def test_multiple_artists(self):
		driver = self.driver
		#go to the site
		driver.get("https://ldevr3t2.github.io")
		#confirm that the title contains 'VT Musica'
		self.assertIn("VT Musica", driver.title)
		add_elem = driver.find_element_by_id("addArtist")

		#make sure that the add element is enabled
		assert add_elem.is_enabled()

		#click the element 5 times, make sure it is disabled
		add_elem.click()
		add_elem.click()
		add_elem.click()
		add_elem.click()
		add_elem.click()

		assert not add_elem.is_enabled()

		#check to see that all input lines are there
		assert driver.find_element_by_id("artist-0")
		assert driver.find_element_by_id("artist-1")
		assert driver.find_element_by_id("artist-2")
		assert driver.find_element_by_id("artist-3")
		assert driver.find_element_by_id("artist-4")

	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
    unittest.main()