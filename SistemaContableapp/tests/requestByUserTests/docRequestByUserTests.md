## Scenario Configuration

### ChargeAccountFormTests

| Name | Class                  | Stage                                                                                                                                                                                                                                                                                                                                                                    |
| ------ | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| setUp1 | ChargeAccountFormTests | name: 'Pablo', identification: '1234567890', phone: '1234567890', city: 'Bogota', addres: 'Calle 123', date: '2023-04-01', value_letters: 'Cien mil pesos', value_numbers: '100000', concept: 'Concepto de prueba', bank: 'Banco de Prueba', type: 'De ahorros', account_number: '1234567890', cex: '12345', retentions: True, declarant: True, colombian_resident: True |
| setUp2 | ChargeAccountFormTests | name: '', identification: '', phone: '', city: '', addres: '', date: '', value_letters: '', value_numbers: '', concept: '', bank: '', type: '', account_number: '', cex: '', retentions: False, declarant: False, colombian_resident: False                                                                                                                              |

### RequisitionFormTests

| Name | Class                | Stage                                                                                                                                                                                                                                                                                                                                                                                         |
| ------ | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| setUp3 | RequisitionFormTests | date: '2023-04-01', beneficiaryName: 'Pablo', idNumber: '1234567890', charge: 'Developer', dependency: 'IT Department', cenco: '1234', value: '100000.50', concept: 'Reintegro colaboradores', description: 'Descripción de prueba', radicate: '12345', payment_order_code: '67890', paymentMethod: 'Nomina', typeAccount: 'De ahorros', account_number: '1234567890', authorName: 'Fernando' |
| setUp4 | RequisitionFormTests | date: '', beneficiaryName: '', idNumber: '', charge: '', dependency: '', cenco: '', value: '', concept: '', description: '', radicate: '', payment_order_code: '', paymentMethod: '', typeAccount: '', account_number: '', authorName: ''                                                                                                                                                     |

### ExteriorPaymentFormTests

| Name | Class                    | Stage                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------ | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| setUp5 | ExteriorPaymentFormTests | beneficiary_name: 'Daniela', beneficiary_last_name: 'Londoño', beneficiary_document_type: 'DNI', beneficiary_document_no: '12345678', passport_number: 'ABC123456', passport_expedition_city: 'Cali', address: 'calle 25', bank_name: 'Bancolombia', account_type: 'Ahorros', swift_code: 'BOFAUS3N', iban_aba_code_type: 'IBAN', iban_aba_code: '01010101', account_name: 'Daniela Londoño', account_number: '1234567890', bank_address: 'calle 32' |
| setUp6 | ExteriorPaymentFormTests | beneficiary_name: '', beneficiary_last_name: '', beneficiary_document_type: '', beneficiary_document_no: '', passport_number: '', passport_expedition_city: '', address: 'calle 25', bank_name: 'Bancolombia', account_type: 'Ahorros', swift_code: '111111111111', iban_aba_code_type: 'IBAN', iban_aba_code: '', account_name: 'Daniela Londoño', account_number: '1234567890', bank_address: 'calle 32'                                           |

### Test Objective

The objective of these tests is to verify the correct functioning of the collection, requisition and foreign payment account forms, ensuring that the mandatory fields are correctly validated and that the forms are valid when correct data is entered.

### Test cases

| Class                    | Método                 | Stage  | Valores de Entrada | Expected results                                              |
| ------------------------ | ---------------------- | ------ | ------------------ | --------------------------------------------------------------- |
| ChargeAccountFormTests   | test_valid_form        | setUp1 | Valid data      | Invalid data                                   |
| ChargeAccountFormTests   | test_blank_fields      | setUp2 | empty fields      | The form must be invalid                                 |
| RequisitionFormTests     | test_valid_form        | setUp3 | Valid data      | Invalid data                                   |
| RequisitionFormTests     | test_blank_fields      | setUp4 | empty fields      | The form must be invalid                                 |
| ExteriorPaymentFormTests | test_form_fields       | -      | -                  | Verify that the form contains all the expected fields |
| ExteriorPaymentFormTests | test_form_valid_data   | setUp5 | Valid data      | Invalid data                                   |
| ExteriorPaymentFormTests | test_form_invalid_data | setUp6 | Invalid data    | The form must be invalid                                 |





## Scenario Configuration

### ChargeAccountModelTests

| Name | Class                   | Stage                                                                                                                                                                                                                                                                                                                                                                    |
| ------ | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| setUp1 | ChargeAccountModelTests | name: 'Pablo', identification: '1234567890', phone: '1234567890', city: 'Bogota', addres: 'Calle 123', date: '2023-04-01', value_letters: 'Cien mil pesos', value_numbers: '100000', concept: 'Concepto de prueba', bank: 'Banco de Prueba', type: 'De ahorros', account_number: '1234567890', cex: '12345', retentions: True, declarant: True, colombian_resident: True |

### RequisitionModelTests

| Name | Class                 | Stage                                                                                                                                                                                                                                                                                                                                                                                         |
| ------ | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| setUp2 | RequisitionModelTests | date: '2023-04-01', beneficiaryName: 'Pablo', idNumber: '1234567890', charge: 'Developer', dependency: 'IT Department', cenco: '1234', value: '100000.50', concept: 'Reintegro colaboradores', description: 'Descripción de prueba', radicate: '12345', payment_order_code: '67890', paymentMethod: 'Nomina', typeAccount: 'De ahorros', account_number: '1234567890', authorName: 'Fernando' |

### ExteriorPaymentModelTests

| Name | Class                     | Stage                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------ | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| setUp3 | ExteriorPaymentModelTests | beneficiary_name: 'Daniela', beneficiary_last_name: 'Londoño', beneficiary_document_type: 'DNI', beneficiary_document_no: '12345678', passport_number: 'ABC123456', passport_expedition_city: 'Cali', address: 'calle 25', bank_name: 'Bancolombia', account_type: 'Ahorros', swift_code: 'BOFAUS3N', iban_aba_code_type: 'IBAN', iban_aba_code: '01010101', account_name: 'Daniela Londoño', account_number: '1234567890', bank_address: 'calle 32' |

### Test Objective of models

The goal of these tests is to verify that the application models are working correctly, including the creation of instances with valid data, the integrity of the fields, and the selection options (choices) for the corresponding fields.

### Test cases of models

| Class                     | Método                        | Stage  | Expected results                                                                                           |
| ------------------------- | ----------------------------- | ------ | ------------------------------------------------------------------------------------------------------------ |
| ChargeAccountModelTests   | test_create_charge_account    | setUp1 | Create a Charge_account instance with the data proporcionados                                           |
| RequisitionModelTests     | test_create_requisition       | setUp2 | Create a Requisition instance with the provided data                                              |
| ExteriorPaymentModelTests | test_create_exterior_payment  | setUp3 | Create an instance of Exterior_payment with the provided data                                         |
| ExteriorPaymentModelTests | test_exterior_payment_fields  | -      | Verify that the Exterior_payment model has the expected fields                                          |
| ExteriorPaymentModelTests | test_exterior_payment_choices | -      | Verify that the Exterior_payment model has the correct options for account_type and iba_aba_code_type |



## Scenario Configuration

### ChargeAccountFormViewTests

| Name | Class                      | Stage                                                                                                                                                                                                                                                                                                                                                                    |
| ------ | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| setUp1 | ChargeAccountFormViewTests | name: 'Pablo', identification: '1234567890', phone: '1234567890', city: 'Bogota', addres: 'Calle 123', date: '2023-04-01', value_letters: 'Cien mil pesos', value_numbers: '100000', concept: 'Concepto de prueba', bank: 'Banco de Prueba', type: 'De ahorros', account_number: '1234567890', cex: '12345', retentions: True, declarant: True, colombian_resident: True |

### RequisitionFormViewTests

| Name | Class                    | Stage                                                                                                                                                                                                                                                                                                                                                                                         |
| ------ | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| setUp2 | RequisitionFormViewTests | date: '2023-04-01', beneficiaryName: 'Pablo', idNumber: '1234567890', charge: 'Developer', dependency: 'IT Department', cenco: '1234', value: '100000.50', concept: 'Reintegro colaboradores', description: 'Descripción de prueba', radicate: '12345', payment_order_code: '67890', paymentMethod: 'Nomina', typeAccount: 'De ahorros', account_number: '1234567890', authorName: 'Fernando' |

### ExteriorPaymentFormViewTests

| Name | Class                        | Stage                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------ | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| setUp3 | ExteriorPaymentFormViewTests | beneficiary_name: 'Daniela', beneficiary_last_name: 'Londoño', beneficiary_document_type: 'DNI', beneficiary_document_no: '12345678', passport_number: 'ABC123456', passport_expedition_city: 'Cali', address: 'calle 25', bank_name: 'Bancolombia', account_type: 'Ahorros', swift_code: 'BOFAUS3N', iban_aba_code_type: 'IBAN', iban_aba_code: '01010101', account_name: 'Daniela Londoño', account_number: '1234567890', bank_address: 'calle 32' |

### Test Objective of views

The objective of these tests is to verify the correct functioning of the views associated with the collection, requisition and foreign payment account forms, ensuring that the forms are rendered correctly in a GET request and that the data sent through a POST request are processed correctly.

### Test cases of views

| Class                        | Método         | Stage  | Valores de Entrada | Expected results                                                 |
| ---------------------------- | -------------- | ------ | ------------------ | ------------------------------------------------------------------ |
| ChargeAccountFormViewTests   | test_get_form  | setUp1 | -                  | The form must render correctly in a GET request |
| ChargeAccountFormViewTests   | test_post_form | setUp1 | Valid data      | The form must be processed successfully in a POST request |
| RequisitionFormViewTests     | test_get_form  | setUp2 | -                  | The form must render correctly in a GET request |
| RequisitionFormViewTests     | test_post_form | setUp2 | Valid data      | The form must be processed successfully in a POST request |
| ExteriorPaymentFormViewTests | test_get_form  | setUp3 | -                  | The form must render correctly in a GET request |
| ExteriorPaymentFormViewTests | test_post_form | setUp3 | Valid data      | The form must be processed successfully in a POST request |