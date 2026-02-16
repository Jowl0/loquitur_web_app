from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///instance/revista.db")


def grid():
    with engine.connect() as connection:
        query_sql = text("""
            SELECT a.titulo, i.url 
            FROM articulos a
            JOIN imagenes_articulo i ON a.id = i.articulo_id
            WHERE i.posicion = 1 
              AND a.estatus = 'publicado'
            ORDER BY a.fecha_publicacion DESC
            LIMIT 5
            """)
        query = connection.execute(query_sql)

        grid = [(fila.titulo, fila.url) for fila in query]

        return grid


g = grid()
print(g)
