## Configuración de Escenarios

### OneStopSearchTest
| Nombre                          | Clase          | Etapa                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|---------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| crear_instancias                | SearchTestCase | Crea instancias de algunos objetos en la base de datos para realizar pruebas.<br>En especial las instancias de los siguientes objetos:<br>- EstadoSolicitud<br>- TipoSolicitud<br>- FechaCreacion<br>- FechaCierre                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| testFiltrarSolicitudPorEstado   | SearchTestCase | Prueba unitaria para verificar el filtrado por estado de las solicitudes.<br>Se crean instancias de solicitudes y se realiza una solicitud GET con el parámetro 'estado', en la cual se supone que el estado es "Aprobado". Luego se realiza la solicitud al controlador 'ventanilla_unica'. Se verifica que la respuesta tenga un código de estado 200 y que el contenido de la respuesta contenga la primera solicitud puesto que su estado es "Aprobado".                                                                                                                                                                                               |
| test_busqueda_solicitud         | SearchTestCase | Prueba la búsqueda de una solicitud.<br>Esta prueba verifica que la función `search_` responda correctamente a una solicitud GET con un parámetro de búsqueda y que devuelva un código de estado 200 junto con el contenido de la solicitud buscada.                                                                                                                                                                                                                                                                                                                                                                             |

### Objetivo del test search

el objetivo de los tests en "search" es probar la funcionalidad del método de búsqueda en el sistema. Este test se encarga de verificar si el método de búsqueda devuelve los resultados esperados cuando se le proporciona un conjunto de datos de entrada específico y el propósito de estos serían asegurarse  que el método de búsqueda está implementado correctamente y que devuelve los resultados correctos de acuerdo con los criterios de búsqueda establecidos.

### Casos de prueba search

| Clase                  | Método                        | Etapa                                                                                                                                                                                                                                                                                                                                                                                            | Valores de Entrada                                                                                                                                                                                                                                                                                                                                                                                                         | Resultado Esperado                                                                                                                                                                                                                                                                                                                          |
|------------------------|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SearchTestCase         | crear_instancias              | Crea instancias de algunos objetos en la base de datos para realizar pruebas. En especial las instancias de los siguientes objetos: EstadoSolicitud, TipoSolicitud, FechaCreacion, FechaCierre                                                                                                                                                                                                   | -                                                                                                                                                                                                                                                                                                                                                                                                                        | Se espera que se creen instancias de objetos en la base de datos para los objetos mencionados, como EstadoSolicitud, TipoSolicitud, FechaCreacion y FechaCierre, que son necesarios para las pruebas relacionadas con la búsqueda y filtrado de solicitudes.                                                                                                                                               |
| SearchTestCase         | testFiltrarSolicitudPorEstado | Prueba unitaria para verificar el filtrado por estado de las solicitudes. Se crean instancias de solicitudes y se realiza una solicitud GET con el parámetro 'estado', en la cual se supone que el estado es "Aprobado". Luego se realiza la solicitud al controlador 'ventanilla_unica'. Se verifica que la respuesta tenga un código de estado 200 y que el contenido de la respuesta contenga la primera solicitud puesto que su estado es "Aprobado". | -                                                                                                                                                                                                                                                                                                                                                                                                                        | Se espera que al filtrar las solicitudes por estado "Aprobado", la vista 'ventanilla_unica' responda con un código de estado 200 y que el contenido de la respuesta contenga la primera solicitud, ya que su estado es "Aprobado".                                                                                                                                                                                   |
| SearchTestCase         | test_busqueda_solicitud       | Prueba la búsqueda de una solicitud. Esta prueba verifica que la función `search_ventanilla` responda correctamente a una solicitud GET con un parámetro de búsqueda y que devuelva un código de estado 200 junto con el contenido de la solicitud buscada.                                                                                                                                | -                                                                                                                                                                                                                                                                                                                                                                                                                        | Se espera que al realizar la búsqueda de solicitudes con el parámetro "requesicion", la vista 'search_ventanilla' responda con un código de estado 200 y que el contenido de la respuesta contenga la solicitud con el tipo "requesicion", asegurando que el método de búsqueda está implementado correctamente y devuelve los resultados correctos de acuerdo con el criterio de búsqueda establecido.  |

## Configuración de Escenarios

### ViewTestCase

| Nombre | Clase        | Etapa |
| ------ | ------------ | ----- |
| setUp  | ViewTestCase | -     |

### Objetivo de los Tests

El objetivo de estos tests es verificar el correcto funcionamiento de las vistas en el sistema contable, incluyendo la renderización de plantillas, el paso de datos de contexto y el procesamiento de formularios.

### Casos de Prueba

| Clase        | Método                    | Etapa                       | Resultado Esperado                                                                                               |
| ------------ | ------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| ViewTestCase | testSummaryOneStopShopView| -                           | Verifica que la vista 'summaryOneStopShop' devuelva un código de estado 200, use la plantilla correcta y pase los datos de contexto requeridos.                           |
| ViewTestCase | testFullOneStopShopView   | -                           | Verifica que la vista 'fullOneStopShop' devuelva un código de estado 200, use la plantilla correcta y pase los datos de contexto requeridos, incluyendo 'followingData' y 'files'. |
| ViewTestCase | testOneStopShopFormViewGet| -                           | Verifica que la vista 'OneStopShopForm' devuelva un código de estado 200, use la plantilla correcta y pase los datos de contexto requeridos, incluyendo 'oneStopShopForm' y 'attachedDocumentForm'. |
| ViewTestCase | testOneStopShopFormViewPostValid| -                    | Verifica que la vista 'OneStopShopForm' redireccione después de una presentación de formulario exitosa y cree las instancias Following y AttachedDocument esperadas.    |

## Configuración de Escenarios

### ModelTestCase

| Nombre | Clase        | Etapa |
| ------ | ------------ | ----- |
| setUp  | ModelTestCase| -     |

### Objetivo de los Tests

El objetivo de estos tests es verificar que los modelos de las aplicaciones funcionen correctamente, incluyendo la creación de instancias con datos válidos y la representación de cadenas esperada.

### Casos de Prueba

| Clase        | Método                    | Etapa   | Resultado Esperado                                                                                                          |
| ------------ | ------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------- |
| ModelTestCase | testFollowingModel       | -       | Verifica que el modelo Following cree instancias correctamente y devuelva la representación de cadena esperada.           |
| ModelTestCase | testAttachedDocumentModel| -       | Verifica que el modelo AttachedDocument cree instancias correctamente y devuelva la representación de cadena esperada.   |

## Configuración de Escenarios

### FormTestCase

| Nombre | Clase       | Etapa |
| ------ | ----------- | ----- |
| setUp  | FormTestCase| -     |

### Objetivo de los Tests

El objetivo de estos tests es verificar que los formularios de la aplicación funcionen correctamente, tanto con datos válidos como con datos inválidos.

### Casos de Prueba

| Clase       | Método                 | Etapa | Resultado Esperado                                                                                         |
| ----------- | ---------------------- | ----- | ---------------------------------------------------------------------------------------------------------- |
| FormTestCase| testOneStopShopValidForm   | -     | Verificar que el formulario OneStopShopForm sea válido cuando se le proporcionan datos válidos.          |
| FormTestCase| testAttachedDocumentValidForm | - | Verificar que el formulario AttachedDocumentForm sea válido cuando se le proporcionan datos de archivo válidos. |
| FormTestCase| testOneStopShopInvalidForm  | -     | Verificar que el formulario OneStopShopForm sea inválido cuando se le proporcionan datos incompletos.      |
| FormTestCase| testAttachedDocumentInvalidForm| - | Verificar que el formulario AttachedDocumentForm sea inválido cuando se le proporcionan datos de archivo incorrectos. |


                                                                                                                                                                                               