## Configuration of Scenarios
## LoginFormTest

| Name  | Class           | Stage                                                                                                                                                                                                                       |
| ------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| setUp1  | LoginFormTest   | Test the login form with valid data. Verifies that the login form is valid when provided with valid data.                                                                                                                  |
| setUp2  | LoginFormTest   | Test the login form with invalid data. Verifies that the login form is invalid when provided with empty data.                                                                                                               |



## CustomUserCreationFormTest

| Name  | Class                    | Stage                                                                                                                                                                                                                                     |
| ------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| setUp1  | CustomUserCreationForm   | Test the custom user creation form with valid data. Verifies that the custom user creation form is valid when provided with valid data.                                                                                               |
| setUp2  | CustomUserCreationForm   | Test the custom user creation form with invalid data. Verifies that the custom user creation form is invalid when provided with mismatched passwords or empty data.                                                             |
### Test Objective
The purpose of these tests is to verify the correct operation of the login and custom user creation forms. It ensures that the forms are valid when valid data is entered and invalid when incorrect or incomplete data is provided.
### Test Cases

| Class                    | Method                 | Stage  | input values                           | Expected results                                              |
| ------------------------ | ---------------------- | ------ | -------------------------------------------- | --------------------------------------------------------------- |
| LoginFormTest            | test_login_form_valid  | setUp1 | {'username': 'testuser', 'password': 'testpassword'} | El formulario debe ser válido                                   |
| LoginFormTest            | test_login_form_invalid| setUp2 | {'username': '', 'password': ''}             | El formulario debe ser inválido                                 |
| CustomUserCreationFormTest | test_custom_user_creation_form_valid | setUp1 | {'first_name': 'John', 'last_name': 'Doe', 'email': 'johndoe@example.com', 'password1': 'testpassword', 'password2': 'testpassword'} | El formulario debe ser válido                          |
| CustomUserCreationFormTest | test_custom_user_creation_form_invalid | setUp2 | {'first_name': 'John', 'last_name': 'Doe', 'email': 'johndoe@example.com', 'password1': 'testpassword', 'password2': 'differentpassword'} | El formulario debe ser inválido debido a contraseñas diferentes |
| CustomUserCreationFormTest | test_custom_user_creation_form_invalid | setUp2 | {}                                           | The form must be invalid due to empty data           |

## Configuration of Scenarios

## UserRequestViewsTest

| Name  | Class                | Stage                                          |
| ------- | -------------------- | ---------------------------------------------- |
| setUp1  | UserRequestViewsTest | Set up the test environment for index view     |
| setUp2  | UserRequestViewsTest | Set up the test environment for forgot password view |
| setUp3  | UserRequestViewsTest | Set up the test environment for user login view |
| setUp4  | UserRequestViewsTest | Set up the test environment for registration view |
| setUp5  | UserRequestViewsTest | Set up the test environment for password reset request view |



### Test Objective
The objective of these tests is to verify the correct operation of views related to user management, such as login, password recovery, and user registration. It ensures that these views return an  status code and utilize the correct templates corresponding to each functionality.

### Test Cases

| Class                   | Method                      | Stage      | Input Values                                     | Expected Result                                                     |
| ----------------------- | --------------------------- | ---------- | ------------------------------------------------- | -------------------------------------------------------------------- |
| UserRequestViewsTest    | test_index_view             | setUp1     | -                                               | Returns a status code 200 and uses the template 'registration/login.html' |
| UserRequestViewsTest    | test_forgot_password_view   | setUp2     | -                                               | Returns a status code 200 and uses the template 'registration/password_reset_form.html' |
| UserRequestViewsTest    | test_user_login_view        | setUp3     | -                                               | Returns a status code 200 and uses the template 'registration/login.html' |
| UserRequestViewsTest    | test_registration_view      | setUp4     | -                                               | Returns a status code 200 and uses the template 'registration/registro.html' |
| UserRequestViewsTest    | test_password_reset_request_view | setUp5 | -                                               | Returns a status code 200 and uses the template 'registration/password_reset_form.html' |
| UserRequestViewsTest    | test_successful_user_login  | setUp1     | {'email': 'test@example.com', 'password': 'password'} | Redirects to the index page after a successful login |
| UserRequestViewsTest    | test_successful_password_reset_request | - | {'email': 'test@example.com'}                   | Redirects to 'password_reset_done' after a successful password reset request |