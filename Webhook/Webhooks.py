# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 11:23:59 2022

@author: Devsavant
"""


class Webhooks():
    def __init__(self, url, out_url):
        self.url = url
        self.out_url = out_url
        self.headers = {"accept": "application/json",
                        "content-type": "application/json"}
    def create_employee(self):
        payload = {
            "monitorFields": ['employeeNumber'],
            "postFields": {'employeeNumber':'employeeNumber', "hireDate":"hireDate", 
                           "terminationDate":"terminationDate", 'status':'status', 
                           'gender':'gender', 'workEmail':'workEmail' ,
                           'mobilePhone': 'mobilePhone', 'workPhone':'workPhone',
                           'firstName':'firstName', 'lastName':'lastName','location':'location', 
                           'dateOfBirth':'dateOfBirth', 'customNationalID#':'customNationalID#'},
            "name": "Webhook-create",
            "url": out_url + str('/create'),
            "format": "json"
        }
        return payload
    def update_employee(self):
        payload = {
            "monitorFields":  ['hireDate', 'status','gender', 
                               'workEmail','mobilePhone','workPhone',
                               'firstName','lastName', 'location','dateOfBirth'],
            
            "postFields": {"hireDate":"hireDate", "terminationDate":"terminationDate", 
                           'status':'status', 'gender':'gender', 'workEmail':'workEmail' ,
                           'mobilePhone': 'mobilePhone', 'workPhone':'workPhone',
                           'firstName':'firstName', 'customNationalID#':'customNationalID#', 
                           'lastName':'lastName','location':'location', 
                           'dateOfBirth':'dateOfBirth'},
            
            "name": "Webhook-employee",
            "url": url_out + str('/updateEmployee'),
            "format": "json"
        }
        return payload
    
    
        
        
# Almacenar los campos que lee cada Webhook para que pueda ser escalable.        

#%%

import requests # number 7
out_url = 'https://1a69-181-58-38-151.ngrok.io'

url = "https://api.bamboohr.com/api/gateway.php/devsavant/v1/webhooks/7/"

payload = {
    "monitorFields": ['employeeNumber'],
    "postFields": {'employeeNumber':'employeeNumber', "hireDate":"hireDate", 
                   "terminationDate":"terminationDate", 'status':'status', 
                   'gender':'gender', 'workEmail':'workEmail' ,
                   'mobilePhone': 'mobilePhone', 'workPhone':'workPhone',
                   'firstName':'firstName', 'lastName':'lastName','location':'location', 
                   'dateOfBirth':'dateOfBirth', 'customNationalID#':'customNationalID#'},
    "name": "Webhook-create",
    "url": out_url + str('/create'),
    "format": "json"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}
response = requests.put(url,
                        auth=('4c8e8e71887eb161878b200bfb61198e2795d008', 'DevSavant'), 
                        headers=headers, json=payload)
print(response.text)


#%% number 8 Tabla Employee
import requests
url = "https://api.bamboohr.com/api/gateway.php/devsavant/v1/webhooks/8/"
url_out= "https://1a69-181-58-38-151.ngrok.io"
payload = {
    "monitorFields":  ['hireDate', 'status','gender', 'terminationDate', 'customNationalID#',
                       'workEmail','mobilePhone','workPhone',
                       'firstName','lastName', 'location','dateOfBirth'],
    
    "postFields": {"hireDate":"hireDate", "terminationDate":"terminationDate", 
                   'status':'status', 'gender':'gender', 'workEmail':'workEmail' ,
                   'mobilePhone': 'mobilePhone', 'workPhone':'workPhone',
                   'firstName':'firstName', 'customNationalID#':'customNationalID#', 
                   'lastName':'lastName','location':'location', 
                   'dateOfBirth':'dateOfBirth'},
    
    "name": "Webhook-employee",
    "url": url_out + str('/updateEmployee'),
    "format": "json"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}
response = requests.put(url,
                        auth=('4c8e8e71887eb161878b200bfb61198e2795d008', 'DevSavant'), 
                        headers=headers, json=payload)
print(response.text)



#%%
import requests
url = "https://api.bamboohr.com/api/gateway.php/devsavant/v1/webhooks/"
url_out= "https://d6c6-2800-e2-9080-f8e-bc90-26de-2229-5e40.ngrok.io"
payload = {
    "monitorFields":  ['customNetPayments1','customCompanyCost1',
                       'customSalary','customGrossCompensation',
                       'customPaySchedule'],
    
    "postFields": {"customNetPayments1":"customNetPayments1", 
                   "customCompanyCost1":"customCompanyCost1", 
                   'customSalary':'customSalary', 
                   'customGrossCompensation':'customGrossCompensation', 
                   'customPaySchedule':'customPaySchedule' },
    "name": "Webhook-money",
    "url": url_out + str('/updateCPA'),
    "format": "json"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}
response = requests.post(url,
                        auth=('4c8e8e71887eb161878b200bfb61198e2795d008', 'DevSavant'), 
                        headers=headers, json=payload)
print(response.text)




#%% Update 
#%% Update Webhook

import requests

url = "https://api.bamboohr.com/api/gateway.php/devsavant/v1/webhooks/6/"

payload = {
    "monitorFields": ["division", "jobTitle"],
    "postFields": {"division": "division",
                   'jobTitle':'jobTitle',
                   'employeeNumber':'employeeNumber'},
    "name": "basic",
    "url": "https://0c73-181-58-38-151.ngrok.io",
    "format": "json"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    #"authorization": "Basic NGM4ZThlNzE4ODdlYjE2MTg3OGIyMDBiZmI2MTE5OGUyNzk1ZDAwODpEZXZTYXZhbnQ="
}

response = requests.put(url, 
                        auth=('4c8e8e71887eb161878b200bfb61198e2795d008', 'DevSavant'),
                        json=payload, headers=headers)

print(response.text)



#%% GEt supost fields





url = "https://api.bamboohr.com/api/gateway.php/devsavant/v1/meta/tables/"

headers = {
    "Accept": "application/json",
    "authorization": "Basic NGM4ZThlNzE4ODdlYjE2MTg3OGIyMDBiZmI2MTE5OGUyNzk1ZDAwODpEZXZTYXZhbnQ="
}

response = requests.get(url, headers=headers)
fields = response.json()

tables = {}
for x in range(len(fields)):
    dict_tempo = {}
    for j in fields[x]['fields']:
        dict_tempo[j['alias']] = j['name']
    tables[str(fields[x]['alias'])] = dict_tempo


