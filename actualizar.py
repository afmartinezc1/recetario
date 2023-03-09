from src.db.cancion import Cancion
from src.db.interprete import Interprete
from src.db.album import Album
from src.db.declarative_base import Session, engine, Base


if __name__ == '__main__':
  session = Session()
  cancion = session.query(Cancion).get(2)
  interprete = session.query(Interprete).get(4)

  cancion.minutos = 5
  cancion.segundos = 30
  cancion.compositor = "Pedro Pérez"
  cancion.interpretes.append(interprete)
  session.add(cancion)
  session.commit()
  session.close()