import requests
import json
import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup

 

with open('crawlingFeeds.json', 'r') as json_file:
	login_details = json.load(json_file)
Ausername=(login_details['crawlScanProfile']['crawlScanSettings']['authSettings']['authData']['normalAuth']['authValues']['user_data'])
Apassword=(login_details['crawlScanProfile']['crawlScanSettings']['authSettings']['authData']['normalAuth']['authValues']['user_pwd_data'])
Busername=(login_details['crawlScanProfile']['crawlScanSettings']['authSettings']['authData']['basicAuth']['authValues']['basic_auth_usrn'])
Bpassword=(login_details['crawlScanProfile']['crawlScanSettings']['authSettings']['authData']['basicAuth']['authValues']['basic_auth_pwd'])
url=(login_details['crawlScanProfile']['urlFQDN'])
login_url=(login_details['crawlScanProfile']['crawlScanSettings']['authSettings']['authData']['normalAuth']['authValues']['login_url'])

# Basic Authentication

response = requests.get(url, auth=HTTPBasicAuth(Busername,Bpassword))
r=response.text
soup = BeautifulSoup(r, 'lxml')

for link in soup.findAll('a'):
    if "//" not in link.get('href'):
        print("crawling site ----->>>>>",url+link.get('href').replace('/','',1))
    else:
        print("crawling site ----->>>>>",link.get('href'))

loginpage = soup.find("a", href="/login.jsp")

if loginpage:
    print("LOGIN PAGE FOUND",loginpage.get('href'))
   
        
else:
    print("NOT FOUND")


#############################################


session = requests.Session()
loginresponse = session.get(login_url)
login_form = soup.find("form")
form_data = {}
for input_field in login_form.find_all("input"):
        if input_field.get("type") == "hidden":
        # Skip hidden fields
            continue
        form_data[input_field.get("name")] = input_field.get("value", "")
form_data["username"] = Ausername
form_data["password"] = Apassword
logiresponse = session.post(login_url, data=form_data)
if loginresponse.url == login_url:
        soup = BeautifulSoup(loginresponse.content, "html.parser")
        print(soup.prettify())