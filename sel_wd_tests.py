import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, re, random

class TestWebApp(unittest.TestCase):
	
	def setUp(self):
		#set up firefox for testing
		#set security so that we can test the microphone
		profile = webdriver.FirefoxProfile()
		profile.set_preference('media.navigator.permission.disabled', True)
		profile.set_preference("http.response.timeout", 20)
		profile.set_preference("dom.max_script_run_time", 20)
		self.driver = webdriver.Firefox(firefox_profile=profile)
		#resize the window
		self.driver.maximize_window()

	#unittest for music recognition button consistency
	def test_music_recognition_buttons(self):
		driver = self.driver
		#go to the site
		driver.get("https://ldevr3t2.github.io")
		#confirm that the title contains 'VT Musica'
		self.assertIn("VT Musica", driver.title)
		#get to recognition section
		content_elem = driver.find_element_by_xpath("//*[@id='recognitionSection']")
		content_elem.click()

		#debug out by saving screenshot
		driver.save_screenshot('screens/test_music_recognition_buttons.png')

		#find music button
		record_elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='record']")))
		#find pause button
		pause_elem = driver.find_element_by_xpath("//*[@id='pause']")
		#find stop and reset button
		stop_elem = driver.find_element_by_xpath("//*[@id='stop']")
		#find search button
		search_elem = driver.find_element_by_xpath("//*[@id='search']")
			
		#test consistency
		assert record_elem.is_enabled()	
		assert pause_elem.is_enabled() == False
		assert stop_elem.is_enabled() == False
		assert search_elem.is_enabled() == False

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
		assert pause_elem.is_enabled() == False
		assert stop_elem.is_enabled() == False
		assert search_elem.is_enabled()	== False

	#unittest for music recognition search functionality
	def test_music_recognition_search(self):
		driver = self.driver
		#go to the site
		driver.get("https://ldevr3t2.github.io")
		#confirm that the title contains 'VT Musica'
		self.assertIn("VT Musica", driver.title)
		#get to recognition section
		content_elem = driver.find_element_by_xpath("//*[@id='recognitionSection']")
		content_elem.click()	

		#debug out by saving screenshot
		driver.save_screenshot('screens/test_music_recognition_search.png')

		#find music button
		record_elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='record']")))
		#find pause button
		pause_elem = driver.find_element_by_xpath("//*[@id='pause']")
		#find search button
		search_elem = driver.find_element_by_xpath("//*[@id='search']")

		#find the match div
		match = driver.find_element_by_xpath("//*[@id='match']")

		#check for visibility of the response div
		assert not match.is_displayed()

		#record and then send
		record_elem.click()
		pause_elem.click()
		search_elem.click()

		#wait for the async response to finish
		time.sleep(10)

		#check for visibility of the response div
		assert match.is_displayed()

  #unittest for reset button
	def test_artist_recommendation_reset_button(self):
		driver = self.driver
		#go to the site
		driver.get("https://ldevr3t2.github.io")
		#confirm that the title contains 'VT Musica'
		self.assertIn("VT Musica", driver.title)
		#get to recommendation section
		content_elem = driver.find_element_by_xpath("//*[@id='recommendationSection']")
		content_elem.click()

		#wait for the elements to come in view
		time.sleep(2)		

		#get artist
		artist_elem = driver.find_element_by_xpath("//*[@id='artist-0']")
		#get reset
		reset_elem = driver.find_element_by_xpath("//*[@id='reset']")

		#add artist info and then attempt to clear
		assert artist_elem.text == ""
		artist_elem.send_keys("Van Halen")
		reset_elem.click()
		assert artist_elem.text == ""

	#unittest for artist recommendation
	def test_artist_recommendation(self):
		driver = self.driver
		#go to the site
		driver.get("https://ldevr3t2.github.io")
		#confirm that the title contains 'VT Musica'
		self.assertIn("VT Musica", driver.title)
		#get to recommendation section
		content_elem = driver.find_element_by_xpath("//*[@id='recommendationSection']")
		content_elem.click()

		#wait for the elements to come in view
		time.sleep(2)		

		#get artist
		artist_elem = driver.find_element_by_xpath("//*[@id='artist-0']")
		#find the match div
		match = driver.find_element_by_xpath("//*[@id='recommendationMatch']")

		#check for visibility of the response div
		assert not match.is_displayed()

		#add artist and send
		artist_elem.send_keys("Van Halen")
		#submit form
		artist_elem.send_keys(Keys.RETURN)

		#wait for the async response to finish
		time.sleep(10)

		#check for visibility of the response div
		assert match.is_displayed()


	#unittest to add multiple artists to the search
	def test_multiple_artists(self):
		driver = self.driver
		#go to the site
		driver.get("https://ldevr3t2.github.io")
		#confirm that the title contains 'VT Musica'
		self.assertIn("VT Musica", driver.title)
		#get to recommendation section
		content_elem = driver.find_element_by_xpath("//*[@id='recommendationSection']")
		content_elem.click()

		#wait for the elements to come in view
		time.sleep(2)		

		add_elem = driver.find_element_by_xpath("//*[@id='addArtist']")

		#make sure that the add element is enabled
		assert add_elem.is_enabled()

		#debug out by saving screenshot
		driver.save_screenshot('screens/test_multiple_artists.png')

		#click the element 5 times, make sure it is disabled
		add_elem.click()
		add_elem.click()
		add_elem.click()
		add_elem.click()
		add_elem.click()

		assert not add_elem.is_enabled()

		#check to see that all input lines are there
		assert driver.find_element_by_xpath("//*[@id='artist-0']")
		assert driver.find_element_by_xpath("//*[@id='artist-1']")
		assert driver.find_element_by_xpath("//*[@id='artist-2']")
		assert driver.find_element_by_xpath("//*[@id='artist-3']")
		assert driver.find_element_by_xpath("//*[@id='artist-4']")

	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
    unittest.main()