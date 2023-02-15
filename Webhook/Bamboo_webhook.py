# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 15:44:45 2022

@author: Devsavant
"""
from dotenv import load_dotenv
import os
import sqlalchemy
import pandas as pd
from sqlalchemy import select, insert, update
from TablesDataBase import CPA_BD, CPA_bd_fecha_ini, CPA_payroolt, CPA_customers, Employee
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, DataError, InternalError, OperationalError
import requests

class Bamboo_set_up():
    '''
        Create or modify Webhooks with Code.
            
        Parameters
        ----------
        None
            You must have the .env file in your folder with all the necessary credentials

        Returns
        -------
        None
    '''
    def __init__(self):
        load_dotenv()
        self.API_KEY = os.getenv('API_KEY')
        
    def create_webhook(self, monitorFields:list, postFields:dict, name:str, url_out:str): #
        url = "https://api.bamboohr.com/api/gateway.php/devsavant/v1/webhooks/"
        payload = {
            "monitorFields": monitorFields,
            "postFields": postFields,
            "name": name,
            "url": url_out,
            "format": "json"
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"        
        }
        response = requests.post(url,
                                auth=(self.API_KEY, 'DevSavant'),
                                headers=headers, json=payload)
        print(response.text)
        return response.text
    
    def update_webhook(self, monitorFields:list, postFields:dict, num:int, url_out:str):
        url = "https://api.bamboohr.com/api/gateway.php/devsavant/v1/webhooks/{}/".format(num)
        payload = {
            "monitorFields": monitorFields,
            "postFields": postFields,
            #"name": "basic",
            "url": url_out,
            "format": "json"
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": "Basic NGM4ZThlNzE4ODdlYjE2MTg3OGIyMDBiZmI2MTE5OGUyNzk1ZDAwODpEZXZTYXZhbnQ="
        }
        response = requests.put(url, json=payload, headers=headers)
        return response.text

class Bamboo_WebHooks():
    '''
        Create or modify Webhooks with Code.
            
        Parameters
        ----------
        None
            You must have the .env file in your folder with all the necessary credentials

        Returns
        -------
        None
    '''
    def __init__(self, req):
        load_dotenv()
        self.request = req
        self.url = '{}://{}:{}@{}:{}/{}'.format(os.getenv('GCP_DRIVER_DB'), 
                                                os.getenv('GCP_USER_DB'),
                                                os.getenv('GCP_PWD_DB'),
                                                os.getenv('GCP_SRVR_DB'),
                                                os.getenv('GCP_PORT_DB'),
                                                os.getenv('GCP_NAME_DB'))
        self.GCP_OPEN_KEY = os.getenv('GCP_OPEN_KEY')
        self.API_KEY = os.getenv('API_KEY')
        
    def test_conection(self):
        try:
            self.engine = sqlalchemy.create_engine(self.url, connect_args={'connect_timeout': 60})
            pd.read_sql_query(select(CPA_BD).where(CPA_BD.employee_code.in_(['77'])), self.engine)
            message = "Success"             
        except SQLAlchemyError as e:
            message = 'Error in DB conection: ' + str(e)
        except Exception as e:
            message = 'Somenthing went wrong: ' + str(e)
        finally:
            return message
        
    def connect_postgres(self):
        self.engine = sqlalchemy.create_engine(self.url)
        return self.engine

    def get_data_webhook(self):
        changedFields = self.request['employees'][0]['changedFields'] #We can use it to LOGS table.
        _data = {}
        for keys, vals in self.request['employees'][0]['fields'].items():
            _data[keys] = vals['value']
        id_client = self.request['employees'][0]['id']
        return id_client, _data

    def insert_values(self, nameTable, values): # must be values a tuple? 
        stmt= insert(nameTable).values(values)
        with self.engine.connect() as conn:
            try:
                conn.execute(stmt)
            except Exception as e:#IntegrityError:
                print('Duplicate data ' + str(e))
            except InternalError as e:
                print('Not data base connection ' + str(e))
            except DataError as error:
                print('Data Error ' + str(error))
            except Exception as e:
                print('Somenthing went wrong ' + str(e))
        print('insert_values was successfully')
    
    def update_values(self, nameTable, ObjectAtrib, filterValue:str, values:dict):        
        stmt = update(nameTable).where(ObjectAtrib==filterValue).values(values)
        with self.engine.connect() as conn:
            try:
                conn.execute(stmt)
            except IntegrityError:
                print(str(IntegrityError))
            except InternalError as e:
                print('Not data base connection ' + str(e))
            except DataError as error:
                print('Data Error ' + str(error))
            except Exception as e:
                print('Something went wrong ' + str(e))
        print('update_values was successfully')

if __name__ == '__main__':
    pass