document.addEventListener('DOMContentLoaded', function() {
    const btnVerMas = document.getElementById('btn-ver-mas-articulos-lista');
    const btnContainer = document.getElementById('btn-container');
    let contador = 1;

    if (btnVerMas) {
        btnVerMas.addEventListener('click', function () {
            const urlApi = '/api/ver_mas/articulos';
            const queryParams = `?contador=${contador}`;

            fetch(urlApi + queryParams)
                .then(response => response.json())
                .then(data => {
                    if (data.length > 0) {
                        const contenedor = document.getElementById('contenedor-articulos');
                        
                        data.forEach(art => {
                            const html = `
                            <div class="card mb-4 border shadow-sm card-fixed-height">
                                <div class="card-body h-100 p-3">
                                    <div class="row h-100">
                                        <div class="col-md-3 h-100">
                                            <div class="card overflow-hidden card-custom-border h-100">
                                                <div class="card-body p-0 position-relative h-100">
                                                    <img src="/${art.imagen}" class="img-cover-fit" alt="${art.titulo}" />
                                                    <a href="${art.slug}" class="stretched-link"></a>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="col-md-9 h-100">
                                            <div class="d-flex flex-column h-100 ps-0 ps-md-3 pt-1 pt-md-0 gap-3">
                                                <h4 class="card-title fw-bold text-dark text-truncate m-0">${art.titulo}</h4>
                                                
                                                <div class="d-flex align-items-center" style="position: relative; z-index: 2;">
                                                    <small class="text-muted">${art.fecha}</small>
                                                </div>

                                                <p class="card-text text-body desc-truncate m-0">
                                                    ${art.descripcion}
                                                </p>

                                                <div class="text-end mt-auto">
                                                    <a href="${art.slug}" class="card-link text-decoration-none fw-bold text-dark stretched-link">
                                                        Leer nota <i class="bi bi-arrow-right"></i>
                                                    </a>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>`;
                            
                            contenedor.insertAdjacentHTML('beforeend', html);
                        });
                        
                        contador++;
                    } else {
                        if (btnContainer) {
                            btnContainer.style.display = 'none';
                        } else {
                            btnVerMas.style.display = 'none';
                        }
                        
                        const alertContainer = document.getElementById('alert-container');
                        if (alertContainer) {
                            alertContainer.innerHTML = `
                                <div class="alert alert-dismissible alert-light border shadow-sm text-center fade show mx-auto" style="max-width: 500px;" role="alert">
                                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                                    <strong>¡Todo leído!</strong> No hay más artículos disponibles.
                                </div>`;
                        }
                    }
                })
                .catch(error => console.error(error));
        });
    }
});