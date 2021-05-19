import requests
import json
from bs4 import BeautifulSoup

def api_obtainer():
	s=requests.session()
	phone=input("input your number in international format.example=+980987654321,+1098765432. Enter:")
	send_password=s.post('https://my.telegram.org/auth/send_password',data={"phone":phone})
	try:
		random_hash=json.loads(send_password.text)["random_hash"]
	except:
		print("Something went wrong....\nPlease check your number.")
		exit(1)
	code=input("check your telegram and Enter The Code: ")
	login=s.post("https://my.telegram.org/auth/login",data={"phone":phone,"password":code,"random_hash":random_hash})
	if login.text != "true":
		print("Something went wrong....\nPlease check your code.")
		exit(1)
	check_condition=s.get("https://my.telegram.org/apps")
	soup=BeautifulSoup(check_condition.content,"html.parser")
	if soup.title.get_text() == "App configuration":
		forms=soup.find_all(class_="form-control input-xlarge uneditable-input")
		api_obtainer.api_id,api_obtainer.api_hash=forms[0].get_text(),forms[1].get_text()
	if soup.title.get_text() == "Create new application":
		config_app=s.post("https://my.telegram.org/apps/create",data={"hash":soup.input["value"],"app_title":"Telethon[Persian]","app_shortname":"Telethon[Persian]","app_platform":"android"})
		result=s.get("https://my.telegram.org/apps")
		soup=BeautifulSoup(result.content,"html.parser")
		forms=soup.find_all(class_="form-control input-xlarge uneditable-input")
		api_obtainer.api_id,api_obtainer.api_hash=forms[0].get_text(),forms[1].get_text()
	return api_obtainer.api_id,api_obtainer.api_hash

#By Telethon[Persian]
	
print(api_obtainer())