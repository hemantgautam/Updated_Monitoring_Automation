# import time
# import json
import os
import time
from datetime import datetime
from time import sleep

import requests
# from time import gmtime, strftime
from apscheduler.schedulers.blocking import BlockingScheduler
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# from twilio.rest import Client
from selenium.webdriver import Keys

from twilio.rest import Client
import pywhatkit as kit
from selenium.webdriver.common.action_chains import ActionChains

# import pyautogui as pg
# import pywin32


# sched = BlockingScheduler()

# @sched.scheduled_job('interval', id='my_job_id', seconds=300)
def main():
	print('Start Time', datetime.now())
	# options = Options()
	# options.headless = True
	# hit the monitoring url
	driver = webdriver.Chrome(executable_path=r'D:\Users\HGautam3\Projects\HMD Support\Updated Monitoring\Updated_Monitoring_Automation\chromedriver.exe')
	driver.get('https://itsusralsp06834.jnj.com:8443/ControlM/')
	# while True:
	# 	sleep(1)

	user_name = driver.find_element("xpath","//*[@id='login-user-name']")
	password = driver.find_element("xpath", "//*[@id='login-user-password']")
	# org = driver.find_element('input')
	# # Find the value of org?
	# val = org.get_attribute("attribute name")

	user_name.send_keys("cpatil11")
	# user_name.send_keys(Keys.ENTER)
	password.send_keys("Chana@1811")
	password.send_keys(Keys.ENTER)
	time.sleep(3)
	mont = driver.find_element("xpath", "//*[@id='SelfServiceDomainTabHeader']").click()
	time.sleep(3)
	services = driver.find_element("xpath", "//*[@id='servicesTabDiv']").click()
	time.sleep(3)
	filter = driver.find_element("xpath", "//*[@id='servicesFilterDropDown']").click()
	time.sleep(3)
	ended_not_ok = driver.find_element("xpath","/html/body/app-app-main/ng-component/app-shell/div/div/sls-domain/div/scrollable-tabset/div/div[1]/div/div/div[3]/tab-content/sls-services/div/div[2]/div[1]/div/div[1]/div[1]/ul/li[3]/span[1]").click()
	time.sleep(3)
	
	path_for_count = "/html/body/app-app-main/ng-component/app-shell/div/div/sls-domain/div/div[2]/a/div/span[2]/flat-status-chart/div/div/div[1]"
	size_variable = driver.find_element("xpath", path_for_count)
	size = int(size_variable.text)
	print("Size: ", size)
	time.sleep(3)
	button = driver.find_element("xpath", "//*[@id='servicesListViewButton']").click()

	time.sleep(3)

	excluded_projects =['1MDPD-DEPUY SYNTHES - US - BIDW - ODH PRD-DEPUYBI']

	# Fetch list of images from folder
	ss_list = os.listdir(r"D:\Users\HGautam3\Projects\HMD Support\Updated Monitoring\Updated_Monitoring_Automation\sceenshots")

	print(ss_list)
	for i in range(1,size+1):
		time.sleep(3)
		# import pdb; pdb.set_trace()

		#check code for decommisioned applications
		apps_name_path= "/html/body/app-app-main/ng-component/app-shell/div/div/sls-domain/div/scrollable-tabset/div/div[1]/div/div/div[3]/tab-content/sls-services/div/div[2]/div[1]/div/div[2]/sls-services-list/div/ctm-common-grid-wrapper-downgraded/div/ag-grid-angular/div/div[2]/div[1]/div[3]/div[2]/div/div/div[{0}]/div[3]/service-name-cell-renderer/div/a".format(i)
		apps_name = driver.find_element("xpath", apps_name_path)
		apps = apps_name.get_attribute('initial-text')
		if apps not in excluded_projects:
			ended_not_ok_project_link = "/html/body/app-app-main/ng-component/app-shell/div/div/sls-domain/div/scrollable-tabset/div/div[1]/div/div/div[3]/tab-content/sls-services/div/div[2]/div[1]/div/div[2]/sls-services-list/div/ctm-common-grid-wrapper-downgraded/div/ag-grid-angular/div/div[2]/div[1]/div[3]/div[2]/div/div/div[{0}]/div[3]/service-name-cell-renderer/div/a".format(i)
			time.sleep(3)
			driver.find_element("xpath", ended_not_ok_project_link).click()
			time.sleep(3)
			# list_view_click = driver.find_element("xpath", "//*[@id='viewpointJobListViewbtn']").click()
			time.sleep(3)

			a = ActionChains(driver)
			gear_hover = driver.find_element("xpath", "/html/body/app-app-main/ng-component/app-shell/div/div/sls-domain/div/scrollable-tabset/div/div[1]/div/div/div[4]/tab-content/service-viewpoint/div/div[2]/div[2]/div[3]/job-list/div/ctm-common-grid-wrapper-downgraded/div/ag-grid-angular/div/div[2]/div[1]/div[1]/div[2]/div/div/div[2]")
			a.move_to_element(gear_hover).perform()
			time.sleep(2)
			path2 = "/html/body/app-app-main/ng-component/app-shell/div/div/sls-domain/div/scrollable-tabset/div/div[1]/div/div/div[4]/tab-content/service-viewpoint/div/div[2]/div[2]/div[3]/job-list/div/ctm-common-grid-wrapper-downgraded/div/ag-grid-angular/div/div[2]/div[1]/div[1]/div[2]/div/div/div[2]/div[2]/span/i"
			filter = driver.find_element("xpath", path2).click()
			time.sleep(3)
			uncheck_all = driver.find_element("xpath", "//*[@id='selectAllContainer']").click()
			time.sleep(3)
			# path3 = "/html/body/app-app-main/ng-component/app-shell/div/div/sls-domain/div/scrollable-tabset/div/div[1]/div/div/div[4]/tab-content/service-viewpoint/div/div[2]/div[2]/div[3]/job-list/div/ctm-common-grid-wrapper-downgraded/div/ag-grid-angular/div/div[6]/div/div/div[2]/div/div/div[1]/div[2]/div[3]/div/div/div[7]/label"
			# not_ok_clicked = driver.find_element("xpath", path3).click()
			# time.sleep(3)
			# path4 = "/html/body/app-app-main/ng-component/app-shell/div/div/sls-domain/div/scrollable-tabset/div/div[1]/div/div/div[4]/tab-content/service-viewpoint/div/div[2]/div[2]/div[3]/job-list/div/ctm-common-grid-wrapper-downgraded/div/ag-grid-angular/div/div[6]/div/div/div[1]/span/i"
			# remove_filter_option = driver.find_element("xpath", path4).click()
			# time.sleep(3)

			if apps+'.png' not in ss_list:
				# minimize_arrow = driver.find_element("xpath", "//*[@class='d-icon-arrow_right']").click()
				# minimize_arrow_path = "/html/body/app-app-main/ng-component/app-shell/div/div/sls-domain/div/scrollable-tabset/div/div[1]/div/div/div[4]/tab-content/service-viewpoint/div/div[2]/div[3]/job-details/div[1]/div[3]/span"
				# minimize_arrow_path = "/html/body/app-app-main/ng-component/app-shell/div/div/sls-domain/div/scrollable-tabset/div/div[1]/div/div/div[5]/tab-content/service-viewpoint/div/div[2]/div[3]/job-details/div[1]/div[2]/span"
				# minimize_arrow = driver.find_element("xpath", minimize_arrow_path).click()

				time.sleep(3)
				print(apps)
				ss = driver.save_screenshot("D:/Users/HGautam3/Projects/HMD Support/Updated Monitoring/Updated_Monitoring_Automation/sceenshots/{0}.png".format(apps))

				# img = "D:/Users/SSayed1/PycharmProjects/HMD/monitoring_automation/sceenshots/1EUSS-MD&D ETHICON US SALES DATA WAREHOUSE PROD-Contract.png"
				img = "sceenshots/{0}.png".format(apps)
				# kit.sendwhats_image("J6ahcZQ0iiO312PU8dXOIb", img, apps)
				# pg.press("enter")

			else:
				ss = driver.save_screenshot("Repeat/{0}.png".format(apps))
				img = "D:/Users/HGautam3/Projects/HMD Support/Updated Monitoring/Updated_Monitoring_Automation/Repeat/{0}.png".format(apps)
				# kit.sendwhats_image("J6ahcZQ0iiO312PU8dXOIb", img, apps)
				# pg.press("enter")
			time.sleep(3)
			# services = driver.find_element("xpath", "//*[@id='servicesTabDiv']").click()

			# account_sid = "AC955bea3a05afba5079c97b726a377bfb"
			# auth_token = "f9b6c24d422e9d75a9abaf8e951a94a0"
			# client = Client(account_sid, auth_token)
			# message = client.messages.create(
			# 	from_='whatsapp:+14155238886',
			# 	body=apps,
			# 	# media_url=["D:/Users/SSayed1/PycharmProjects/HMD/monitoring_automation/test_{0}.png".format(i)],
			# 	to='whatsapp:+918792564177')

			close_tab = driver.find_element("xpath", "//*[contains(@class, 'd-icon-cross') and contains(@class, 'ng-scope')]").click()
			time.sleep(3)
			refresh = driver.find_element("xpath", "//*[@id='manualRefreshButton']").click()
			time.sleep(3)
	print('End Time',datetime.now() )

# sched.start()
main()