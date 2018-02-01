import requests
import time
import random

print ("[" + (time.strftime("%H:%M:%S")) + "]" + " ********************************************")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + " *            747WAREHOUSE Bot              *")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + " *          Developed by @mxnnxt            *")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + " ********************************************\n")

email = str(input("[" + (time.strftime("%H:%M:%S") + "]" + " - Enter your Gmail: ")))

########################################################
#                                                      #
#                     EDIT BELOW                       #
#                                                      #
########################################################

firstName = "John"
lastName = "Doe"
gender = "M"
birthMonth = "06"
birthYear = "2000"
birthDay = "12"

########################################################
#                                                      #
#           **DO NOT EDIT BELOW THIS POINT**           #
#                                                      #
########################################################


session = requests.session()

headers = {
	"accept":"application/json, text/javascript, */*; q=0.01",
	"accept-encoding":"gzip, deflate, br",
	"accept-language":"en-US,en;q=0.9",
	"content-type":"application/json; charset=UTF-8",
	"origin":"http://www.adidas.com",
	"referer":"http://www.adidas.com/us/mi_ultraboost",
	"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
	"connection": "keep-alive"
}


times = int(input("[" + (time.strftime("%H:%M:%S") + "]" + " - Enter the number of entries you would like to enter: ")))


class GmailDotEmailGenerator:
  def __init__(self, email):
    self.__username__, self.__domain__ = email.split('@')
  def generate(self):
    return self.__generate__(self.__username__, self.__domain__)
  def __generate__(self, username, domain):
    emails = list()
    username_length = len(username)
    combinations = pow(2, username_length - 1)
    padding = "{0:0" + str(username_length - 1) + "b}"
    for i in range(0, combinations):
        bin = padding.format(i)
        full_email = ""

        for j in range(0, username_length - 1):
            full_email += (username[j]);
            if bin[j] == "1":
                full_email += "."
        full_email += (username[j + 1])
        emails.append(full_email + "@" + domain)
    return emails

def raffle(emails):
	for email in \
		(GmailDotEmailGenerator(emails).generate())[:times]:


		print("[" + (time.strftime("%H:%M:%S")) + "]" + " - ENTERING RAFFLE . . .")
		global session
		

		url = "https://brand.campaign.adidas.com/api/scv/subscription/newsletter/create"

		payload = '{"email":"'+email+'","firstName":"'+firstName+'","lastName":"'+lastName+'","gender":"'+gender+'","datepicker":"'+(birthMonth.replace('0',''))+'/'+(birthDay.replace('0',''))+'/'+birthYear+'","dateOfBirth":"'+birthYear+'-'+birthMonth+'-'+birthDay+'","legalCheckbox":"1","countryOfSite":"US","newsletterDomain":"United States","newsletterLanguage":"en","newsletterTypeId":"40000","source":"543452387","eventType":"adi_eCom_Basketball_adidas747","sendMail":"Y","consents":{"consent":[{"consentType":"AMF","consentValue":"Y","consentVersion":"ADIUS_VER_1"}]}}'
	
		res = session.post(url, data=payload, headers=headers)
		time.sleep(1/2)
		#print(res.text)

		if "true" in res.text:
			print("[" + (time.strftime("%H:%M:%S")) + "]" +" - SUCCESSFULLY ENTERED "+email+"\n")
		else:
			print("[" + (time.strftime("%H:%M:%S")) + "]" +" - ERROR COULD NOT ENTER "+email+"\n")


raffle(email)
