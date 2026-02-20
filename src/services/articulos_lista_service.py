from src.models.articulo import articulo

def articulos_lista_service(contador, cantidad=5):
    
    resultados_db = articulo.articulos_lista_db(contador, cantidad)
    
    if not resultados_db:

        return []        
    lista_articulos = []
    
    for titulo, url_imagen, descripcion, fecha, slug, autor_nombre, autor_img, autor_pagina in resultados_db:
    
        lista_articulos.append({
            "titulo": titulo,
            "imagen": url_imagen,
            "descripcion": descripcion,
            "fecha": fecha,
            "slug": slug,
            "autor": autor_nombre,
            "autor_url_imagen": autor_img,
            "autor_url_pagina": autor_pagina
    
        })
        
    return lista_articulos