from src.database.db import db
from src.models.articulo import articulo
from src.models.imagen import imagen
from src.models.autor import autor
from src.models.autoria import autoria

def obtener_articulos_paginados(contador, cantidad=5, autor_id=None):
    offset = cantidad * contador
    
    query = db.session.query(
        articulo.titulo, 
        imagen.url, 
        articulo.descripcion, 
        articulo.fecha_publicacion, 
        articulo.slug,
        autor.nombre,
        autor.url_imagen,
        autor.url_pagina
    ).join(imagen, imagen.articulo_id == articulo.id) \
     .join(autoria, autoria.articulo_id == articulo.id) \
     .join(autor, autor.id == autoria.autor_id) \
     .filter(imagen.posicion == 1) \
     .filter(articulo.estatus == 'publicado')

    if autor_id:
        query = query.filter(autor.id == autor_id)

    articulos_db = (
        query.order_by(articulo.fecha_publicacion.desc())
        .offset(offset)
        .limit(cantidad)
        .all()
    )

    resultado = []
    for art in articulos_db:
        resultado.append({
            "titulo": art.titulo,
            "imagen": art.url,
            "descripcion": art.descripcion,
            "fecha": art.fecha_publicacion,
            "slug": art.slug,
            "autor": art.nombre,
            "autor_url_imagen": art.url_imagen,
            "autor_url_pagina": art.url_pagina
        })
        
    return resultado