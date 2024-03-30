## Configuración de Escenarios

### ChargeAccountFormTests

| Nombre | Clase                  | Etapa                                                                                                                                                                                                                                                                                                                                                                    |
| ------ | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| setUp1 | ChargeAccountFormTests | name: 'Pablo', identification: '1234567890', phone: '1234567890', city: 'Bogota', addres: 'Calle 123', date: '2023-04-01', value_letters: 'Cien mil pesos', value_numbers: '100000', concept: 'Concepto de prueba', bank: 'Banco de Prueba', type: 'De ahorros', account_number: '1234567890', cex: '12345', retentions: True, declarant: True, colombian_resident: True |
| setUp2 | ChargeAccountFormTests | Todos los campos vacíos                                                                                                                                                                                                                                                                                                                                                  |

### RequisitionFormTests

| Nombre | Clase                | Etapa                                                                                                                                                                                                                                                                                                                                                                                         |
| ------ | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| setUp1 | RequisitionFormTests | date: '2023-04-01', beneficiaryName: 'Pablo', idNumber: '1234567890', charge: 'Developer', dependency: 'IT Department', cenco: '1234', value: '100000.50', concept: 'Reintegro colaboradores', description: 'Descripción de prueba', radicate: '12345', payment_order_code: '67890', paymentMethod: 'Nomina', typeAccount: 'De ahorros', account_number: '1234567890', authorName: 'Fernando' |
| setUp2 | RequisitionFormTests | Todos los campos vacíos                                                                                                                                                                                                                                                                                                                                                                       |

### Casos de Prueba

Objetivo del test: Probar el correcto funcionamiento de los formularios de cuenta de cobro y requisición.

| Clase                  | Método            | Etapa  | Valores de Entrada | Resultado Esperado              |
| ---------------------- | ----------------- | ------ | ------------------ | ------------------------------- |
| ChargeAccountFormTests | test_valid_form   | setUp1 | Datos válidos      | El formulario debe ser válido   |
| ChargeAccountFormTests | test_blank_fields | setUp2 | Campos vacíos      | El formulario debe ser inválido |
| RequisitionFormTests   | test_valid_form   | setUp1 | Datos válidos      | El formulario debe ser válido   |
| RequisitionFormTests   | test_blank_fields | setUp2 | Campos vacíos      | El formulario debe ser inválido |

<br>
<br>
<br>

## Configuración de Escenarios

### ChargeAccountModelTests

| Nombre | Clase                   | Etapa                                                                                                                                                                                                                                                                                                                                                                    |
| ------ | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| setUp  | ChargeAccountModelTests | name: 'Pablo', identification: '1234567890', phone: '1234567890', city: 'Bogota', addres: 'Calle 123', date: '2023-04-01', value_letters: 'Cien mil pesos', value_numbers: '100000', concept: 'Concepto de prueba', bank: 'Banco de Prueba', type: 'De ahorros', account_number: '1234567890', cex: '12345', retentions: True, declarant: True, colombian_resident: True |

### RequisitionModelTests

| Nombre | Clase                 | Etapa                                                                                                                                                                                                                                                                                                                                                                                         |
| ------ | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| setUp  | RequisitionModelTests | date: '2023-04-01', beneficiaryName: 'Pablo', idNumber: '1234567890', charge: 'Developer', dependency: 'IT Department', cenco: '1234', value: '100000.50', concept: 'Reintegro colaboradores', description: 'Descripción de prueba', radicate: '12345', payment_order_code: '67890', paymentMethod: 'Nomina', typeAccount: 'De ahorros', account_number: '1234567890', authorName: 'Fernando' |

### Casos de Prueba

Objetivo del test: Probar la correcta creación de instancias de los modelos Charge_account y Requisition.

| Clase                   | Método                     | Etapa | Valores de Entrada | Resultado Esperado                            |
| ----------------------- | -------------------------- | ----- | ------------------ | --------------------------------------------- |
| ChargeAccountModelTests | test_create_charge_account | setUp | Datos válidos      | Se debe crear una instancia de Charge_account |
| RequisitionModelTests   | test_create_requisition    | setUp | Datos válidos      | Se debe crear una instancia de Requisition    |

<br>
<br>
<br>

## Configuración de Escenarios

### ChargeAccountFormViewTests

| Nombre | Clase                      | Etapa                                                                                                                                                                                                                                                                                                                                                                    |
| ------ | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| setUp  | ChargeAccountFormViewTests | name: 'Pablo', identification: '1234567890', phone: '1234567890', city: 'Bogota', addres: 'Calle 123', date: '2023-04-01', value_letters: 'Cien mil pesos', value_numbers: '100000', concept: 'Concepto de prueba', bank: 'Banco de Prueba', type: 'De ahorros', account_number: '1234567890', cex: '12345', retentions: True, declarant: True, colombian_resident: True |

### RequisitionFormViewTests

| Nombre | Clase                    | Etapa                                                                                                                                                                                                                                                                                                                                                                                         |
| ------ | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| setUp  | RequisitionFormViewTests | date: '2023-04-01', beneficiaryName: 'Pablo', idNumber: '1234567890', charge: 'Developer', dependency: 'IT Department', cenco: '1234', value: '100000.50', concept: 'Reintegro colaboradores', description: 'Descripción de prueba', radicate: '12345', payment_order_code: '67890', paymentMethod: 'Nomina', typeAccount: 'De ahorros', account_number: '1234567890', authorName: 'Fernando' |

### Casos de Prueba

Objetivo del test: Probar el correcto funcionamiento de las vistas de los formularios de cuenta de cobro y requisición.

| Clase                      | Método         | Etapa | Valores de Entrada | Resultado Esperado                                      |
| -------------------------- | -------------- | ----- | ------------------ | ------------------------------------------------------- |
| ChargeAccountFormViewTests | test_get_form  | setUp | -                  | La vista debe renderizar correctamente el formulario    |
| ChargeAccountFormViewTests | test_post_form | setUp | Datos válidos      | El formulario debe procesarse correctamente y redirigir |
| RequisitionFormViewTests   | test_get_form  | setUp | -                  | La vista debe renderizar correctamente el formulario    |
| RequisitionFormViewTests   | test_post_form | setUp | Datos válidos      | El formulario debe procesarse correctamente y redirigir |