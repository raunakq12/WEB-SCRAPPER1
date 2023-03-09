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

login_form_url=(login_details['crawlScanProfile']['crawlScanSettings']['authSettings']['authData']['normalAuth']['authValues']['login_form_url'])

s = requests.Session()

# Basic Authentication
flag=0
response = s.get(url, auth=HTTPBasicAuth(Busername,Bpassword))
r=response.text
soup = BeautifulSoup(r, 'lxml')
for link in soup.findAll('a'):
    if "//" not in link.get('href'):
        if "login.jsp" in link.get('href'):
            flag=1
            print("--------------------------------------------------------------------------------------------------- !! login page detected ")
            print("crawling site ----->>>>>",url+link.get('href').replace('/','',1))
            print("---------------------------------------------------------------------------------------------------")
        else:
             print("crawling site ----->>>>>",url+link.get('href').replace('/','',1))
    else:
        print("crawling site ----->>>>>",link.get('href'))

print("\n")
print("\n")
print("\n")


#############################################

# print(s.cookies)

s.post(
     login_form_url,
     data={
        "uid": Ausername,
        "passw": Apassword,
        "btnSubmit": "Login",
    },
    auth=HTTPBasicAuth(Busername,Bpassword),
)

# print(s.cookies)

res = s.get("https://m1.forenzythreatlabs.com/bank/main.jsp", auth=HTTPBasicAuth(Busername,Bpassword))
soup_N=BeautifulSoup(res.text, 'html.parser')
print("BANK ACCOUNTS ---------------->",soup_N.find_all('option'))
for link in soup.findAll('a'):
     print("crawling site ----->>>>>",link.get('href'))


"""
loginresponse = s.get(login_url, auth=HTTPBasicAuth(Busername,Bpassword))
login_O=BeautifulSoup(loginresponse.text,"lxml")
login_form = soup.find("form")
form_data = {}

for input_field in login_form.find_all("input"):
        if input_field.get("type") == "hidden":
        # Skip hidden fields
            continue
        form_data[input_field.get("name")] = input_field.get("value", "")

form_data["uid"] = Ausername
form_data["passw"] = Apassword

logiresponse = s.post(login_form["action"], data=form_data)

print(BeautifulSoup(loginresponse.content), 'lxml')
"""