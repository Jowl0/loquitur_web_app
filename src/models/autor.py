from src.database import db

class autor(db.Model):
    __tablename__ = "autores"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), unique=True)
    instagram_url = db.Column(db.String(255))
    correo_url = db.Column(db.String(255))
    linkedin_url = db.Column(db.String(255))
    x_url = db.Column(db.String(255))
    url_imagen = db.Column(db.String(800), nullable=False)
    url_pagina = db.Column(db.String(800), nullable=False)
    fecha_registro = db.Column(
        db.String(19), nullable=False, default=db.func.datetime("now")
    )

    @classmethod
    def autor_db(cls, slug=None, articulo_id=None):
        from src.models.autoria import autoria

        query = db.session.query(
            autor.nombre,
            autor.url_imagen,
            autor.url_pagina,
            autor.fecha_registro,
            autor.id
        )

        if articulo_id:
            query = query.join(autoria, autor.id == autoria.autor_id).filter(autoria.articulo_id == articulo_id)
        elif slug:
            query = query.filter(autor.url_pagina == f"/autores/{slug}")

        resultado = query.all()

        if not resultado:
            return None

        return resultado

    @classmethod
    def autores_db(cls, contador, cantidad=5):
        offset = cantidad * contador
    
        query = (
            db.session.query(
                cls.nombre,
                cls.url_imagen,
                cls.url_pagina,
                cls.fecha_registro
            )
            .order_by(cls.nombre.asc())
            .offset(offset)
            .limit(cantidad)
            .all()
        )

        if not query:
           return None
        
        return query