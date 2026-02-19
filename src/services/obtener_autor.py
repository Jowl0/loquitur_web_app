from src.database.db import db
from src.models.autor import autor

def obtener_autor(slug=None):
    autor_db = (
        db.session.query(
            autor.nombre,
            autor.url_imagen,
            autor.url_pagina,
            autor.fecha_registro,
            autor.id
        )
        .filter(autor.url_pagina == f"/autores/{slug}")
        .all() 
    )

    resultado = []
    
    for row in autor_db:
        resultado.append({
            "nombre": row.nombre,
            "imagen": row.url_imagen,
            "url_perfil": row.url_pagina,
            "fecha_registro": row.fecha_registro,
            'id' : row.id
        })
        
    return resultado