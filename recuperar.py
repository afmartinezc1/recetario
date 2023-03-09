from src.db.cancion import Cancion
from src.db.interprete import Interprete
from src.db.album import Album, Medio
from src.db.vocal import Vocal
from src.db.instrumental import Instrumental
from src.db.declarative_base import Session, engine, Base
from sqlalchemy.orm import selectin_polymorphic


if __name__ == '__main__':
  session = Session()
  # canciones = session.query(Cancion).all()
  vocales = session.query(Vocal).all()
  for x in vocales:
    print(x.titulo)
  print(all(hasattr(x, "cantante") for x in vocales))
  print(all(hasattr(x, "cantante") for x in vocales))

  # print('Las canciones almacenadas son:')
  # for cancion in canciones:
  #   print(type(cancion))
  #   print("Tipo: " + '' + " | Titulo: " + cancion.titulo + " (00:" +
  #       str(cancion.minutos) + ":" +
  #       str(cancion.segundos) + ")")

  #   print("")
  #   print("Intérpretes")
  #   for interprete in cancion.interpretes:
  #       print(" - " + interprete.nombre)

  #   print("")
  #   print("Presente en el album:")
  #   for album in cancion.albumes:
  #       print(" - " + album.titulo)

  #   print("---------------------------------")


  # print('Los álbumes almacenados en discos son:')
  # albumes = session.query(Album).filter(Album.medio == Medio.DISCO).all()
  # for album in albumes:
  #   print("Album: " + album.titulo)

  session.close()