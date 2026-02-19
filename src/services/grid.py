from src.database.db import db
from src.models.articulo import articulo
from src.models.imagen import imagen
from src.models.autor import autor
from src.models.autoria import autoria

def get_grid():
    grid = (   
        db.session.query(articulo.titulo, imagen.url, articulo.slug)
        .join(imagen, imagen.articulo_id == articulo.id)
        .filter(imagen.posicion == 1)
        .filter(articulo.estatus == 'publicado')
        .order_by(articulo.fecha_publicacion.desc())
        .limit(5)
        .all()
    )   
    return(grid)