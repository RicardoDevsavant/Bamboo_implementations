# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 14:54:00 2022

@author: Devsavant
"""

from ctypes import *
CDLL(r"C:\Users\Devsavant\miniconda3\Lib\site-packages\confluent_kafka.libs\librdkafka-09f4f3ec.dll")
from confluent_kafka import Consumer
import json
from Bamboo_webhook import Bamboo_WebHooks
from TablesDataBase import CPA_BD, CPA_bd_fecha_ini, CPA_payroolt, CPA_customers, Employee


def call_db(response):
    '''
        Connect to the DB and send the queued information.

        Parameters
        ----------
        response: API request response (PUT/POST/GET)

        Returns
        -------
        message: Process Status
            String
    '''
    process = Bamboo_WebHooks(response)
    process.connect_postgres()   
    try:
        print('Update process has run successfully')
        process.update_values(Employee, Employee.id_employee, response['id_employee'], response)
        message = 'Success'
    except:
        try:
            print('Insert process has run successfully')
            process.insert_values(Employee, response)
            message = 'Success'
        except:
            message = 'Something went wrong with the connection'
    finally:
        return message
    
def consumer():
    '''
    
    '''
    consumer = Consumer({"bootstrap.servers": "34.28.76.134:9092",
                        "group.id": "my_consumer_group",
                        "auto.offset.reset": "earliest",
                        "enable.auto.commit": False})
    consumer.subscribe(['queuing.dcp.bamboo'])
    try:
        while True:
            msg = consumer.poll(1.0)
            print(f"Consuming from kafka - {msg}")
            if msg is None:
                continue
            elif msg.error():
                print(f'Msg error from kafka {msg.error()}')
            else:
                response = json.loads(msg.value().decode('utf-8'))
                print(response)
                message = call_db(response)
                if message == 'Success':
                    consumer.commit() # Que no se haga commit hasta que se halla guardado el dato en BD
                else:
                    pass 
    except KeyboardInterrupt:
        pass
    except KafkaException as e:
        print('Exception kafka manager consumer {}'.format(e))
    except KafkaError as e:
        print('Error kafka manager consumer {}'.format(e))
    except Exception as e:
        print(e)
    finally:
        consumer.close()
        
if __name__ == '__main__':
    consumer()
