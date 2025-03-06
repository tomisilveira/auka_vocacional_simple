// scripts.js
document.addEventListener("DOMContentLoaded", function () {
    // Mostrar cartel de carga al hacer clic en un botón
    const forms = document.querySelectorAll("form");
    forms.forEach(form => {
        form.addEventListener("submit", function (e) {
            // Mostrar cartel solo si el formulario tiene un mensaje de carga
            if (form.dataset.loadingMessage) {
                const loadingOverlay = document.createElement("div");
                loadingOverlay.classList.add("loading-overlay", "active");
                loadingOverlay.innerHTML = `
                    <div class="loading-message">
                        ${form.dataset.loadingMessage}
                    </div>
                `;
                document.body.appendChild(loadingOverlay);
            }
        });
    });

    // Ocultar cartel de carga cuando se complete la acción
    window.addEventListener("pageshow", function () {
        const loadingOverlay = document.querySelector(".loading-overlay");
        if (loadingOverlay) {
            loadingOverlay.remove();
        }
    });
});