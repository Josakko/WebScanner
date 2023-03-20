import requests
import validators
from termcolor import colored

print("-" * 50)
web = input("> Enter website url: ")


while True:
    if validators.url(web):
        response = requests.get(web)
        print("-" * 50)
        break
    else:
        print(colored("[-] Invalid URL, please try again!", "red"))
        web = input("> Enter website url: ")

response = requests.get(web)

output = ""
output += response.text + "\n"
if (response.status_code == 200):
    response = requests.get(web+'/admin.php')

    output += "Admin login page status code: " + str(response.status_code) + "\n"
    if(response.status_code == 200):
        output += "Vulnerable\n"
        print(colored("Vulnerable", "green"))
        print(colored("Initial request status code: " + str(response.status_code), "green"))
    else:
        output += "Non-vulnerable\n"
        print(colored("Non-vulnerable", "red"))
        print(colored("Initial request status code: " + str(response.status_code), "red"))
else:
    output += "Initial request status code: " + str(response.status_code) + "\n"
    output += "Failure\n"

with open("log.txt", "w", encoding="utf-8") as f:
    f.write(output)

