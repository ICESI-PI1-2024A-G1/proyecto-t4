## Participantes:

- Pablo Fernando Pineda Patiño
- Leidy Daniela Londoño Candelo 
- Nayeli Suarez Portillo 
- Yeison Antonio Rodriguez Zuluaga 
- Isabella Huila Cerón


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
Para el correcto funcionamiento del programa debe instalar todas las dependencias necesarias con el comando `pip install -r requirements.txt`

Con el siguiente comando se corren todos los tests unitarios de un solo intento: `python manage.py test SistemaContableApp.tests.testMain`

Con los siguientes comandos calcula el coverage: 
1. `coverage run  manage.py test SistemaContableApp.tests.testMain`
2. `coverage report`

(Hay un coverage del 94%)


Con los siguientes comandos corre las pruebas automatizadas: 
`python manage.py test SistemaContableApp.tests.loginTest.seleniumLogin`

`python manage.py test SistemaContableApp.tests.requestByUserTests.seleniumRequests`

`python manage.py test SistemaContableApp.tests.requestByUserTests.seleniumRequestPermission`

`python manage.py test SistemaContableApp.tests.oneStopShopTests.seleniumOneStopShopForm`

`python manage.py test SistemaContableApp.tests.oneStopShopTests.seleniumOneStopShopPermissionTest`

`python manage.py test SistemaContableApp.tests.updateUserTests.seleniumUpdateUserPermissionTests`





















