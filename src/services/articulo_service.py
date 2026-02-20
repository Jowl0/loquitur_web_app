from src.models.articulo import articulo

def articulo_service(slug):
    resultado_db = articulo.articulo_db(slug)
    
    if not resultado_db:
        return None
    art_id, titulo, contenido, fecha, descripcion, url_imagen = resultado_db
    
    return {
        "id": art_id,
        "titulo": titulo,
        "contenido": contenido,
        "fecha": fecha,
        "descripcion": descripcion,
        "imagen": url_imagen
    }