# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 14:58:24 2022

@author: Devsavant
"""

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Employee(Base):
    __tablename__ = "employee"
    __table_args__ = {"schema": "DCP"}
    id_employee = Column(Integer,  primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    gender_id = Column(String)
    dateofbirth = Column(Date)
    hiredate = Column(Date)
    update_date = Column(DateTime)
    terminationdate = Column(Date)
    nationalid = Column(Integer)
    workemail = Column(String)
    location = Column(String)
    workphone = Column(String)
    mobilephone = Column(Integer)
    status = Column(Integer)
    eeid = Column(Integer)

class CPA_BD(Base):
    __tablename__ = "cpa_bd"
    __table_args__ = {"schema": "CPA"}   
    employee_code = Column(Integer, primary_key=True)
    code_month = Column(String)
    customer_facing = Column(String)
    payroll = Column(String)
    customer = Column(String)
    manager = Column(String)
    project = Column(String)
    position = Column(String)
    date = Column(String)
    hours = Column(String)
    cost = Column(String)
    cost_payroll = Column(String)
    sales = Column(String)
    overhead = Column(String)
    year = Column(String)
    month = Column(String)
    sdops_type = Column(String)
    sdops_class = Column(String)
    upload_date = Column(String)   
    
    def __repr__(self):
        return f"User(employee_code={self.employee_code!r}, \
                    cost={self.cost!r}, cost_payroll={self.cost_payroll!r})"

class CPA_bd_fecha_ini(Base):
    __tablename__ = "cpa_bd_fecha_ini"   
    __table_args__ = {"schema": "CPA"}  
    payroll = Column(String)
    employee = Column(Integer, primary_key=True)
    sdops = Column(String)
    estado = Column(String)
    eliminado = Column(String)
    hire_date = Column(String)
    menu_date = Column(String)
    hours_worked_month = Column(String)
    sale_fp_pr = Column(String)
    fecha_de_salida = Column(String)
    upload_date = Column(String)    
   
    def __repr__(self):
        return f"User(employee_code={self.employee_code!r}, \
                    cost={self.cost!r}, cost_payroll={self.cost_payroll!r})"    
    
class CPA_payroolt(Base):
    __tablename__ = "cpa_payroolt"  
    __table_args__ = {"schema": "CPA"}  
    code = Column(Integer, primary_key=True)
    name = Column(String)
    department = Column(String)
    segment = Column(String)
    cost_payroll = Column(String)
    company_cost = Column(String)
    date = Column(String)
    month = Column(String)
    year = Column(String)
    type_qb = Column(String)
    upload_date = Column(String)    
   
    def __repr__(self):
        return f"User(employee_code={self.employee_code!r}, \
                    cost={self.cost!r}, cost_payroll={self.cost_payroll!r})"    

    
class CPA_registros_eliminados(Base):
    __tablename__ = "cpa_registros_eliminados"  
    __table_args__ = {"schema": "CPA"}  
    code = Column(Integer, primary_key=True)
    persona = Column(String)
    categoria = Column(String)
    ultimo_costo = Column(String)
    ultima_venta = Column(String)
    fecha_eliminacion = Column(String)
    comentario = Column(String)
    upload_date = Column(String)    
   
    def __repr__(self):
        return f"User(employee_code={self.employee_code!r}, \
                    cost={self.cost!r}, cost_payroll={self.cost_payroll!r})"    
    
    
class CPA_bd_full_price(Base):
    __tablename__ = "cpa_bd_full_price"
    __table_args__ = {"schema": "CPA"}  
    code_ini = Column(Integer, primary_key=True)
    code = Column(String)
    name = Column(String)
    full_price_sale = Column(String)
    full_cost = Column(String)
    tipo_de_costo = Column(String)
    date = Column(String)
    month = Column(String)
    year = Column(String)
    upload_date = Column(String)    
   
    def __repr__(self):
        return f"User(employee_code={self.employee_code!r}, \
                    cost={self.cost!r}, cost_payroll={self.cost_payroll!r})"  
    
class CPA_customers(Base):
    __tablename__ = "cpa_customers"   
    __table_args__ = {"schema": "CPA"}  
    code = Column(Integer, primary_key=True)
    customer = Column(String)
    addres = Column(String)
    contact = Column(String)
    contact_number = Column(String)
    
    def __repr__(self):
        return f"User(employee_code={self.employee_code!r}, \
                    cost={self.cost!r}, cost_payroll={self.cost_payroll!r})"  
    
    
    
    
    
    