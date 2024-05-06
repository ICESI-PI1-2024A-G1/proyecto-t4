// JavaScript
document.addEventListener("DOMContentLoaded", function() {
    // Seleccionar todos los botones de edición
    var editButtons = document.querySelectorAll(".edit-btn");

    // Agregar evento clic a cada botón de edición
    editButtons.forEach(function(button) {
        button.addEventListener("click", function(event) {
            // Obtener el formulario asociado al botón de edición
            var popup = button.nextElementSibling;

            // Mostrar el formulario (popup)
            popup.style.display = "block";

            // Evitar que el clic en el botón propague al tr que lo contiene
            event.stopPropagation();
        });
    });

    // Seleccionar todas las clases "close" dentro de popups y agregar evento clic
    var closeButtons = document.querySelectorAll(".popup .close");
    closeButtons.forEach(function(closeBtn) {
        closeBtn.addEventListener("click", function() {
            // Ocultar el popup al hacer clic en la "x"
            var popup = closeBtn.closest(".popup");
            popup.style.display = "none";
        });
    });

    // Función para abrir el popup
    window.openPop = function() {
        // Aquí va la lógica para abrir el popup
    };
    
    // Función para cerrar el popup
    window.closePop = function() {
        // Aquí va la lógica para cerrar el popup
    };
});
