import requests
import os 
from flask import Flask
phone_no =Flask("Enter the number: ")

Data={"use":phone_no,"pass":"","ciso":"IN","IP":"49.36.237.230","IP_COUNTRY":"India","IPADDRESS":"49.36.237.230","GEOIP_COUNTRY_ISO":"IN","originalreferer":"https://m.indiamart.com/my/?ref=/","ph_code":"91","glusr_usr_ip":"49.36.237.230","duplicateEmailCheck":""}

r = requests.post('https://m.indiamart.com/ajaxrequest/identified/common/login', json=Data)
print()
print("printing status code: ", r.status_code)
print()
print("now we are loadind info of the user ")
print()
print(r.json())

