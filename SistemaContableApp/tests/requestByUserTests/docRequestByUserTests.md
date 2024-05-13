# Pruebas Unitarias sobre el modulo de Requests

## Descripción de tests unitarios

### IsLateRequestTestCase

Esta clase contiene pruebas para la función `isLateRequest` que determina si una fecha de solicitud es posterior al día 20 del mes actual.

#### test_is_late_request_true
- **Descripción**: Verifica que `isLateRequest` retorna `True` cuando la fecha de solicitud es posterior al día 20 del mes actual.
- **Valores de Entrada**: `request_date = datetime(2024, 5, 21)`
- **Resultado Esperado**: `True`

#### test_is_late_request_false  
- **Descripción**: Verifica que `isLateRequest` retorna `False` cuando la fecha de solicitud es anterior al día 20 del mes actual.
- **Valores de Entrada**: `request_date = datetime(2024, 5, 15)`  
- **Resultado Esperado**: `False`

#### test_is_late_request_same_month
- **Descripción**: Verifica que `isLateRequest` retorna `False` cuando la fecha de solicitud es el día 20 del mes actual.
- **Valores de Entrada**: `request_date = datetime(today.year, today.month, 20)`
- **Resultado Esperado**: `False`

### ViewsTestCase

Esta clase contiene pruebas para las vistas relacionadas con los formularios de cuenta de recaudo, requisición, pago al exterior, legalización y solicitud de anticipo.

#### test_get_charge_account_form
- **Descripción**: Verifica que el formulario de cuenta de recaudo se renderiza correctamente en una solicitud GET.
- **Valores de Entrada**: Ninguno
- **Resultado Esperado**: El código de estado de la respuesta es 200 y se utiliza la plantilla 'chargeAccountForm.html'.

#### test_create_charge_account_form
- **Descripción**: Verifica que una cuenta de recaudo se crea correctamente en una solicitud POST con datos de formulario válidos.
- **Valores de Entrada**: Datos de formulario válidos
- **Resultado Esperado**: El código de estado de la respuesta es 302 y se crea una instancia de `Charge_account` con los datos proporcionados.

#### test_get_exterior_payment_form
- **Descripción**: Verifica que el formulario de pago al exterior se renderiza correctamente en una solicitud GET.
- **Valores de Entrada**: Ninguno
- **Resultado Esperado**: El código de estado de la respuesta es 200 y se utiliza la plantilla 'exteriorPaymentForm.html'.

#### test_create_exterior_payment_form
- **Descripción**: Verifica que un pago al exterior se crea correctamente en una solicitud POST con datos de formulario válidos.
- **Valores de Entrada**: Datos de formulario válidos
- **Resultado Esperado**: El código de estado de la respuesta es 302 y se crea una instancia de `Exterior_payment` con los datos proporcionados.

#### test_get_requisition_form
- **Descripción**: Verifica que el formulario de requisición se renderiza correctamente en una solicitud GET.
- **Valores de Entrada**: Ninguno
- **Resultado Esperado**: El código de estado de la respuesta es 200 y se utiliza la plantilla 'requisitionForm.html'.

#### test_create_requisition_form
- **Descripción**: Verifica que una requisición se crea correctamente en una solicitud POST con datos de formulario válidos.
- **Valores de Entrada**: Datos de formulario válidos
- **Resultado Esperado**: El código de estado de la respuesta es 302 y se crea una instancia de `Requisition` con los datos proporcionados.

#### test_get_legalization_form
- **Descripción**: Verifica que el formulario de legalización se renderiza correctamente en una solicitud GET.
- **Valores de Entrada**: Ninguno
- **Resultado Esperado**: El código de estado de la respuesta es 200 y se utiliza la plantilla 'legalizationForm.html'.

#### test_create_legalization_form
- **Descripción**: Verifica que una legalización se crea correctamente en una solicitud POST con datos de formulario válidos.
- **Valores de Entrada**: Datos de formulario válidos
- **Resultado Esperado**: El código de estado de la respuesta es 302 y se crea una instancia de `Legalization` con los datos proporcionados, incluyendo los gastos asociados.

#### test_get_advance_solicitation_form  
- **Descripción**: Verifica que el formulario de solicitud de anticipo se renderiza correctamente en una solicitud GET.
- **Valores de Entrada**: Ninguno
- **Resultado Esperado**: El código de estado de la respuesta es 200 y se utiliza la plantilla 'advancePaymentForm.html'.

#### test_create_travel_advance_solicitation_form
- **Descripción**: Verifica que una solicitud de anticipo de viaje se crea correctamente en una solicitud POST con datos de formulario válidos.
- **Valores de Entrada**: Datos de formulario válidos
- **Resultado Esperado**: El código de estado de la respuesta es 302 y se crea una instancia de `AdvancePayment` con los datos proporcionados, incluyendo los gastos asociados.

### ExcelGenerationTestCase

Esta clase contiene pruebas para la generación de archivos Excel a partir de los objetos del sistema.

#### test_generate_excel_charge_account
- **Descripción**: Verifica que un archivo Excel se genera correctamente a partir de un objeto `Charge_account`.
- **Valores de Entrada**: Instancia de `Charge_account`
- **Resultado Esperado**: Se genera un archivo Excel con la extensión `.xlsx`.

#### test_generate_excel_exterior_payment
- **Descripción**: Verifica que un archivo Excel se genera correctamente a partir de un objeto `Exterior_payment`.
- **Valores de Entrada**: Instancia de `Exterior_payment`
- **Resultado Esperado**: Se genera un archivo Excel con la extensión `.xlsx`.

#### test_generate_excel_requisition
- **Descripción**: Verifica que un archivo Excel se genera correctamente a partir de un objeto `Requisition`.
- **Valores de Entrada**: Instancia de `Requisition`
- **Resultado Esperado**: Se genera un archivo Excel con la extensión `.xlsx`.

#### test_generate_excel_legalization
- **Descripción**: Verifica que un archivo Excel se genera correctamente a partir de un objeto `Legalization`.
- **Valores de Entrada**: Instancia de `Legalization`  
- **Resultado Esperado**: Se genera un archivo Excel con la extensión `.xlsx`.

#### test_generate_excel_advance_payment
- **Descripción**: Verifica que un archivo Excel se genera correctamente a partir de un objeto `AdvancePayment`.
- **Valores de Entrada**: Instancia de `AdvancePayment`
- **Resultado Esperado**: Se genera un archivo Excel con la extensión `.xlsx`.

### FormCreationViewTestCase

Esta clase contiene pruebas para verificar el acceso a los formularios según los roles de usuario.

#### test_createChargeAccountForm_allowed
- **Descripción**: Verifica que un usuario con el rol de 'Solicitante' puede acceder al formulario de cuenta de recaudo.
- **Valores de Entrada**: Ninguno
- **Resultado Esperado**: El código de estado de la respuesta es 200 y se renderiza el formulario `ChargeAccountForm`.

#### test_createChargeAccountForm_not_allowed
- **Descripción**: Verifica que un usuario con el rol de 'Contable' no puede acceder al formulario de cuenta de recaudo.
- **Valores de Entrada**: Ninguno
- **Resultado Esperado**: El código de estado de la respuesta es 302 (redirección).

#### test_createRequisitionForm_allowed
- **Descripción**: Verifica que un usuario con el rol de 'Solicitante' puede acceder al formulario de requisición.
- **Valores de Entrada**: Ninguno
- **Resultado Esperado**: El código de estado de la respuesta es 200 y se renderiza el formulario `RequisitionForm`.

#### test_createRequisitionForm_not_allowed
- **Descripción**: Verifica que un usuario con el rol de 'Contable' no puede acceder al formulario de requisición.
- **Valores de Entrada**: Ninguno
- **Resultado Esperado**: El código de estado de la respuesta es 302 (redirección).

#### test_createExteriorPaymentForm_allowed
- **Descripción**: Verifica que un usuario con el rol de 'Solicitante' puede acceder al formulario de pago al exterior.
- **Valores de Entrada**: Ninguno
- **Resultado Esperado**: El código de estado de la respuesta es 200 y se renderiza el formulario `ExteriorPaymentForm`.

#### test_createExteriorPaymentForm_not_allowed
- **Descripción**: Verifica que un usuario con el rol de 'Contable' no puede acceder al formulario de pago al exterior.
- **Valores de Entrada**: Ninguno
- **Resultado Esperado**: El código de estado de la respuesta es 302 (redirección).

#### test_createLegalizationForm_allowed
- **Descripción**: Verifica que un usuario con el rol de 'Solicitante' puede acceder al formulario de legalización.
- **Valores de Entrada**: Ninguno
- **Resultado Esperado**: El código de estado de la respuesta es 200 y se renderiza el formulario `TravelExpensesSolicitationForm`.

#### test_createLegalizationForm_not_allowed
- **Descripción**: Verifica que un usuario con el rol de 'Contable' no puede acceder al formulario de legalización.
- **Valores de Entrada**: Ninguno
- **Resultado Esperado**: El código de estado de la respuesta es 302 (redirección).

#### test_createAdvancePaymentForm_allowed
- **Descripción**: Verifica que un usuario con el rol de 'Solicitante' puede acceder al formulario de solicitud de anticipo.
- **Valores de Entrada**: Ninguno
- **Resultado Esperado**: El código de estado de la respuesta es 200 y se renderiza el formulario `TravelAdvanceSolicitationForm`.

#### test_createAdvancePaymentForm_not_allowed
- **Descripción**: Verifica que un usuario con el rol de 'Contable' no puede acceder al formulario de solicitud de anticipo.
- **Valores de Entrada**: Ninguno
- **Resultado Esperado**: El código de estado de la respuesta es 302 (redirección).

### ModelTests

Esta sección contiene pruebas unitarias para verificar el correcto funcionamiento de los modelos de datos utilizados en la aplicación. Estas pruebas comprueban la creación de instancias de los modelos con datos válidos, la integridad de los campos y las opciones de selección (choices) para los campos correspondientes.

#### ChargeAccountModelTests

##### test_create_charge_account
- **Descripción**: Verifica que se puede crear una instancia de `Charge_account` con datos válidos.
- **Valores de Entrada**: Datos válidos para crear una instancia de `Charge_account`
- **Resultado Esperado**: Se crea una instancia de `Charge_account` con los datos proporcionados.

#### RequisitionModelTests  

##### test_create_requisition
- **Descripción**: Verifica que se puede crear una instancia de `Requisition` con datos válidos.
- **Valores de Entrada**: Datos válidos para crear una instancia de `Requisition`
- **Resultado Esperado**: Se crea una instancia de `Requisition` con los datos proporcionados.

#### ExteriorPaymentModelTests

##### test_create_exterior_payment
- **Descripción**: Verifica que se puede crear una instancia de `Exterior_payment` con datos válidos.
- **Valores de Entrada**: Datos válidos para crear una instancia de `Exterior_payment`
- **Resultado Esperado**: Se crea una instancia de `Exterior_payment` con los datos proporcionados.

##### test_exterior_payment_fields
- **Descripción**: Verifica que el modelo `Exterior_payment` tiene los campos esperados.
- **Valores de Entrada**: Ninguno
- **Resultado Esperado**: Los campos del modelo `Exterior_payment` coinciden con los campos esperados.

##### test_exterior_payment_choices
- **Descripción**: Verifica que el modelo `Exterior_payment` tiene las opciones correctas para los campos `account_type` e `iban_aba_code_type`.
- **Valores de Entrada**: Ninguno
- **Resultado Esperado**: Las opciones de los campos `account_type` e `iban_aba_code_type` coinciden con las esperadas.

#### LegalizationModelTests

##### test_create_legalization
- **Descripción**: Verifica que se puede crear una instancia de `Legalization` con datos válidos.
- **Valores de Entrada**: Datos válidos para crear una instancia de `Legalization`
- **Resultado Esperado**: Se crea una instancia de `Legalization` con los datos proporcionados.

##### test_fields_legalization
- **Descripción**: Verifica que los campos de una instancia de `Legalization` tienen los valores esperados.
- **Valores de Entrada**: Datos válidos para crear una instancia de `Legalization`
- **Resultado Esperado**: Los valores de los campos `traveler_name` y `currency_type_of_advance_value` coinciden con los valores esperados.

#### AdvancePaymentModelTests  

##### test_create_advance_payment
- **Descripción**: Verifica que se puede crear una instancia de `AdvancePayment` con datos válidos.
- **Valores de Entrada**: Datos válidos para crear una instancia de `AdvancePayment`
- **Resultado Esperado**: Se crea una instancia de `AdvancePayment` con los datos proporcionados.

##### test_fields_advance_payment
- **Descripción**: Verifica que los campos de una instancia de `AdvancePayment` tienen los valores esperados.
- **Valores de Entrada**: Datos válidos para crear una instancia de `AdvancePayment`
- **Resultado Esperado**: Los valores de los campos `traveler_name` y `currency_type_of_advance_value` coinciden con los valores esperados.

### FormTests

Esta sección contiene pruebas unitarias para verificar el correcto funcionamiento de los formularios utilizados en la aplicación. Estas pruebas aseguran que los formularios validen correctamente los datos de entrada y que cumplan con las reglas de negocio establecidas.

#### ChargeAccountFormTests

##### test_valid_form
- **Descripción**: Verifica que el formulario `ChargeAccountForm` es válido con datos de entrada válidos.
- **Valores de Entrada**: Datos válidos para el formulario `ChargeAccountForm`
- **Resultado Esperado**: El formulario es válido.

##### test_blank_fields
- **Descripción**: Verifica que el formulario `ChargeAccountForm` es inválido si se dejan campos obligatorios en blanco.
- **Valores de Entrada**: Campos obligatorios en blanco
- **Resultado Esperado**: El formulario es inválido.

#### RequisitionFormTests

##### test_valid_form
- **Descripción**: Verifica que el formulario `RequisitionForm` es válido con datos de entrada válidos.
- **Valores de Entrada**: Datos válidos para el formulario `RequisitionForm`
- **Resultado Esperado**: El formulario es válido.

##### test_blank_fields
- **Descripción**: Verifica que el formulario `RequisitionForm` es inválido si se dejan campos obligatorios en blanco.
- **Valores de Entrada**: Campos obligatorios en blanco
- **Resultado Esperado**: El formulario es inválido.

#### ExteriorPaymentFormTests

##### test_form_fields
- **Descripción**: Verifica que el formulario `ExteriorPaymentForm` contiene todos los campos esperados.
- **Valores de Entrada**: Ninguno
- **Resultado Esperado**: El formulario contiene los campos esperados.

##### test_form_valid_data
- **Descripción**: Verifica que el formulario `ExteriorPaymentForm` es válido con datos de entrada válidos.
- **Valores de Entrada**: Datos válidos para el formulario `ExteriorPaymentForm`
- **Resultado Esperado**: El formulario es válido.

##### test_form_invalid_data
- **Descripción**: Verifica que el formulario `ExteriorPaymentForm` es inválido con datos de entrada inválidos.
- **Valores de Entrada**: Datos inválidos para el formulario `ExteriorPaymentForm`
- **Resultado Esperado**: El formulario es inválido.

#### TravelExpensesSolicitationFormTests

##### test_valid_form
- **Descripción**: Verifica que el formulario `TravelExpensesSolicitationForm` es válido con datos de entrada válidos.
- **Valores de Entrada**: Datos válidos para el formulario `TravelExpensesSolicitationForm`
- **Resultado Esperado**: El formulario es válido.

##### test_blank_fields
- **Descripción**: Verifica que el formulario `TravelExpensesSolicitationForm` es inválido si se dejan campos obligatorios en blanco.
- **Valores de Entrada**: Campos obligatorios en blanco
- **Resultado Esperado**: El formulario es inválido.

#### TravelAdvanceSolicitationFormTests

##### test_valid_form
- **Descripción**: Verifica que el formulario `TravelAdvanceSolicitationForm` es válido con datos de entrada válidos.
- **Valores de Entrada**: Datos válidos para el formulario `TravelAdvanceSolicitationForm`
- **Resultado Esperado**: El formulario es válido.

##### test_blank_fields
- **Descripción**: Verifica que el formulario `TravelAdvanceSolicitationForm` es inválido si se dejan campos obligatorios en blanco.
- **Valores de Entrada**: Campos obligatorios en blanco
- **Resultado Esperado**: El formulario es inválido.


## Tests unitarios totales

### Cuenta de Cobro (Charge Account):
#### Total: 13 tests

### Requisición (Requisition):  
#### Total: 8 tests

### Pago al Exterior (Exterior Payment):
#### Total: 11 tests

### Legalización (Legalization):
#### Total: 7 tests

### Solicitud de Anticipo (Advance Payment):
#### Total: 9 tests

### Total Final: 48 tests


## Descripción de tests E2E

### RequestsTestCase

Esta clase contiene pruebas de extremo a extremo (e2e) para los formularios de solicitud de la aplicación.

#### setup_data
- **Descripción**: Configura los datos iniciales requeridos para las pruebas, incluyendo la creación de los roles en la base de datos si no existen.
- **Valores de Entrada**: Ninguno.
- **Resultado Esperado**: Los roles necesarios están creados en la base de datos.

#### register_user
- **Descripción**: Simula el registro de un nuevo usuario en la aplicación.
- **Valores de Entrada**: Nombre, apellido, correo electrónico, rol y contraseña del usuario.
- **Resultado Esperado**: El usuario se registra correctamente, y se muestran los mensajes de éxito correspondientes en la página.

#### login_as_admin
- **Descripción**: Inicia sesión en la aplicación como un usuario administrador.
- **Valores de Entrada**: Credenciales de inicio de sesión del administrador (correo electrónico y contraseña).
- **Resultado Esperado**: El usuario administrador inicia sesión correctamente.

#### test_charge_account_form
- **Descripción**: Prueba el formulario de solicitud de cuenta de recaudo.
- **Pasos**:
  1. Registra un usuario administrador.
  2. Inicia sesión como administrador.
  3. Navega al formulario de solicitud de cuenta de recaudo.
  4. Completa todos los campos requeridos del formulario.
  5. Envía el formulario.
- **Resultado Esperado**: El formulario se envía correctamente, y se muestra un mensaje de éxito.

#### test_exterior_payment_form
- **Descripción**: Prueba el formulario de solicitud de pago al exterior.
- **Pasos**:
  1. Registra un usuario administrador.
  2. Inicia sesión como administrador.
  3. Navega al formulario de solicitud de pago al exterior.
  4. Completa todos los campos requeridos del formulario.
  5. Envía el formulario.
- **Resultado Esperado**: El formulario se envía correctamente, y se muestra un mensaje de éxito.

#### test_requisition_form
- **Descripción**: Prueba el formulario de solicitud de requisición.
- **Pasos**:
  1. Registra un usuario administrador.
  2. Inicia sesión como administrador.
  3. Navega al formulario de solicitud de requisición.
  4. Completa todos los campos requeridos del formulario.
  5. Envía el formulario.
- **Resultado Esperado**: El formulario se envía correctamente, y se muestra un mensaje de éxito.

#### test_legalization_form
- **Descripción**: Prueba el formulario de solicitud de legalización.
- **Pasos**:
  1. Registra un usuario administrador.
  2. Inicia sesión como administrador.
  3. Navega al formulario de solicitud de legalización.
  4. Completa todos los campos requeridos del formulario.
  5. Envía el formulario.
- **Resultado Esperado**: El formulario se envía correctamente, y se muestra un mensaje de éxito.

#### test_advance_payment_form
- **Descripción**: Prueba el formulario de solicitud de anticipo.
- **Pasos**:
  1. Registra un usuario administrador.
  2. Inicia sesión como administrador.
  3. Navega al formulario de solicitud de anticipo.
  4. Completa todos los campos requeridos del formulario.
  5. Envía el formulario.
- **Resultado Esperado**: El formulario se envía correctamente, y se muestra un mensaje de éxito.

Estas pruebas 2E2 simulan la interacción de un usuario con la aplicación web, incluyendo el registro, inicio de sesión, navegación a los formularios de solicitud, llenado de campos y envío de los formularios. Cada prueba verifica que el formulario correspondiente se envía correctamente y se muestra un mensaje de éxito después de enviar el formulario.


## Tests E2E totales: 
### 5 tests E2E
