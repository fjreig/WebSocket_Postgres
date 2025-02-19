from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float
from datetime import datetime

from app.database import Base, session, engine

class BlogPost(Base):
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

# Creating new tables
#Base.metadata.create_all(engine)

def get_all_posts():
    result = session.query(BlogPost).limit(5).all()
    return(result)