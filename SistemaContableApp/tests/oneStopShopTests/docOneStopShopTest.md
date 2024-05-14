# Pruebas Unitarias sobre el módulo Ventanilla Única

## Descripción de tests unitarios

### CommentsTestCase

La clase `CommentsTestCase` contiene pruebas para la función comments, la cual determina el comportamiento de comentarios en el módulo Ventanilla Única. Estas pruebas cubren diferentes escenarios para garantizar que el sistema se comporte como se espera en diversas situaciones.

#### test_approval_comment_unauthorized: 

  - **Descripción**: Verificar que un usuario no autorizado no puede aprobar un comentario.
  - **Entrada**: Usuario no autorizado intenta aprobar un comentario.
  - **Resultado esperado**: Se espera que el usuario sea redirigido a la página de inicio de sesión.

#### test_approval_comment_empty: 
  - **Descripción**: Verificar el comportamiento cuando el comentario de aprobación está vacío.
  - **Entrada**: Un usuario administrador intenta aprobar un comentario vacío.
  - **Resultado esperado**: Se espera que el comentario de aprobación esté vacío en la instancia del objeto.

#### test_approval_comment_valid: 
  - **Descripción**: Verificar la funcionalidad de aprobar un comentario.
  - **Entrada**: Usuario administrador aprueba un comentario válido.
  - **Resultado esperado**: Se espera que el comentario de aprobación se guarde correctamente en la base de datos.

#### test_approval_comment_redirect: 
  - **Descripción**: Verificar la redirección después de enviar un comentario de aprobación.
  - **Entrada**: Usuario administrador aprueba un comentario y es redirigido.
  - **Resultado esperado**: Se espera que la redirección lleve a la página 'fullOneStopShop' sin mensajes de éxito.

#### test_approval_comment_not_allowed: 
  - **Descripción**: Verificar que la Ventanilla Única no puede aprobar un comentario.
  - **Entrada**: Usuario de Ventanilla Única intenta aprobar un comentario.
  - **Resultado esperado**: Se espera que el usuario sea redirigido con un mensaje de error de permisos.

#### test_accounting_comment_valid_admin: 
  - **Descripción**: Verificar que un usuario administrador puede agregar un comentario de contabilidad.
  - **Entrada**: Usuario administrador agrega un comentario de contabilidad válido.
  - **Resultado esperado**: Se espera que el comentario de contabilidad se guarde correctamente en la base de datos.

#### test_accounting_comment_valid_gestor: 
  - **Descripción**: Verificar que un usuario gestor puede agregar un comentario de contabilidad válido.
  - **Entrada**: Usuario gestor agrega un comentario de contabilidad válido.
  - **Resultado esperado**: Se espera que el comentario de contabilidad se guarde correctamente en la base de datos.

#### test_accounting_comment_valid_contable: 
  - **Descripción**: Verificar que un usuario contable puede agregar un comentario de contabilidad válido.
  - **Entrada**: Usuario contable agrega un comentario de contabilidad válido.
  - **Resultado esperado**: Se espera que el comentario de contabilidad se guarde correctamente en la base de datos.

#### test_accounting_comment_invalid_user: 
  - **Descripción**: Verificar que un usuario no válido no puede agregar un comentario de contabilidad.
  - **Entrada**: Usuario de Ventanilla Única intenta agregar un comentario de contabilidad.
  - **Resultado esperado**: Se espera que el usuario sea redirigido con un mensaje de error de permisos.

#### test_accounting_comment_redirect: 
  - **Descripción**: Verificar la redirección después de enviar un comentario de contabilidad.
  - **Entrada**: Usuario administrador agrega un comentario de contabilidad y es redirigido.
  - **Resultado esperado**: Se espera que la redirección lleve a la página 'fullOneStopShop' sin mensajes de éxito.

### FormTestCase

Esta clase `FormTestCase` contiene pruebas para las formas `OneStopShopForm` y `AttachedDocumentForm`, las cuales se utilizan en el módulo Ventanilla Única para capturar datos y adjuntar documentos. Estas pruebas garantizan que las formas se comporten como se espera y validen los datos correctamente.

#### testOneStopShopValidForm:

- **Descripción**: Probar el formulario `OneStopShopForm` con datos válidos.
- **Entrada**: Datos válidos para el formulario.
- **Resultado esperado**: Se espera que el formulario sea válido.

#### testAttachedDocumentValidForm:

- **Descripción**: Probar el formulario `AttachedDocumentForm` con datos válidos.
- **Entrada**: Datos de archivo válidos para el formulario.
- **Resultado esperado**: Se espera que el formulario sea válido.

#### testOneStopShopInvalidForm:

- **Descripción**: Probar el formulario `OneStopShopForm` con datos inválidos.
- **Entrada**: Datos incompletos para el formulario.
- **Resultado esperado**: Se espera que el formulario sea inválido.

#### testAttachedDocumentInvalidForm:

- **Descripción**: Probar el formulario `AttachedDocumentForm` con datos inválidos.
- **Entrada**: Datos de archivo incorrectos para el formulario.
- **Resultado esperado**: Se espera que el formulario sea inválido.

#### testOneStopShopInvalid:

- **Descripción**: Probar el formulario `OneStopShopForm` con datos inválidos.
- **Entrada**: Datos incompletos para el formulario.
- **Resultado esperado**: Se espera que el formulario sea inválido.

### HistoryStateTestCase

Esta clase `HistoryStateTestCase` contiene pruebas para el modelo `Following` y la funcionalidad relacionada con el historial de cambios de estado en el módulo Ventanilla Única. Estas pruebas garantizan que los estados de los objetos se gestionen correctamente y que el historial de cambios de estado se muestre adecuadamente en la interfaz de usuario.

#### test_initial_state:

- **Descripción**: Verificar el estado inicial del objeto Following.
- **Entrada**: Inicia sesión como usuario administrador y crea una instancia del objeto.
- **Resultado esperado**: Se espera que el estado inicial del objeto Following sea "Pendiente de aceptación".

#### test_state_change:

- **Descripción**: Probar el cambio de estado de un objeto.
- **Entrada**: Inicia sesión como usuario administrador, crea una instancia del objeto y cambia su estado.
- **Resultado esperado**: Se espera que el estado del objeto cambie correctamente de "Pendiente de aceptación" a "En revisión".

#### test_state_change_history_display:

- **Descripción**: Verificar la visualización del historial de cambios de estado.
- **Entrada**: Inicia sesión como usuario administrador, crea una instancia del objeto y cambia su estado.
- **Resultado esperado**: Se espera que al acceder a la vista 'changeHistory', se muestre correctamente el historial de cambios de estado para el objeto dado.

#### test_state_change_history_display_empty:

- **Descripción**: Verificar la visualización del historial de cambios de estado cuando no hay cambios.
- **Entrada**: Inicia sesión como usuario administrador y crea una instancia del objeto sin cambios de estado.
- **Resultado esperado**: Se espera que al acceder a la vista 'changeHistory', se muestre que no hay cambios de estado para el objeto dado.

### ModelTestCase

Esta clase `ModelTestCase` contiene pruebas para los modelos `Following` y `AttachedDocument` en el módulo Ventanilla Única. Estas pruebas aseguran que los modelos creen instancias correctamente y devuelvan la representación de cadena esperada.

#### testFollowingModel:

- **Descripción**: Probar el modelo `Following`.
- **Entrada**: Se crea una instancia del modelo `Following`.
- **Resultado esperado**: Se espera que la representación de cadena de la instancia sea `<type> - <cenco>`.

#### testAttachedDocumentModel:

- **Descripción**: Probar el modelo `AttachedDocument`.
- **Entrada**: Se crea una instancia del modelo `AttachedDocument`.
- **Resultado esperado**:
  - La representación de cadena de la instancia debería ser el nombre del archivo.
  - El campo `associatedFollowing` debería estar asociado a una instancia de `Following`.

### ModifyStateTestCase

Esta clase `ModifyStateTestCase` contiene pruebas para la vista `update_state` en el módulo Ventanilla Única. Estas pruebas garantizan que la actualización del estado de un objeto `Following` se realice correctamente y que se manejen adecuadamente los diferentes casos, como la autorización del usuario y la validez del nuevo estado.

#### test_update_state_view:

- **Descripción**: Prueba la vista `update_state` para actualizar el estado de un objeto `Following`.
- **Entrada**: Se envía una solicitud POST a la vista con un nuevo estado.
- **Resultado esperado**: Se espera que la vista redirija correctamente después de la actualización y que el estado del objeto `Following` se actualice correctamente en la base de datos.

#### test_update_state_view_invalid_state:

- **Descripción**: Prueba la vista `update_state` con un estado inválido.
- **Entrada**: Se envía una solicitud POST a la vista con un estado que no existe en la base de datos.
- **Resultado esperado**: Se espera que la vista redirija a la página correcta y que el estado del objeto `Following` no cambie.

#### test_update_state_to_current_state:

- **Descripción**: Prueba la vista `update_state` al intentar actualizar al mismo estado actual.
- **Entrada**: Se envía una solicitud POST a la vista con el mismo estado actual.
- **Resultado esperado**: Se espera que la vista redirija a la página correcta y que el estado del objeto `Following` no cambie.

#### test_update_state_unauthorized_user:

- **Descripción**: Prueba la vista `update_state` con un usuario no autorizado.
- **Entrada**: Se envía una solicitud POST a la vista con un usuario sin permisos de administrador.
- **Resultado esperado**: Se espera que la vista redirija a la página correcta y que el estado del objeto `Following` no cambie, y que se muestre un mensaje de error de permisos.

### OneStopShop View/Permission TestCase

Esta clase contiene pruebas para las vistas relacionadas con la Ventanilla Única en la aplicación de contabilidad.

#### setUp()

- **Descripción**: Configura los datos necesarios para las pruebas.
- **Entrada**: Ninguna.
- **Resultado esperado**: Roles, usuarios, estados y objetos `Following` creados correctamente.

#### test_summaryOneStopShopView_allowed()

- **Descripción**: Prueba si un usuario con el rol de administrador puede acceder a la vista resumen de la Ventanilla Única.
- **Resultado esperado**: Se espera que el código de estado de la respuesta sea 200.

#### test_summaryOneStopShopView_not_allowed()

- **Descripción**: Prueba si un usuario sin los permisos adecuados puede acceder a la vista resumen de la Ventanilla Única.
- **Resultado esperado**: Se espera que el código de estado de la respuesta sea 302, que indica una redirección debido a la falta de permisos.

#### test_fullOneStopShopView_allowed()

- **Descripción**: Prueba si un usuario con el rol de administrador puede acceder a la vista completa de la Ventanilla Única.
- **Resultado esperado**: Se espera que el código de estado de la respuesta sea 200.

#### test_fullOneStopShopView_not_allowed()

- **Descripción**: Prueba si un usuario sin los permisos adecuados puede acceder a la vista completa de la Ventanilla Única.
- **Resultado esperado**: Se espera que el código de estado de la respuesta sea 302, que indica una redirección debido a la falta de permisos.

#### test_oneStopShopFormView_allowed()

- **Descripción**: Prueba si un usuario con el rol de Ventanilla Única puede acceder al formulario de la Ventanilla Única.
- **Resultado esperado**: Se espera que el código de estado de la respuesta sea 200.

#### test_oneStopShopFormView_not_allowed()

- **Descripción**: Prueba si un usuario sin los permisos adecuados puede acceder al formulario de la Ventanilla Única.
- **Resultado esperado**: Se espera que el código de estado de la respuesta sea 302, que indica una redirección debido a la falta de permisos.

#### test_updateState_not_allowed()

- **Descripción**: Prueba si un usuario con el rol de Ventanilla Única puede actualizar el estado de un objeto `Following`.
- **Resultado esperado**: Se espera que el código de estado de la respuesta sea 302, que indica una redirección debido a la falta de permisos, y que el estado del objeto `Following` no cambie.

#### test_updateState_allowed()

- **Descripción**: Prueba si un usuario con el rol de administrador puede actualizar el estado de un objeto `Following`.
- **Resultado esperado**: Se espera que el código de estado de la respuesta sea 302, que indica una redirección después de la actualización, y que el estado del objeto `Following` cambie correctamente.

#### test_changeHistory_allowed()

- **Descripción**: Prueba si un usuario con el rol de administrador puede ver el historial de cambios de un objeto `Following`.
- **Resultado esperado**: Se espera que el código de estado de la respuesta sea 200.

#### test_changeHistory_not_allowed()

- **Descripción**: Prueba si un usuario con el rol de Ventanilla Única puede ver el historial de cambios de un objeto `Following`.
- **Resultado esperado**: Se espera que el código de estado de la respuesta sea 200, ya que el usuario no tiene los permisos adecuados.

#### test_approval_comment()

- **Descripción**: Prueba si un usuario con el rol de administrador puede agregar un comentario de aprobación a un objeto `Following`.
- **Resultado esperado**: Se espera que el código de estado de la respuesta sea 302, que indica una redirección después de la actualización, y que el comentario de aprobación se guarde correctamente en el objeto `Following`.

#### test_approval_comment_no_permission()

- **Descripción**: Prueba si un usuario sin los permisos adecuados puede agregar un comentario de aprobación a un objeto `Following`.
- **Resultado esperado**: Se espera que el código de estado de la respuesta sea 200, ya que el usuario no tiene los permisos adecuados para realizar esta acción.

#### test_accounting_comment()

- **Descripción**: Prueba si un usuario con el rol de contable puede agregar un comentario de contabilidad a un objeto `Following`.
- **Resultado esperado**: Se espera que el código de estado de la respuesta sea 302, que indica una redirección después de la actualización, y que el comentario de contabilidad se guarde correctamente en el objeto `Following`.

#### test_accounting_comment_no_permission()

- **Descripción**: Prueba si un usuario sin los permisos adecuados puede agregar un comentario de contabilidad a un objeto `Following`.
- **Resultado esperado**: Se espera que el código de estado de la respuesta sea 200, ya que el usuario no tiene los permisos adecuados para realizar esta acción.

#### test_acceptance_state()

- **Descripción**: Prueba si un usuario con el rol de administrador puede cambiar el estado de aceptación de un objeto `Following`.
- **Resultado esperado**: Se espera que el código de estado de la respuesta sea 302, que indica una redirección después de la actualización, y que el estado de aceptación del objeto `Following` se actualice correctamente.

#### test_acceptance_state_no_permission()

- **Descripción**: Prueba si un usuario sin los permisos adecuados puede cambiar el estado de aceptación de un objeto `Following`.
- **Resultado esperado**: Se espera que el código de estado de la respuesta sea 200, ya que el usuario no tiene los permisos adecuados para realizar esta acción.

#### test_revision_state()

- **Descripción**: Prueba si un usuario con el rol de administrador puede cambiar el estado de revisión de un objeto `Following`.
- **Resultado esperado**: Se espera que el código de estado de la respuesta sea 302, que indica una redirección después de la actualización, y que el estado de revisión del objeto `Following` se actualice correctamente.

#### test_revision_state_no_permission()

- **Descripción**: Prueba si un usuario sin los permisos adecuados puede cambiar el estado de revisión de un objeto `Following`.
- **Resultado esperado**: Se espera que el código de estado de la respuesta sea 200, ya que el usuario no tiene los permisos adecuados para realizar esta acción.

#### test_approval_state()

- **Descripción**: Prueba si un usuario con el rol de administrador puede cambiar el estado de aprobación de un objeto `Following`.
- **Resultado esperado**: Se espera que el código de estado de la respuesta sea 302, que indica una redirección después de la actualización, y que el estado de aprobación del objeto `Following` se actualice correctamente.

#### test_approval_state_no_permission()

- **Descripción**: Prueba si un usuario sin los permisos

 adecuados puede cambiar el estado de aprobación de un objeto `Following`.
- **Resultado esperado**: Se espera que el código de estado de la respuesta sea 200, ya que el usuario no tiene los permisos adecuados para realizar esta acción.

### SearchTestCase

Esta clase de prueba valida la funcionalidad de búsqueda y filtrado en la vista de resumen de la Ventanilla Única.

#### setUp()

- **Descripción**: Configura los datos necesarios para las pruebas.
- **Entrada**: Ninguna.
- **Resultado esperado**: Roles, usuarios y objetos `Following` creados correctamente.

#### crear_instancias()

- **Descripción**: Crea instancias de objetos `Following` en la base de datos para realizar pruebas.
- **Entrada**: Ninguna.
- **Resultado esperado**: Instancias creadas correctamente.

#### test_filtrarSolicitud_estado()

- **Descripción**: Prueba el filtrado de solicitudes por estado.
- **Resultado esperado**: Se espera que la respuesta tenga un código de estado 200 y contenga las solicitudes con el estado especificado.

#### test_busqueda_solicitud()

- **Descripción**: Prueba la búsqueda de una solicitud por tipo.
- **Resultado esperado**: Se espera que la respuesta tenga un código de estado 200 y contenga la solicitud buscada.

#### test_busqueda()

- **Descripción**: Prueba la búsqueda de una solicitud por cualquier parámetro.
- **Resultado esperado**: Se espera que la respuesta tenga un código de estado 200 y contenga las solicitudes que coincidan con el parámetro de búsqueda.

#### test_filtrar_solicitud_por_tipo()

- **Descripción**: Prueba el filtrado de solicitudes por tipo.
- **Resultado esperado**: Se espera que la respuesta tenga un código de estado 200 y contenga la solicitud con el tipo especificado.

#### test_filtrar_solicitud_por_fecha()

- **Descripción**: Prueba el filtrado de solicitudes por rango de fechas de creación.
- **Resultado esperado**: Se espera que la respuesta tenga un código de estado 200 y contenga las solicitudes cuyas fechas de creación estén dentro del rango especificado.

#### test_filter_close_date()

- **Descripción**: Prueba el filtrado de solicitudes por rango de fechas de cierre.
- **Resultado esperado**: Se espera que la respuesta tenga un código de estado 200 y contenga las solicitudes cuyas fechas de cierre estén dentro del rango especificado.

### StateTestCase

La clase `StatesTestCase` contiene pruebas para verificar el comportamiento de las vistas relacionadas con los estados de las solicitudes en el sistema contable.

#### test_acceptance_state_authenticated

  - **Descripción**: Prueba el cambio de estado de aceptación de una solicitud por un usuario autenticado.
  - **Entrada**: Usuario autenticado como administrador, solicitud con estado de aceptación inicial 'Pendiente'.
  - **Resultado esperado**: Se espera que la solicitud cambie su estado de aceptación a 'Aceptado' y que el código de estado de la respuesta sea 200.

#### test_acceptance_state_authenticated_rejected

  - **Descripción**: Prueba el cambio de estado de aceptación de una solicitud por un usuario autenticado.
  - **Entrada**: Usuario autenticado como administrador, solicitud con estado de aceptación inicial 'Rechazado'.
  - **Resultado esperado**: Se espera que la solicitud cambie su estado de aceptación a 'Rechazado' y que el código de estado de la respuesta sea 200.

#### test_set_revision_state_authenticated

  - **Descripción**: Prueba el cambio de estado de revisión de una solicitud por un usuario autenticado.
  - **Entrada**: Usuario autenticado como administrador, solicitud con estado de revisión inicial 'En revisión'.
  - **Resultado esperado**: Se espera que la solicitud cambie su estado de revisión a 'En revisión' y que el código de estado de la respuesta sea 200.

#### test_set_invalid_revision_state

  - **Descripción**: Prueba el intento de establecer un estado de revisión no permitido.
  - **Entrada**: Usuario autenticado como administrador, solicitud con estado de revisión inicial 'None'.
  - **Resultado esperado**: Se espera que el estado de revisión de la solicitud no cambie y que el código de estado de la respuesta sea 200.

#### test_set_approval_state_authenticated

  - **Descripción**: Prueba el cambio de estado de aprobación de una solicitud por un usuario autenticado.
  - **Entrada**: Usuario autenticado como administrador, solicitud con estado de aprobación inicial 'None'.
  - **Resultado esperado**: Se espera que la solicitud cambie su estado de aprobación a 'Aprobado' y que el código de estado de la respuesta sea 200.

#### test_set_invalid_approval_state

  - **Descripción**: Prueba el intento de establecer un estado de aprobación no permitido.
  - **Entrada**: Usuario autenticado como administrador, solicitud con estado de aprobación inicial 'None'.
  - **Resultado esperado**: Se espera que el estado de aprobación de la solicitud no cambie y que el código de estado de la respuesta sea 200.


### TestCase

La clase `ViewTestCase` contiene pruebas para verificar el comportamiento de las vistas en el sistema contable.

#### testSummaryOneStopShopView

  - **Descripción**: Prueba de la vista `summaryOneStopShop`.
  - **Entrada**: Usuario autenticado como administrador.
  - **Resultado esperado**: Se espera que la vista devuelva un código de estado 200, use la plantilla 'summaryOneStopShop.html' y pase 'followingData' en el contexto.

#### testFullOneStopShopView

  - **Descripción**: Prueba de la vista `fullOneStopShop`.
  - **Entrada**: Usuario autenticado como administrador.
  - **Resultado esperado**: Se espera que la vista devuelva un código de estado 200, use la plantilla 'fullOneStopShop.html' y pase 'followingData' y 'files' en el contexto.

#### testOneStopShopFormViewGet

  - **Descripción**: Prueba de la vista `OneStopShopForm` con una solicitud GET.
  - **Entrada**: Usuario autenticado como 'Ventanilla única'.
  - **Resultado esperado**: Se espera que la vista devuelva un código de estado 200, use la plantilla 'oneStopShopForm.html' y pase 'oneStopShopForm' y 'attachedDocumentForm' en el contexto.

#### testOneStopShopFormViewPostValid

  - **Descripción**: Prueba de la vista `OneStopShopForm` con una solicitud POST que contiene datos válidos.
  - **Entrada**: Usuario autenticado como 'Ventanilla única'.
  - **Resultado esperado**: Se espera que la vista redireccione a 'OneStopShopForm' después de enviar el formulario correctamente. Se debe crear una instancia de Following con el creador proporcionado y una instancia de AttachedDocument asociada al Following creado.

## Tests unitarios totales

### Comentario de aprobación area contable:
#### Total: 10 tests

### modificación estado de aceptación : 2 tests
### modificación estado de revisión : 2 tests
### modificación estado de aprobación : 2 tests
#### Total: 6 tests

### historial de modificación manual del estado:
#### Total: 3 tests

### Forms test:
#### Total: 4 tests

### Models test:
#### Total: 2 tests

### Modify state:
#### Total: 4 tests

### Search tesT:
#### Total: 5 tests

### views test:
#### Total: 4 tests

### Gestión de permisos
#### Total: 20 tests

### Total Final: 58 tests

### Descripción de tests E2E

#### FormTestCase

Esta clase contiene pruebas de extremo a extremo (E2E) para los formularios de solicitud de la aplicación.

#### setup_data

  - **Descripción**: Configura los datos necesarios para las pruebas.
  - **Resultado esperado**: Los roles y estados se configuran correctamente en la base de datos antes de ejecutar las pruebas.

#### type_text

  - **Descripción**: Simula la escritura de texto en un campo de formulario.
  - **Entrada**: `element` (el elemento del formulario), `text` (el texto a escribir).
  - **Resultado esperado**: El texto se escribe correctamente en el campo de formulario proporcionado.

#### register_user

  - **Descripción**: Prueba el proceso de registro de un nuevo usuario.
  - **Entrada**: `name` (nombre del usuario), `last_name` (apellido del usuario), `email` (correo electrónico del usuario), `rol` (rol del usuario), `password` (contraseña del usuario).
  - **Resultado esperado**: Se espera que el usuario se registre correctamente y se muestre un mensaje de confirmación en la página.

#### login_as_ventanilla

  - **Descripción**: Prueba el proceso de inicio de sesión como usuario de "Ventanilla única".
  - **Resultado esperado**: Se espera que el usuario inicie sesión correctamente y sea redirigido a la página principal después de iniciar sesión.

#### test_onestopshop_form

  - **Descripción**: Prueba la funcionalidad del formulario de "Agregar a ventanilla única".
  - **Resultado esperado**: Se espera que el formulario se llene correctamente y que el envío sea exitoso, mostrando un mensaje de éxito después del envío.


## OneStopShopPermissionTestCase

### Método: setUp

**Descripción**: Configura el entorno de prueba antes de ejecutar las pruebas.

   - Inicializa el navegador web (Chrome) y configura los datos iniciales llamando al método `setup_data()`.

### Método: tearDown

**Descripción**: Limpia el entorno de prueba después de ejecutar las pruebas.

   - Cierra el navegador web.

### Método: type_text

**Descripción**: Simula escribir texto en un campo de entrada.

### Método: setup_data

**Descripción**: Configura los datos iniciales requeridos para las pruebas.

   - Crea los roles en la base de datos si no existen.
   - Llama al método `setup_state()`.

### Método: setup_state

**Descripción**: Crea el estado "En revisión" en la base de datos si no existe.

### Método: setup_roles

**Descripción**: Crea los roles en la base de datos si no existen.

### Método: register_user

**Descripción**: Simula el registro de un nuevo usuario en la aplicación.

   - Abre la página de registro.
   - Rellena el formulario de registro con los datos proporcionados.
   - Envía el formulario de registro.
   - Verifica el registro exitoso.

### Método: login

**Descripción**: Inicia sesión como usuario con las credenciales especificadas.

   - Abre la página de inicio de sesión.
   - Rellena el formulario de inicio de sesión con las credenciales proporcionadas.
   - Envía el formulario de inicio de sesión.

### Método: test_admin_can_access_summary_one_stop_shop_view

**Descripción**: Prueba que un usuario con el rol 'admin' pueda acceder a la vista 'summaryOneStopShopView'.

   - Registra un usuario con el rol 'Administrador'.
   - Inicia sesión como el usuario 'Administrador'.
   - Accede a la vista 'summaryOneStopShopView'.
   - Verifica que se muestre el título adecuado.


### Método: test_lider_can_access_summary_one_stop_shop_view

1. **Descripción**: Prueba que un usuario con el rol 'Líder' pueda acceder a la vista 'summaryOneStopShopView'.
2. **Pasos**:
    - Registrar un usuario con el rol 'Líder'.
    - Iniciar sesión como el usuario 'Líder'.
    - Acceder a la vista 'summaryOneStopShopView'.
    - Verificar que se muestra el título.

### Método: test_gestor_can_access_summary_one_stop_shop_view

1. **Descripción**: Prueba que un usuario con el rol 'Gestor' pueda acceder a la vista 'summaryOneStopShopView'.
2. **Pasos**:
    - Registrar un usuario con el rol 'Gestor'.
    - Iniciar sesión como el usuario 'Gestor'.
    - Acceder a la vista 'summaryOneStopShopView'.
    - Verificar que se muestra el título.

### Método: test_solicitante_cannot_access_summary_one_stop_shop_view

1. **Descripción**: Prueba que un usuario con el rol 'Solicitante' no pueda acceder a la vista 'summaryOneStopShopView' y se muestre el mensaje de error apropiado.
2. **Pasos**:
    - Registrar un usuario con el rol 'Solicitante'.
    - Iniciar sesión como el usuario 'Solicitante'.
    - Intentar acceder a la vista.
    - Verificar que se muestra el mensaje de error.

### Método: test_gestor_can_access_full_one_stop_shop_view

1. **Descripción**: Prueba que un usuario con el rol 'Gestor' pueda acceder a la vista 'fullOneStopShopView'.
2. **Pasos**:
    - Registrar un usuario con el rol 'Gestor'.
    - Iniciar sesión como el usuario 'Gestor'.
    - Acceder a la vista 'fullOneStopShopView'.
    - Verificar que se muestra el título.

### Método: test_admin_can_access_full_one_stop_shop_view

1. **Descripción**: Prueba que un usuario con el rol 'Administrador' pueda acceder a la vista 'fullOneStopShopView'.
2. **Pasos**:
    - Registrar un usuario con el rol 'Administrador'.
    - Iniciar sesión como el usuario 'Administrador'.
    - Acceder a la vista 'fullOneStopShopView'.
    - Verificar que se muestra el título.

### Método: test_solicitante_cannot_access_full_one_stop_shop_view

1. **Descripción**: Prueba que un usuario con el rol 'Solicitante' no pueda acceder a la vista 'fullOneStopShopView' y se muestre el mensaje de error apropiado.
2. **Pasos**:
    - Registrar un usuario con el rol 'Solicitante'.
    - Iniciar sesión como el usuario 'Solicitante'.
    - Intentar acceder a la vista.
    - Verificar que se muestra el mensaje de error.

### Método: test_ventanilla_can_access_one_stop_shop_form_view

1. **Descripción**: Prueba que un usuario con el rol 'Ventanilla única' pueda acceder a la vista 'oneStopShopFormView'.
2. **Pasos**:
    - Registrar un usuario con el rol 'Ventanilla única'.
    - Iniciar sesión como el usuario 'Ventanilla única'.
    - Acceder a la vista 'oneStopShopFormView'.
    - Verificar que se muestra el título.

### Método: test_admin_cannot_access_access_one_stop_shop_form_view

1. **Descripción**: Prueba que un usuario con el rol 'Administrador' no pueda acceder a la vista 'oneStopShopFormView' y se muestre el mensaje de error apropiado.
2. **Pasos**:
    - Registrar un usuario con el rol 'Administrador'.
    - Iniciar sesión como el usuario 'Administrador'.
    - Intentar acceder a la vista.
    - Verificar que se muestra el mensaje de error.

### Método: test_lider_cannot_access_access_one_stop_shop_form_view

1. **Descripción**: Prueba que un usuario con el rol 'Lider' no pueda acceder a la vista 'oneStopShopFormView' y se muestre el mensaje de error apropiado.
2. **Pasos**:
    - Registrar un usuario con el rol 'Lider'.
    - Iniciar sesión como el usuario 'Lider'.
    - Intentar acceder a la vista.
    - Verificar que se muestra el mensaje de error.

### Método: test_gestor_cannot_access_access_one_stop_shop_form_view

1. **Descripción**: Prueba que un usuario con el rol 'Gestor' no pueda acceder a la vista 'oneStopShopFormView' y se muestre el mensaje de error apropiado.
2. **Pasos**:
    - Registrar un usuario con el rol 'Gestor'.
    - Iniciar sesión como el usuario 'Gestor'.
    - Intentar acceder a la vista.
    - Verificar que se muestra el mensaje de error.


### Método: test_update_state_allowed_users

1. **Descripción**: Prueba que un usuario con el rol 'Administrador' o 'Gestor' pueda actualizar el estado correctamente.
2. **Pasos**:
    - Registrar un usuario con permisos.
    - Crear un nuevo objeto Following.
    - Iniciar sesión como el usuario.
    - Intentar acceder a la vista.
    - Cambiar el estado.
    - Verificar que el estado se haya actualizado correctamente.

### Método: test_update_state_not_allowed_users

1. **Descripción**: Prueba que los usuarios sin el rol 'Administrador' o 'Gestor' no puedan actualizar el estado de un seguimiento y se muestre el mensaje de error apropiado.
2. **Pasos**:
    - Registrar un usuario sin permisos.
    - Crear un nuevo objeto Following.
    - Iniciar sesión como el usuario sin permisos.
    - Intentar acceder a la vista.
    - Cambiar el estado.
    - Verificar que se muestra el mensaje de error.
    - Verificar que el estado del seguimiento no haya cambiado.


### Método: test_approval_comment_not_allowed_user

1. **Descripción**: Prueba que un usuario sin el rol 'Administrador' o 'Gestor' no puede agregar un comentario de aprobación.
2. **Pasos**:
    - Registrar un usuario sin permisos.
    - Crear un nuevo objeto Following.
    - Iniciar sesión como el usuario sin permisos.
    - Acceder a la vista de comentario de aprobación.
    - Abrir el modal de comentario de aprobación.
    - Esperar a que el modal se abra.
    - Ingresar un comentario de aprobación.
    - Enviar el formulario.
    - Verificar que se muestra el mensaje de error.
    - Verificar que el comentario de aprobación no haya cambiado.

### Método: test_acceptance_state_not_allowed_user

1. **Descripción**: Prueba que un usuario sin el rol 'Administrador' o 'Gestor' no puede editar el estado de aceptación.
2. **Pasos**:
    - Registrar un usuario sin permisos.
    - Crear un nuevo objeto Following.
    - Iniciar sesión como el usuario sin permisos.
    - Acceder a la vista de comentario de aprobación.
    - Abrir el modal de comentario de aprobación.
    - Esperar a que el modal se abra.
    - Ingresar un comentario de aprobación.
    - Enviar el formulario.
    - Verificar que se muestra el mensaje de error.
    - Verificar que el estado de aceptación no haya cambiado.

### Método: test_revision_state_not_allowed_user

1. **Descripción**: Prueba que un usuario sin el rol 'Administrador' o 'Gestor' no puede editar el estado de revisión.
2. **Pasos**:
    - Registrar un usuario sin permisos.
    - Crear un nuevo objeto Following.
    - Iniciar sesión como el usuario sin permisos.
    - Acceder a la vista de comentario de aceptación.
    - Abrir el modal de comentario de aceptación.
    - Esperar a que el modal se abra.
    - Ingresar un comentario de aceptación.
    - Enviar el formulario.
    - Verificar que se muestra el mensaje de error.
    - Verificar que el estado de aceptación no haya cambiado.

### Método: test_approval_state_not_allowed_user

1. **Descripción**: Prueba que un usuario sin el rol 'Administrador' o 'Gestor' no puede editar el estado de aprobación.
2. **Pasos**:
    - Registrar un usuario sin permisos.
    - Crear un nuevo objeto Following.
    - Iniciar sesión como el usuario sin permisos.
    - Acceder a la vista de edición de estado de aprobación.
    - Intentar abrir el modal de comentario de aprobación.
    - Esperar a que el modal se abra.
    - Ingresar un comentario de aceptación.
    - Enviar el formulario.
    - Verificar que se muestra el mensaje de error.
    - Verificar que el estado de aprobación no haya cambiado.

## Tests E2E totales: 
### 18 tests E2E