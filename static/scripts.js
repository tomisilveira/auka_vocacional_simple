// static/scripts.js
document.addEventListener("DOMContentLoaded", function () {
    // Cargar las localidades en el <select>
    const locationSelect = document.getElementById('location');
    localidades.forEach(localidad => {
        const option = document.createElement('option');
        option.value = localidad;
        option.textContent = localidad;
        locationSelect.appendChild(option);
    });

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

function validateForm() {
    const ageInput = document.getElementById('age');
    const ageValue = ageInput.value;

    // Validar que la edad esté entre 14 y 40, o sea "+40"
    if (ageValue === "+40") {
        return true; // Permite enviar el formulario
    }

    const age = parseInt(ageValue, 10);
    if (isNaN(age)) {
        alert("Por favor, ingresa una edad válida.");
        return false;
    }
    if (age < 14 || age > 40) {
        alert("La edad debe estar entre 14 y 40 años, o selecciona '+40'.");
        return false;
    }

    return true; // Permite enviar el formulario
}