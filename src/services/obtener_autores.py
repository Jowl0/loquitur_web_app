from src.database.db import db
from src.models.autor import autor

def obtener_autores(contador, cantidad=5):
    offset = cantidad * contador
    
    autores_db = (
        db.session.query(
            autor.nombre,
            autor.url_imagen,
            autor.url_pagina,
            autor.fecha_registro

        )
        .order_by(autor.nombre.asc())
        .offset(offset)
        .limit(cantidad)
        .all()
    )

    resultado = []
    for row in autores_db:
        resultado.append({
            "nombre": row.nombre,
            "imagen": row.url_imagen,
            "url_perfil": row.url_pagina,
            "fecha_registro": row.fecha_registro
        })
        
    return resultado