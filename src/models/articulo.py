from src.database import db

class articulo(db.Model):
    __tablename__ = "articulos"
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(300), nullable=False)
    descripcion = db.Column(db.String(300), nullable=False)
    slug = db.Column(db.String(300), unique=True, nullable=False)
    estatus = db.Column(db.String(20), nullable=False, default="draft")
    fecha_publicacion = db.Column(db.String(19))
    contenido = db.Column(db.Text, nullable=False)
    
    @classmethod
    def grid_db(cls):
        from src.models.imagen import imagen
        
        query = (   
            db.session.query(cls.titulo, imagen.url, cls.slug)
            .join(imagen, imagen.articulo_id == cls.id)
            .filter(imagen.posicion == 1)
            .filter(cls.estatus == 'publicado')
            .order_by(cls.fecha_publicacion.desc())
            .limit(5)
            .all()
        )  
        
        if not query:
            return None
            
        return query

    @classmethod
    def articulos_lista_db(cls, contador, cantidad=5):
        from src.models.imagen import imagen
        from src.models.autor import autor
        from src.models.autoria import autoria
        
        offset = cantidad * contador
    
        query = (
            db.session.query(
                cls.titulo, 
                imagen.url, 
                cls.descripcion, 
                cls.fecha_publicacion, 
                cls.slug,
                autor.nombre,
                autor.url_imagen,
                autor.url_pagina
            )
            .join(imagen, imagen.articulo_id == cls.id)
            .join(autoria, autoria.articulo_id == cls.id)
            .join(autor, autor.id == autoria.autor_id)
            .filter(imagen.posicion == 1)
            .filter(cls.estatus == 'publicado')
            .order_by(cls.fecha_publicacion.desc())
            .offset(offset)
            .limit(cantidad)
            .all()
        )

        if not query:
            return None

        return query
    
    @classmethod
    def articulo_db(cls, slug):
        from src.models.imagen import imagen
        
        query = (
            db.session.query(
                cls.id,
                cls.titulo,
                cls.contenido,
                cls.fecha_publicacion,
                cls.descripcion,
                imagen.url
            )
            .join(imagen, imagen.articulo_id == cls.id)
            .filter(cls.slug == f"/articulos/{slug}") 
            .filter(cls.estatus == 'publicado')
            .filter(imagen.posicion == 1)
            .first()
        )
        
        if not query:
            return None
            
        return query

    @classmethod
    def articulos_lista_autor_db(cls, autor_id, contador, cantidad=5):
        from src.models.imagen import imagen
        from src.models.autoria import autoria

        offset = cantidad * contador
        
        query = (
            db.session.query(
                cls.titulo, 
                imagen.url, 
                cls.descripcion, 
                cls.fecha_publicacion, 
                cls.slug
            )
            .join(imagen, imagen.articulo_id == cls.id)
            .join(autoria, autoria.articulo_id == cls.id)
            .filter(imagen.posicion == 1)
            .filter(cls.estatus == 'publicado')
            .filter(autoria.autor_id == autor_id)
            .order_by(cls.fecha_publicacion.desc())
            .offset(offset)
            .limit(cantidad)
            .all()
        )
        
        if not query:
            return None
            
        return query