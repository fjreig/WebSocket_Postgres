from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float
from sqlalchemy import Date, cast, extract, func
from datetime import datetime
import pandas as pd
import json

from app.database import Base, session, engine

class AARR(Base):
    __tablename__ = "aarr"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime)
    v1 = Column(Float)
    i1 = Column(Float)
    pa1 = Column(Float)
    v2 = Column(Float)
    i2 = Column(Float)
    pa2 = Column(Float)
    v3 = Column(Float)
    i3 = Column(Float)
    pa3 = Column(Float)
    pa = Column(Float)
    fp = Column(Float)
    frec = Column(Float)
    v12 = Column(Float)
    v23 = Column(Float)
    v31 = Column(Float)
    ea_import = Column(Float)
    eq_import = Column(Float)
    ea_export = Column(Float)
    eq_export = Column(Float)

def get_all():
    result = session.query(AARR).limit(5).all()
    return(result)

def Informe_Mensual(year, month):
    result = session.query(cast(AARR.fecha, Date).label('Fecha'), (func.max(AARR.ea_import)-func.min(AARR.ea_import)).label('EA_Import')).\
        filter(extract('month', AARR.fecha) == month, extract('year', AARR.fecha) == year).\
        group_by(cast(AARR.fecha, Date)).\
        order_by(cast(AARR.fecha, Date)).\
        all()
    valores = []
    for i in range(len(result)):
        valores.append({'Fecha': str(result[i][0]), 'EA_import': result[i][1]})
    return(json.dumps(valores))

def InformeAnual(year):
    result = session.query(extract('month', AARR.fecha).label('Month'), (func.max(AARR.ea_import)-func.min(AARR.ea_import)).label('EA_Import')).\
        filter(extract('year', AARR.fecha) == year).\
        group_by(extract('month', AARR.fecha)).\
        order_by(extract('month', AARR.fecha)).\
        all()
    valores = []
    for i in range(len(result)):
        valores.append({'Month': int(result[i][0]), 'EA_import': result[i][1]})
    return(json.dumps(valores))