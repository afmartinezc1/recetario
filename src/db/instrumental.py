from sqlalchemy import Column, Integer, String, ForeignKey
from .cancion import Cancion

class Instrumental(Cancion):
    # id = Column(ForeignKey("cancion.id"), primary_key=True)
    instrumentoPrincipal = Column(String)    
    __mapper_args__ = {
        "polymorphic_identity": "instrumental",
    }
    

# Beyond compare # 