from sqlalchemy import Column, String, ForeignKey
from .cancion import Cancion

class Vocal(Cancion):    
    __tablename__ = 'vocal'
    id = Column(ForeignKey('cancion.id'), primary_key=True)
    cantante = Column(String)
    __mapper_args__ = {
        "polymorphic_identity": "vocal",
    }

# Beyond compare # 