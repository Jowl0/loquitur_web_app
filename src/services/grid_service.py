from src.models.articulo import articulo

def grid_service():
    grid=articulo.grid_db()
    return(grid)