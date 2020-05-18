import requests
import json
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

URLS = [line.rstrip('\n') for line in open('urls')]

options = Options()
	
options.set_headless(True)
	
driver = webdriver.Firefox(options=options)

#driver = webdriver.Firefox()

print(URLS)

imageslist = []

i = 0
while i < len(URLS):
	
	print(URLS[i])
	
	try:
	
		driver.get(URLS[i])
	
		imageLen = driver.execute_script("return document.images.length;")
	
		b = 0
	
		while b < imageLen:
		
			imageslist.append(driver.execute_script("if(document.images[" + str(b) + "].alt == '' | 'null'){ return document.images[" + str(b) + "].src}"))
		
			print(imageslist[b])
		
			b += 1
	
		images = '\n'.join(str(e) for e in imageslist)
	
		with open("images", "a+") as file:
			file.write(URLS[i] + ': ' + images + '\n')
	
		i += 1
	
	except:
		
		print('Failed')
		
		i += 1

driver.quit()