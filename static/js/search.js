function toggleFiltrado() {
    var ordenarPor = document.getElementById('ordenar_por').value;
    var tipoDiv = document.getElementById('tipoDiv');
    var estadoDiv = document.getElementById('estadoDiv');
    var fechaCreacionDiv = document.getElementById('fechaCreacionDiv');
    var fechaCierreDiv = document.getElementById('fechaCierreDiv');

    if (ordenarPor === 'currentState') {
        estadoDiv.style.display = 'flex';
        tipoDiv.style.display = 'none';
        fechaCreacionDiv.style.display = 'none';
        fechaCierreDiv.style.display = 'none';
    } else if (ordenarPor === 'type') {
        estadoDiv.style.display = 'none';
        tipoDiv.style.display = 'flex';
        fechaCreacionDiv.style.display = 'none';
        fechaCierreDiv.style.display = 'none';
    } else if (ordenarPor === 'creationDate') {
        estadoDiv.style.display = 'none';
        tipoDiv.style.display = 'none';
        fechaCreacionDiv.style.display = 'flex';
        fechaCierreDiv.style.display = 'none';

        // Configurar calendarios desplegables para fecha de creación
        $("#fecha_creacion_inicio, #fecha_creacion_fin").datepicker({
            dateFormat: 'yy-mm-dd',
            onSelect: function(selectedDate) {
                var option = this.id === "fecha_creacion_inicio" ? "minDate" : "maxDate",
                    instance = $(this).data("datepicker"),
                    date = $.datepicker.parseDate(instance.settings.dateFormat || $.datepicker._defaults.dateFormat, selectedDate, instance.settings);
                $("#fecha_creacion_inicio, #fecha_creacion_fin").not(this).datepicker("option", option, date);
            }
        });
    } else if (ordenarPor === 'closeDate') {
        estadoDiv.style.display = 'none';
        tipoDiv.style.display = 'none';
        fechaCreacionDiv.style.display = 'none';
        fechaCierreDiv.style.display = 'flex';

        // Configurar calendarios desplegables para fecha de cierre
        $("#fecha_cierre_inicio, #fecha_cierre_fin").datepicker({
            dateFormat: 'yy-mm-dd',
            onSelect: function(selectedDate) {
                var option = this.id === "fecha_cierre_inicio" ? "minDate" : "maxDate",
                    instance = $(this).data("datepicker"),
                    date = $.datepicker.parseDate(instance.settings.dateFormat || $.datepicker._defaults.dateFormat, selectedDate, instance.settings);
                $("#fecha_cierre_inicio, #fecha_cierre_fin").not(this).datepicker("option", option, date);
            }
        });
    } else {
        estadoDiv.style.display = 'none';
        tipoDiv.style.display = 'none';
        fechaCreacionDiv.style.display = 'none';
        fechaCierreDiv.style.display = 'none';
    }
}

