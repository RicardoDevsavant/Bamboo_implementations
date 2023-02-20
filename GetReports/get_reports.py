import os
import requests
import sqlalchemy
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import select
from TablesDataBase import CPA_BD, Employee
from sqlalchemy.exc import SQLAlchemyError

class BambooReports():
    '''   
        Get and process the data from the Bamboo Reports.
            
        Parameters
        ----------
        You must have the .env file in your folder with all the necessary credentials
        reports: Dict
            You should pass the number of the report that you want to update into DevSavant DB 

        Returns
        -------
        None

    '''
    def __init__(self, reports:dict) -> None:
        self.reports = reports
        load_dotenv()
        self.url = '{}://{}:{}@{}:{}/{}'.format(os.getenv('GCP_DRIVER_DB'), 
                                                os.getenv('GCP_USER_DB'),
                                                os.getenv('GCP_PWD_DB'),
                                                os.getenv('GCP_SRVR_DB'),
                                                os.getenv('GCP_PORT_DB'),
                                                os.getenv('GCP_NAME_DB'))
        self.GCP_OPEN_KEY = os.getenv('GCP_OPEN_KEY')
        self.token = os.getenv('API_KEY')

    def get_bamboo_report_data(self, _id:int):
        url = "https://api.bamboohr.com/api/gateway.php/devsavant/v1/reports/{}?format=json&fd=no&onlyCurrent=false".format(_id)
        headers = {
            "Accept": "application/json"
        }
        self.response = requests.get(url,
                                auth=(TOKEN, 'DevSavant'), 
                                headers=headers)
        self.response.raise_for_status()    
        if self.response.status_code != 204:
            print('Request for {} runing successfuly'.format(self.response['title']))
        else: 
            pass 
            # re-schedule the time to run the report        
        return self.response.json()
    
    def look_fields_names(self, _id:str) -> list:
        fields = self.response.json()['fields']
        columns = []
        for field in fields:
            columns.append(field['name'])
        return columns

    def get_employee_data(self):
        data = pd.DataFrame(self.response.json()['Employee'])
        data.colums = self.look_fields_names()
    
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
        
if __name__  == '__main__':
    pass