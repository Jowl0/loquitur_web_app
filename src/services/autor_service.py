from src.models.autor import autor

def autor_service(slug=None, articulo_id=None):
    autor_db = autor.autor_db(slug=slug, articulo_id=articulo_id)

    if not autor_db:
        return []

    resultado = []
    for nombre, imagen, url, fecha, id_autor in autor_db:
        resultado.append({
            "nombre": nombre,
            "imagen": imagen,
            "url_perfil": url,
            "fecha_registro": fecha,
            "id": id_autor
        })

    return resultado