## Descripción de tests unitarios

### GetUsersTest

La clase `GetUsersTest` contiene pruebas para el endpoint de la API de obtener usuarios. Estas pruebas cubren diferentes escenarios para garantizar que el endpoint responda adecuadamente a diversas solicitudes y parámetros.

#### test_get_users_no_exclude_1:

- **Descripción**: Probar la obtención de usuarios sin excluir roles.
- **Resultado esperado**: Se espera una respuesta exitosa con todos los roles incluidos.

#### test_get_users_with_exclude_1:

- **Descripción**: Probar la obtención de usuarios excluyendo ciertos roles.
- **Resultado esperado**: Se espera una respuesta exitosa con los roles excluidos.

#### test_get_users_exception_1:

- **Descripción**: Probar la obtención de usuarios con un parámetro exclude JSON inválido.
- **Resultado esperado**: Se espera una respuesta de error indicando que el parámetro exclude es inválido.

#### test_get_users_empty_request_1:

- **Descripción**: Probar la obtención de usuarios con una solicitud vacía.
- **Resultado esperado**: Se espera una respuesta exitosa con todos los roles incluidos.

#### test_get_users_invalid_exclude_1:

- **Descripción**: Probar la obtención de usuarios con un parámetro exclude inválido.
- **Resultado esperado**: Se espera una respuesta de error indicando que el parámetro exclude es inválido.

#### test_get_users_invalid_method_1:

- **Descripción**: Probar la obtención de usuarios con un método HTTP inválido.
- **Resultado esperado**: Se espera una respuesta de error indicando que el método HTTP es inválido.

#### test_get_users_valid_request_1:

- **Descripción**: Probar la obtención de usuarios con un parámetro exclude válido.
- **Resultado esperado**: Se espera una respuesta exitosa con los roles excluidos.

#### test_get_users_no_exclude:

- **Descripción**: Probar la obtención de usuarios sin excluir ningún rol.
- **Resultado esperado**: Se espera una respuesta exitosa con todos los roles incluidos.

#### test_get_users_with_exclude:

- **Descripción**: Probar la obtención de usuarios excluyendo ciertos roles.
- **Resultado esperado**: Se espera una respuesta exitosa con los roles excluidos.

#### test_get_users_exception:

- **Descripción**: Probar la obtención de usuarios con un parámetro exclude JSON inválido.
- **Resultado esperado**: Se espera una respuesta de error indicando que el parámetro exclude es inválido.

#### test_get_users_empty_request:

- **Descripción**: Probar la obtención de usuarios con una solicitud vacía.
- **Resultado esperado**: Se espera una respuesta exitosa con todos los roles incluidos.

#### test_get_users_invalid_exclude:

- **Descripción**: Probar la obtención de usuarios con un parámetro exclude inválido.
- **Resultado esperado**: Se espera una respuesta de error indicando que el parámetro exclude es inválido.

#### test_get_users_invalid_method:

- **Descripción**: Probar la obtención de usuarios con un método HTTP inválido.
- **Resultado esperado**: Se espera una respuesta de error indicando que el método HTTP es inválido.

#### test_get_users_valid_request:

- **Descripción**: Probar la obtención de usuarios con un parámetro exclude válido.
- **Resultado esperado**: Se espera una respuesta exitosa con los roles excluidos.

#### Descripción de tests unitarios

### UpdateRoleTest

La clase `UpdateRoleTest` contiene pruebas para el endpoint de la API de actualización de roles de usuario. Estas pruebas abarcan diferentes escenarios para garantizar que el endpoint maneje adecuadamente diversas solicitudes y parámetros.

#### setUp

- **Descripción**: Configura el entorno de prueba.
- **Resultado esperado**: Configuración exitosa del cliente de pruebas.

#### Pruebas de actualización de roles

#### test_update_role_empty_request

- **Descripción**: Actualizar el rol de usuario con una solicitud vacía.
- **Resultado esperado**: Se espera una respuesta de error con el código de estado HTTP.

#### test_update_role_invalid_request

- **Descripción**: Actualizar el rol de usuario con parámetros inválidos.
- **Resultado esperado**: Se espera una respuesta de error con el código de estado HTTP.

#### test_update_role_no_post

- **Descripción**: Actualizar el rol de usuario con una solicitud GET.
- **Resultado esperado**: Se espera una respuesta de error con el código de estado HTTP.

#### test_update_role_invalid_following_id

- **Descripción**: Actualizar el rol de usuario con un ID de seguimiento inválido.
- **Resultado esperado**: Se espera una respuesta de error con el código de estado HTTP.

#### test_update_role_invalid_user_id

- **Descripción**: Actualizar el rol de usuario con un ID de usuario inválido.
- **Resultado esperado**: Se espera una respuesta de error con el código de estado HTTP.

#### test_update_role_invalid_role_type

- **Descripción**: Actualizar el rol de usuario con un tipo de rol inválido.
- **Resultado esperado**: Se espera una respuesta de error con el código de estado HTTP.

#### test_update_role_missing_parameters

- **Descripción**: Actualizar el rol de usuario con parámetros faltantes.
- **Resultado esperado**: Se espera una respuesta de error con el código de estado HTTP.

#### test_update_role_invalid_method

- **Descripción**: Actualizar el rol de usuario con un método HTTP inválido.
- **Resultado esperado**: Se espera una respuesta de error con el código de estado HTTP.

#### test_update_role_valid_request

- **Descripción**: Actualizar el rol de usuario con parámetros válidos.
- **Resultado esperado**: Se espera una respuesta exitosa con el código de estado HTTP.

#### test_update_role_empty_request_2

- **Descripción**: Actualizar el rol de usuario con una solicitud vacía.
- **Resultado esperado**: Se espera una respuesta de error con el código de estado HTTP.

#### test_update_role_invalid_request_2

- **Descripción**: Actualizar el rol de usuario con parámetros inválidos.
- **Resultado esperado**: Se espera una respuesta de error con el código de estado HTTP.

#### test_update_role_no_post_2

- **Descripción**: Actualizar el rol de usuario con una solicitud GET.
- **Resultado esperado**: Se espera una respuesta de error con el código de estado HTTP.

#### test_update_role_invalid_following_id_2

- **Descripción**: Actualizar el rol de usuario con un ID de seguimiento inválido.
- **Resultado esperado**: Se espera una respuesta de error con el código de estado HTTP.

#### test_update_role_invalid_user_id_2

- **Descripción**: Actualizar el rol de usuario con un ID de usuario inválido.
- **Resultado esperado**: Se espera una respuesta de error con el código de estado HTTP.

#### test_update_role_invalid_role_type_2

- **Descripción**: Actualizar el rol de usuario con un tipo de rol inválido.
- **Resultado esperado**: Se espera una respuesta de error con el código de estado HTTP.

#### test_update_role_missing_parameters_2

- **Descripción**: Actualizar el rol de usuario con parámetros faltantes.
- **Resultado esperado**: Se espera una respuesta de error con el código de estado HTTP.

#### test_update_role_invalid_method_2

- **Descripción**: Actualizar el rol de usuario con un método HTTP inválido.
- **Resultado esperado**: Se espera una respuesta de error con el código de estado HTTP.

#### test_update_role_valid_request_2

- **Descripción**: Actualizar el rol de usuario con parámetros válidos.
- **Resultado esperado**: Se espera una respuesta exitosa con el código de estado HTTP.

