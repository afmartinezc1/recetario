from sqlalchemy import Column, Integer, ForeignKey
from .declarative_base import Base

class AlbumCancion(Base):
  __tablename__ = 'albumCancion'
  
  cancion = Column(Integer, ForeignKey('cancion.id'), primary_key=True)
  album = Column(Integer, ForeignKey('album.id'), primary_key=True)