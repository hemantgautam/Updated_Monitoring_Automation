"""

Pending To Do - 
- Schedule cron job at 9:40 am ist time, to remove all the files from Ended_Not_OK_Files folder
- Reduce image size before exporting
- remove index from exported image dataframe
- Unistall unwanted python packages and create requirements.txt file
- change all variables/folders names with the correct names
- Add proper comment everywhere
- run pylint once dev is completed

"""

import os
import time
from datetime import datetime, timedelta
from time import sleep
import csv
import base64
from twilio.rest import Client
import pandas as pd
import dataframe_image as dfi

import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from selenium import webdriver
import edgedriver_autoinstaller
from selenium.webdriver.common.keys import Keys

from twilio.rest import Client
import pywhatkit as kit
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from twilio.rest import Client
from openpyxl.workbook import Workbook
from msedge.selenium_tools import Edge, EdgeOptions
from emaill import Mail
from whatsapp_api import WhatsApp

sched = BlockingScheduler()

def main():
	try:
		print('Start Time', datetime.now())
		ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
		options = EdgeOptions()
		options.use_chromium = True
		options.add_argument("headless")
		options.add_argument("disable-gpu")

		options.add_experimental_option("prefs", {
			"download.default_directory": ROOT_DIR + "\Moniter_Jobs",
			"download.prompt_for_download": False,
			"download.directory_upgrade": True,
			"safebrowsing.enabled": True
		})
		options.add_argument("-inprivate")

		driver = Edge(executable_path= ROOT_DIR + "\msedgedriver.exe", options=options)
		driver.get('https://itsusralsp06834.jnj.com:8443/ControlM/')

		user_name = driver.find_element("xpath", "//*[@id='login-user-name']")
		password = driver.find_element("xpath", "//*[@id='login-user-password']")


		user_name.send_keys("cpatil11")
		password.send_keys("Chana@1811")
		password.send_keys(Keys.ENTER)
		time_sleep()
		mont = driver.find_element("xpath", "//*[@id='SelfServiceDomainTabHeader']").click()
		time_sleep()
		services = driver.find_element("xpath", "//*[@id='servicesTabDiv']").click()
		time_sleep()
		filter = driver.find_element("xpath", "//*[@id='servicesFilterDropDown']").click()
		time_sleep()
		ended_not_ok = driver.find_element("xpath","/html/body/app-app-main/ng-component/app-shell/div/div/sls-domain/div/scrollable-tabset/div/div[1]/div/div/div[3]/tab-content/sls-services/div/div[2]/div[1]/div/div[1]/div[1]/ul/li[3]/span[1]").click()
		time_sleep()

		path_for_count = "/html/body/app-app-main/ng-component/app-shell/div/div/sls-domain/div/div[2]/a/div/span[2]/flat-status-chart/div/div/div[1]"
		size_variable = driver.find_element("xpath", path_for_count)
		size = int(size_variable.text)
		print("Size: ", size)
		time_sleep()
		button = driver.find_element("xpath", "//*[@id='servicesListViewButton']").click()

		time_sleep()

		excluded_projects =['1MDPD-DEPUY SYNTHES - US - BIDW - ODH PRD-DEPUYBI']
		# size = 0
		for i in range(1,size+1):
			time_sleep()

			#check code for decommisioned applications
			apps_name_path= "/html/body/app-app-main/ng-component/app-shell/div/div/sls-domain/div/scrollable-tabset/div/div[1]/div/div/div[3]/tab-content/sls-services/div/div[2]/div[1]/div/div[2]/sls-services-list/div/ctm-common-grid-wrapper-downgraded/div/ag-grid-angular/div/div[2]/div[1]/div[3]/div[2]/div/div/div[{0}]/div[3]/service-name-cell-renderer/div/a".format(i)
			apps_name = driver.find_element("xpath", apps_name_path)
			apps = apps_name.get_attribute('initial-text')
			if apps not in excluded_projects:
				ended_not_ok_project_link = "/html/body/app-app-main/ng-component/app-shell/div/div/sls-domain/div/scrollable-tabset/div/div[1]/div/div/div[3]/tab-content/sls-services/div/div[2]/div[1]/div/div[2]/sls-services-list/div/ctm-common-grid-wrapper-downgraded/div/ag-grid-angular/div/div[2]/div[1]/div[3]/div[2]/div/div/div[{0}]/div[3]/service-name-cell-renderer/div/a".format(i)
				time_sleep()
				driver.find_element("xpath", ended_not_ok_project_link).click()
				time_sleep()
				list_view_click = driver.find_element("xpath", "//*[@id='viewpointJobListViewbtn']").click()
				time_sleep()

				# Xpath for exporting the Ended Not ok Jobs for each project
				path5 = "//*[@id='export-csv-view-point-button']"
				click_export = driver.find_element("xpath", path5).click()
				time_sleep()

				# driver.implicitly_wait(10)

				close_tab = driver.find_element("xpath", "//*[contains(@class, 'd-icon-cross') and contains(@class, 'ng-scope')]").click()
				# driver.implicitly_wait(10)
				refresh = driver.find_element("xpath", "//*[@id='manualRefreshButton']").click()
				time_sleep()

		print("loop is completed")

		input_folder = ROOT_DIR + "\Moniter_Jobs"

		csv_files = [file for file in os.listdir(input_folder) if file.endswith('.csv')]
		email_whatsapp_flag = False
		for file in csv_files:
			app_name = file.split(".")
			file_path = os.path.join(input_folder, file)
			df = pd.read_csv(file_path, usecols = ['Job Name','Status', 'Start Time', 'End time', 'Folder', 'Member/File name'])
			if len(df) > 0:

				# If time is less than 12:10am EST(9:40am ist) then we need to consider previous day of failed jobs, and after 9:40am IST, consider current day of failed jobs
				now = datetime.now()
				today9_40am = now.replace(hour=9, minute=40, second=0, microsecond=0)
				today_date = datetime.today()
				if now < today9_40am:
					yster_day = today_date - timedelta(days=1)
					today_date = yster_day.strftime('%Y-%m-%d')
				else:
					today_date = today_date.strftime('%Y-%m-%d')


				df['Start Time'] = pd.to_datetime(df["Start Time"]).dt.normalize()
				# today_date = datetime.today().strftime('%Y-%m-%d')
				# # import pdb; pdb.set_trace()

				filtered_df = df[(df['Status'] == 'Ended Not OK') & (df['Start Time'] == today_date)]

				# Check the difference in filtered_df and csv file present inside the Ended_Not_OK_Files, If both df have same rows present, do not create image

				# check if Ended Not OK CSV file is already present for application, then read the dataframe and compare with the current DF

				if len(filtered_df) > 0:
					app_orignl_name = app_name[0].split("_jobs_")
					existing_file = ROOT_DIR + "/Ended_Not_OK_Files/{0}.csv".format(app_orignl_name[0])
					is_exist = os.path.exists(existing_file)
					if is_exist:
						df_existing_file = pd.read_csv(existing_file)
						final_df = filtered_df[~filtered_df["Job Name"].isin(df_existing_file["Job Name"])]
						if len(final_df) > 0:
							email_whatsapp_flag = True
							os.remove(ROOT_DIR + "/Ended_Not_OK_Files/{0}.csv")
							filtered_df.to_csv(ROOT_DIR + "/Ended_Not_OK_Files/{0}.csv".format(app_orignl_name[0]), index=False)

							files_image_df = filtered_df.style.set_table_styles([dict(selector='th',props=[('text-align','center'),('background-color','#40466e'),('color','white')])])
							files_image_df.set_properties(**{'text-align':'center'})
							pd.set_option('colheader_justify','center')
						
							file_name = ROOT_DIR + r"/Ended_Not_OK_Images/"+ app_orignl_name[0]+ ".png"
							dfi.export(files_image_df, file_name)
					else:
						email_whatsapp_flag = True
						filtered_df.to_csv(ROOT_DIR + "/Ended_Not_OK_Files/{0}.csv".format(app_orignl_name[0]), index=False)

						files_image_df = filtered_df.style.set_table_styles([dict(selector='th',props=[('text-align','center'),('background-color','#40466e'),('color','white')])])
						files_image_df.set_properties(**{'text-align':'center'})
						pd.set_option('colheader_justify','center')

						file_name = ROOT_DIR + r"/Ended_Not_OK_Images/"+ app_orignl_name[0]+ ".png"
						dfi.export(files_image_df, file_name)		

		# Send all the Ended NOt Ok Images to Gmail
		if email_whatsapp_flag:
			mail_obj = Mail()
			respo = mail_obj.send_success_mail()
			if respo:
				print("Email Sent Sucessfully!!")

			# Send alert message to whatsapp
			whatsapp_obj = WhatsApp()
			wa_response= whatsapp_obj.send_whatsapp_text()
			if wa_response != "":
				print(wa_response, "Whatsapp Alert is sent!!")

		# Delete Csv file and images from Moniter_Jobs and Ended_Not_OK_Images
		files_to_delete = ROOT_DIR + "\Moniter_Jobs"
		for f in os.listdir(files_to_delete):
			os.remove(os.path.join(files_to_delete, f))
		
		images_to_delete = ROOT_DIR + "\Ended_Not_OK_Images"
		for f in os.listdir(images_to_delete):
			os.remove(os.path.join(images_to_delete, f))

		print('End Time',datetime.now())

	except Exception as error:
		print("===============Exception==============")
		# # Send Failure email
		# mail_obj = Mail()
		# respo = mail_obj.send_exception_mail(error)

def time_sleep():
	time.sleep(5)


# main()

# Schedules the job_function to be executed Monday through Friday at between 12-16 at specific times.   
sched.add_job(main, 'interval', seconds=1200)

# Start the scheduler
sched.start()