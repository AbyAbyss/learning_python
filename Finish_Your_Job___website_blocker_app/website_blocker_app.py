# change hosts_temp to hosts_temp in line 29 and 37 to start blocking

import time
from datetime import datetime as dt

hosts_temp = "hosts"  # For  testing
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com"]
while True:
	print("Websites that will be blocked are: " + str(website_list))
	user_input = input("\n\nEnter 'add' to add Websites(separate with spaces only) else press 'Enter' to start blocking: ")
	if user_input == 'add':
		new_website = input("\nEnter the website: ")
		website_list.extend(new_website.split(' '))
	else:
		print("\nWebsites that will be blocked are: " + str(website_list))
		break

print("Set timer to block('Hour must be greater than or equal to present hour')\n\nPresent Hour is: " + str(dt.now().hour))

start_time = int(input("\nEnter start time: "))
end_time = int(input("Enter end time: "))
total_working_hours = end_time - start_time

while True:
	if dt(dt.now().year, dt.now().month, dt.now().day, start_time) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, end_time):
		print("Working Hours...from: {0} and ends at {1}".format(start_time, end_time))
		with open(hosts_temp, 'r+') as file:
			content = file.read()
			for website in website_list:
				if website in content:
					pass
				else:
					file.write(redirect + " " + website + "\n")
	else:
		with open(hosts_temp, 'r+') as file:
			content = file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
			file.truncate()
		
		if dt.now().hour > start_time:
			start_time = end_time + 1
			end_time = end_time + total_working_hours + 1
		print("Free Time..Next Working Hour starts from {0}".format(start_time))
	time.sleep(5)
