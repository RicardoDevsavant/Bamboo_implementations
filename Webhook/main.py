"""
Created on Wed Dec 14 11:17:52 2022

@author: RichieHeredia Devsavant
"""
import json
from ctypes import *
CDLL(r"C:\Users\Devsavant\miniconda3\Lib\site-packages\confluent_kafka.libs\librdkafka-09f4f3ec.dll")
from flask import Flask,request,jsonify
from Bamboo_webhook import Bamboo_WebHooks
from TablesDataBase import CPA_BD, CPA_bd_fecha_ini, CPA_payroolt, CPA_customers, Employee
from datetime import datetime
from confluent_kafka import Producer
from uuid import uuid4

"""
This code is listen a WebHook From Bamboo usign an API 

"""

def ack_delivery(err, msg):
    '''
        Kafka Errors
    '''
    if err is not None:
        print("Failed to deliver message: {}".format(err))
    else:
        print("Produced record to topic {} partition [{}] @ offset {}".format(msg.topic(), msg.partition(), msg.offset()))

def transform_information(information:dict, id_):
    '''
        Get information from Bamboo and transform to DB acceptable values.
            
        Parameters
        ----------
        information : Client information when it has a modification. 
            Dictionary.
        id_ : Internal Client ID. 
            String.

        Returns
        -------
        Dict
            Post all the cleaned information.
    '''

    _rename = {'employeeNumber':'eeid',    
              'gender':'gender_id',
              'customNationalID#':'NationalID'}
        
    for key, value in _rename.items():
        try:
            information[value] = information.pop(key)
        except:
            pass
    
    _gender = {'Female': '2' , 'Male': '1'}
    for key, value in _gender.items():
        try:
            information['gender_id'] = int(information['gender_id'].replace(key, value))
        except:
            pass
    if information['gender_id'] == None: information['gender_id'] = 1
    information['id_employee'] = id_
    information['update_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    information =  {k.lower(): v for k, v in information.items()}
    return information

def kafka_line(_information):
    '''
        Get the cleaned information and sent to a queue in Kafka.
            
        Parameters
        ----------
        information : Client information when it has a modification. 
            Dictionary.

        Returns
        -------
        None
    '''
    producer = Producer({"bootstrap.servers": "34.28.76.134:9092"})
    # pram-1: Topic name, 
    producer.produce('queuing.dcp.bamboo', key=str(uuid4()), 
                     value=json.dumps(_information), on_delivery=ack_delivery)        
    producer.poll(0)
    producer.flush()
    return True
    

app = Flask(__name__)
@app.route("/", methods=['GET'])
def read_root():
  return jsonify({'message':'Hello From WEBHOOK API'})

#Webhook 7
@app.route("/create", methods=['POST'])
def basic_hello():
    print('Running Create... ')
    req = request.json    
    process = Bamboo_WebHooks(req)    
    id_client, temp_dict = process.get_data_webhook()
    temp_dict = transform_information(temp_dict, id_client)    
    message = process.test_conection()
    # Process to conect to the DB devSavant
    if message == 'Success':
        print('Conections Successfully, saving data in postgres... ')
        process.connect_postgres()
        process.insert_values(Employee, temp_dict)
        send_ = 'Data Updated in DB'
    else :
        print('Sending data to Kafka...\n')
        kafka_line(temp_dict)
        send_ = 'Data Saved in Kafka'
    return send_

# Webhook 8
@app.route("/updateEmployee", methods=['POST'])
def hello_world():
    req = request.json
    print('Running updateEmployee...')
    process = Bamboo_WebHooks(req)
    id_client, temp_dict = process.get_data_webhook()    
    temp_dict = transform_information(temp_dict, id_client)    
    message = process.test_conection()
    print(message)
    # Process to conect to the DB devSavant
    if message == 'Success':
        print('Conections Successfully, saving data in postgres... ')
        process.connect_postgres()        
        process.update_values(Employee, Employee.id_employee, id_client, temp_dict)
        send_ = 'Data Updated in DB'
    else :
        print('Sending data to Kafka...\n')
        kafka_line(temp_dict)
        send_ = 'Data Saved in Kafka'
    return send_

if __name__ ==  "__main__":
  app.run(debug=True,
          host='0.0.0.0',
          port=8080)
  