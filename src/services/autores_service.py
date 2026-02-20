from src.models.autor import autor

def autores_service(contador, cantidad=5):
    autores_db = autor.autores_db(contador, cantidad)

    if not autores_db:
        return []

    resultado = []
    for nombre, imagen, url, fecha in autores_db:
        resultado.append({
            "nombre": nombre,
            "imagen": imagen,
            "url_perfil": url,
            "fecha_registro": fecha
        })
        
    return resultado