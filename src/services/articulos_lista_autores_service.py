from src.models.articulo import articulo

def articulos_lista_autor_service(autor_id, contador, cantidad=5):
    resultados_db = articulo.articulos_lista_autor_db(autor_id, contador, cantidad)
    
    if not resultados_db:
        return []
        
    lista_articulos = []
    
    for titulo, url_imagen, descripcion, fecha_publicacion, slug in resultados_db:
        lista_articulos.append({
            "titulo": titulo,
            "imagen": url_imagen,
            "descripcion": descripcion,
            "fecha": fecha_publicacion,
            "slug": slug
        })
        
    return lista_articulos