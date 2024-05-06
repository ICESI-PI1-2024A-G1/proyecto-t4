# Gestión contable

El presente proyecto tiene como objetivo proporcionar un sistema en donde se pueda gestionar las solicitudes contables. Este sistema permite a los usuarios completar formularios específicos para cada tipo de solicitud y enviarlos para su procesamiento. Además de estas funcionalidades, el proyecto incluye características adicionales como la generación de documentos PDF a partir de la información del formulario y el envío de solicitudes a la oficina de ventanilla única para su gestión.
Dentro del sistema, existe un apartado llamado Ventanilla Única, donde se lleva a cabo el procesamiento de las solicitudes. Esta sección proporciona herramientas que permiten buscar y filtrar las solicitudes de acuerdo con diversos criterios, facilitando así la gestión y seguimiento de estas. Con esto, se busca garantizar la eficiencia, la transparencia y la precisión en el manejo de los procesos financieros.

### Objetivos específicos:
Los objetivos específicos del proyecto son los siguientes:
- Gestión de Solicitudes: Permitir a los usuarios solicitantes la creación de diferentes tipos de solicitudes, como cuentas de cobro, requisiciones y pagos al exterior, a través de formularios específicos para cada tipo de solicitud.
- Almacenamiento de Información: Registrar y almacenar de manera precisa la información proporcionada por los usuarios en las solicitudes, incluyendo datos personales, detalles de la solicitud y cualquier otra información relevante para su procesamiento.
- Envío y Procesamiento: Facilitar el envío de las solicitudes a la oficina de ventanilla única para su procesamiento, garantizando que la información se entregue de manera oportuna y completa para llevar a cabo los procesos necesarios.
-	Generación de Documentos: Crear documentos PDF a partir de la información ingresada en los formularios de solicitud, facilitando el envío estructurado y organizado de la información para su revisión y procesamiento.
-	Búsqueda y Recuperación de Información: Proporcionar funcionalidades de búsqueda y recuperación de solicitudes previamente registradas, permitiendo a los usuarios con permisos adecuados encontrar y analizar la información de manera eficiente.
## Notas adicionales
- La función sendFormAsPdf se encarga de enviar el formulario como un archivo PDF adjunto por correo electrónico. Si se desea cambiar el correo electrónico al que se envían los formularios, simplemente se puede modificar el valor de las variables email o recipient_email dentro de las funciones createExteriorPaymentForm, createChargeAccountForm y createRequisitionForm.

-	Para el correcto funcionamiento del filtro en el diseño de los campos de los formularios adaptados al HTML, es necesario descargar e instalar el paquete django-widget-tweaks. Esto se puede hacer mediante el comando pip install django-widget-tweaks.
- Para el funcionamiento adecuado de la generación de archivos PDF, se deben descargar e instalar los siguientes paquetes:
- 	django-renderpdf: Instalable a través de pip install django-renderpdf.
o	GTK for Windows Runtime Environment Installer: Se puede descargar desde el siguiente enlace: GTK for Windows Runtime Environment Installer.
-	El apartado de formulario para agregar en ventanilla única es lo que permite crear y enviar las solicitudes en ventanilla única mediante la completitud de distintos campos y archivos adjuntos, actualmente este apartado solo permite adjuntar un único documento adjunto, pero para el futuro se espera puedan ser más.
-	La función de búsqueda y filtrado actualmente realiza la búsqueda mediante los campos más relevantes que se puedan considerar de la solicitud, pero aun así cabe la posibilidad de agregar más “queryset” con palabras que se consideren claves dentro de los campos de las solicitudes.
- Para el correcto funcionamiento del programa, es necesario descargar django.multiupload, esto con el comando "pip install django-multiupload"; actualmente este apartado no está siendo utilizado, pero se usó durante el desarrollo en etapas anteriores del proyecto. Aunque no se esté utilizando en la versión actual, se debe instalar y ya en próximos feat tomará una elección al respecto.

## Participantes:

- Pablo Fernando Pineda Patiño
- Leidy Daniela Londoño Candelo 
- Nayeli Suarez Portillo 
- Yeison Antonio Rodriguez Zuluaga 
- Isabella Huila Cerón
