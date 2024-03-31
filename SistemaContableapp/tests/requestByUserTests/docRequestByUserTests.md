## Configuración de Escenarios

### ChargeAccountFormTests

| Nombre | Clase                  | Etapa                                                                                                                                                                                                                                                                                                                                                                    |
| ------ | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| setUp1 | ChargeAccountFormTests | name: 'Pablo', identification: '1234567890', phone: '1234567890', city: 'Bogota', addres: 'Calle 123', date: '2023-04-01', value_letters: 'Cien mil pesos', value_numbers: '100000', concept: 'Concepto de prueba', bank: 'Banco de Prueba', type: 'De ahorros', account_number: '1234567890', cex: '12345', retentions: True, declarant: True, colombian_resident: True |
| setUp2 | ChargeAccountFormTests | name: '', identification: '', phone: '', city: '', addres: '', date: '', value_letters: '', value_numbers: '', concept: '', bank: '', type: '', account_number: '', cex: '', retentions: False, declarant: False, colombian_resident: False                                                                                                                              |

### RequisitionFormTests

| Nombre | Clase                | Etapa                                                                                                                                                                                                                                                                                                                                                                                         |
| ------ | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| setUp3 | RequisitionFormTests | date: '2023-04-01', beneficiaryName: 'Pablo', idNumber: '1234567890', charge: 'Developer', dependency: 'IT Department', cenco: '1234', value: '100000.50', concept: 'Reintegro colaboradores', description: 'Descripción de prueba', radicate: '12345', payment_order_code: '67890', paymentMethod: 'Nomina', typeAccount: 'De ahorros', account_number: '1234567890', authorName: 'Fernando' |
| setUp4 | RequisitionFormTests | date: '', beneficiaryName: '', idNumber: '', charge: '', dependency: '', cenco: '', value: '', concept: '', description: '', radicate: '', payment_order_code: '', paymentMethod: '', typeAccount: '', account_number: '', authorName: ''                                                                                                                                                     |

### ExteriorPaymentFormTests

| Nombre | Clase                    | Etapa                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------ | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| setUp5 | ExteriorPaymentFormTests | beneficiary_name: 'Daniela', beneficiary_last_name: 'Londoño', beneficiary_document_type: 'DNI', beneficiary_document_no: '12345678', passport_number: 'ABC123456', passport_expedition_city: 'Cali', address: 'calle 25', bank_name: 'Bancolombia', account_type: 'Ahorros', swift_code: 'BOFAUS3N', iban_aba_code_type: 'IBAN', iban_aba_code: '01010101', account_name: 'Daniela Londoño', account_number: '1234567890', bank_address: 'calle 32' |
| setUp6 | ExteriorPaymentFormTests | beneficiary_name: '', beneficiary_last_name: '', beneficiary_document_type: '', beneficiary_document_no: '', passport_number: '', passport_expedition_city: '', address: 'calle 25', bank_name: 'Bancolombia', account_type: 'Ahorros', swift_code: '111111111111', iban_aba_code_type: 'IBAN', iban_aba_code: '', account_name: 'Daniela Londoño', account_number: '1234567890', bank_address: 'calle 32'                                           |

### Objetivo de los Tests

El objetivo de estos tests es verificar el correcto funcionamiento de los formularios de cuenta de cobro, requisición y pago al exterior, asegurando que los campos obligatorios sean validados correctamente y que los formularios sean válidos cuando se ingresen datos correctos.

### Casos de Prueba

| Clase                    | Método                 | Etapa  | Valores de Entrada | Resultado Esperado                                              |
| ------------------------ | ---------------------- | ------ | ------------------ | --------------------------------------------------------------- |
| ChargeAccountFormTests   | test_valid_form        | setUp1 | Datos válidos      | El formulario debe ser válido                                   |
| ChargeAccountFormTests   | test_blank_fields      | setUp2 | Campos vacíos      | El formulario debe ser inválido                                 |
| RequisitionFormTests     | test_valid_form        | setUp3 | Datos válidos      | El formulario debe ser válido                                   |
| RequisitionFormTests     | test_blank_fields      | setUp4 | Campos vacíos      | El formulario debe ser inválido                                 |
| ExteriorPaymentFormTests | test_form_fields       | -      | -                  | Verificar que el formulario contiene todos los campos esperados |
| ExteriorPaymentFormTests | test_form_valid_data   | setUp5 | Datos válidos      | El formulario debe ser válido                                   |
| ExteriorPaymentFormTests | test_form_invalid_data | setUp6 | Datos inválidos    | El formulario debe ser inválido                                 |





## Configuración de Escenarios

### ChargeAccountModelTests

| Nombre | Clase                   | Etapa                                                                                                                                                                                                                                                                                                                                                                    |
| ------ | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| setUp1 | ChargeAccountModelTests | name: 'Pablo', identification: '1234567890', phone: '1234567890', city: 'Bogota', addres: 'Calle 123', date: '2023-04-01', value_letters: 'Cien mil pesos', value_numbers: '100000', concept: 'Concepto de prueba', bank: 'Banco de Prueba', type: 'De ahorros', account_number: '1234567890', cex: '12345', retentions: True, declarant: True, colombian_resident: True |

### RequisitionModelTests

| Nombre | Clase                 | Etapa                                                                                                                                                                                                                                                                                                                                                                                         |
| ------ | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| setUp2 | RequisitionModelTests | date: '2023-04-01', beneficiaryName: 'Pablo', idNumber: '1234567890', charge: 'Developer', dependency: 'IT Department', cenco: '1234', value: '100000.50', concept: 'Reintegro colaboradores', description: 'Descripción de prueba', radicate: '12345', payment_order_code: '67890', paymentMethod: 'Nomina', typeAccount: 'De ahorros', account_number: '1234567890', authorName: 'Fernando' |

### ExteriorPaymentModelTests

| Nombre | Clase                     | Etapa                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------ | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| setUp3 | ExteriorPaymentModelTests | beneficiary_name: 'Daniela', beneficiary_last_name: 'Londoño', beneficiary_document_type: 'DNI', beneficiary_document_no: '12345678', passport_number: 'ABC123456', passport_expedition_city: 'Cali', address: 'calle 25', bank_name: 'Bancolombia', account_type: 'Ahorros', swift_code: 'BOFAUS3N', iban_aba_code_type: 'IBAN', iban_aba_code: '01010101', account_name: 'Daniela Londoño', account_number: '1234567890', bank_address: 'calle 32' |

### Objetivo de los Tests de Modelos

El objetivo de estos tests es verificar que los modelos de las aplicaciones funcionen correctamente, incluyendo la creación de instancias con datos válidos, la integridad de los campos y las opciones de selección (choices) para los campos correspondientes.

### Casos de Prueba de Modelos

| Clase                     | Método                        | Etapa  | Resultado Esperado                                                                                           |
| ------------------------- | ----------------------------- | ------ | ------------------------------------------------------------------------------------------------------------ |
| ChargeAccountModelTests   | test_create_charge_account    | setUp1 | Crear una instancia de Charge_account con los datos proporcionados                                           |
| RequisitionModelTests     | test_create_requisition       | setUp2 | Crear una instancia de Requisition con los datos proporcionados                                              |
| ExteriorPaymentModelTests | test_create_exterior_payment  | setUp3 | Crear una instancia de Exterior_payment con los datos proporcionados                                         |
| ExteriorPaymentModelTests | test_exterior_payment_fields  | -      | Verificar que el modelo Exterior_payment tenga los campos esperados                                          |
| ExteriorPaymentModelTests | test_exterior_payment_choices | -      | Verificar que el modelo Exterior_payment tenga las opciones correctas para account_type e iban_aba_code_type |



## Configuración de Escenarios

### ChargeAccountFormViewTests

| Nombre | Clase                      | Etapa                                                                                                                                                                                                                                                                                                                                                                    |
| ------ | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| setUp1 | ChargeAccountFormViewTests | name: 'Pablo', identification: '1234567890', phone: '1234567890', city: 'Bogota', addres: 'Calle 123', date: '2023-04-01', value_letters: 'Cien mil pesos', value_numbers: '100000', concept: 'Concepto de prueba', bank: 'Banco de Prueba', type: 'De ahorros', account_number: '1234567890', cex: '12345', retentions: True, declarant: True, colombian_resident: True |

### RequisitionFormViewTests

| Nombre | Clase                    | Etapa                                                                                                                                                                                                                                                                                                                                                                                         |
| ------ | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| setUp2 | RequisitionFormViewTests | date: '2023-04-01', beneficiaryName: 'Pablo', idNumber: '1234567890', charge: 'Developer', dependency: 'IT Department', cenco: '1234', value: '100000.50', concept: 'Reintegro colaboradores', description: 'Descripción de prueba', radicate: '12345', payment_order_code: '67890', paymentMethod: 'Nomina', typeAccount: 'De ahorros', account_number: '1234567890', authorName: 'Fernando' |

### ExteriorPaymentFormViewTests

| Nombre | Clase                        | Etapa                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------ | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| setUp3 | ExteriorPaymentFormViewTests | beneficiary_name: 'Daniela', beneficiary_last_name: 'Londoño', beneficiary_document_type: 'DNI', beneficiary_document_no: '12345678', passport_number: 'ABC123456', passport_expedition_city: 'Cali', address: 'calle 25', bank_name: 'Bancolombia', account_type: 'Ahorros', swift_code: 'BOFAUS3N', iban_aba_code_type: 'IBAN', iban_aba_code: '01010101', account_name: 'Daniela Londoño', account_number: '1234567890', bank_address: 'calle 32' |

### Objetivo de los Tests de Vistas

El objetivo de estos tests es verificar el correcto funcionamiento de las vistas asociadas a los formularios de cuenta de cobro, requisición y pago al exterior, asegurando que los formularios se rendericen correctamente en una solicitud GET y que los datos enviados a través de una solicitud POST sean procesados correctamente.

### Casos de Prueba de Vistas

| Clase                        | Método         | Etapa  | Valores de Entrada | Resultado Esperado                                                 |
| ---------------------------- | -------------- | ------ | ------------------ | ------------------------------------------------------------------ |
| ChargeAccountFormViewTests   | test_get_form  | setUp1 | -                  | El formulario debe renderizarse correctamente en una solicitud GET |
| ChargeAccountFormViewTests   | test_post_form | setUp1 | Datos válidos      | El formulario debe procesarse correctamente en una solicitud POST  |
| RequisitionFormViewTests     | test_get_form  | setUp2 | -                  | El formulario debe renderizarse correctamente en una solicitud GET |
| RequisitionFormViewTests     | test_post_form | setUp2 | Datos válidos      | El formulario debe procesarse correctamente en una solicitud POST  |
| ExteriorPaymentFormViewTests | test_get_form  | setUp3 | -                  | El formulario debe renderizarse correctamente en una solicitud GET |
| ExteriorPaymentFormViewTests | test_post_form | setUp3 | Datos válidos      | El formulario debe procesarse correctamente en una solicitud POST  |