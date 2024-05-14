## User Model Tests

### Test Case: UserModelTestCase

#### Method: setUp
- Description: Set up necessary data for the test case.
- Actions:
  - Created two roles: 'Administrador' and 'Solicitante'.
  - Created a user with username 'testuser', email 'test@example.com', name 'Test', and password 'testpassword'.

#### Method: test_user_creation
- Description: Verifies that a new user is created correctly in the database.
- Actions:
  - Asserts that a User object with the username 'testuser' exists.

#### Method: test_user_str_representation
- Description: Verifies the text string representation of the User object.
- Actions:
  - Asserts that converting the User object to a string returns 'Test, None'.

#### Method: test_user_rol_assignment
- Description: Verifies that a role can be correctly assigned to a user.
- Actions:
  - Assigns the 'Administrador' role to the user created in the setup.
  - Asserts that the assigned role is the same.

### Test Case: UserUpdateFormTestCase

#### Method: setUp
- Description: Set up necessary data for the test case.
- Actions:
  - Created a 'Administrador' role.
  - Created a user with username 'testuser', email 'test@example.com', name 'Test', and password 'testpassword'.

#### Method: test_user_update_form_valid
- Description: Verifies that the UserUpdateForm form is valid with correct data.
- Actions:
  - Created a dictionary with valid data.
  - Created an instance of the form with the valid data and the user instance.
  - Asserts that the form is valid.

#### Method: test_user_update_form_invalid
- Description: Verifies that the UserUpdateForm form is invalid with incorrect data.
- Actions:
  - Created a dictionary with invalid data (incorrect email).
  - Created an instance of the form with the invalid data and the user instance.
  - Asserts that the form is invalid.

### Test Case: UserViewTestCase

#### Method: setUp
- Description: Set up necessary data for the test case.
- Actions:
  - Created a client.
  - Created an 'Administrador' role.
  - Created an admin user with username 'admin', email 'admin@example.com', name 'Admin', and password 'adminpassword'.
  - Assigned the 'Administrador' role to the admin user.

#### Method: test_user_list_view
- Description: Verifies that an admin user can access the user list view.
- Actions:
  - Logged in with the admin user.
  - Made a GET request to the 'user_list' view.
  - Asserts that the HTTP status code is 200 (OK).
  - Asserts that the 'user_list.html' template is used.

#### Method: test_edit_user_view_get
- Description: Verifies that an admin user can access a particular user's edit view.
- Actions:
  - Logged in with the admin user.
  - Mocked a GET request to the 'edit_user' view.
  - Asserts that the HTTP status code is 200 (OK).
  - Asserts that the 'update_user.html' template is used.

#### Method: test_edit_user_view_post
- Description: Verifies that an admin user can update data for a particular user.
- Actions:
  - Logged in with the admin user.
  - Mocked a POST request to the 'edit_user' view with valid form data.
  - Asserts that it is redirected to the 'user_list' view.

#### Method: test_delete_user_view_get
- Description: Verifies that an admin user can access the confirmation view to delete a particular user.
- Actions:
  - Logged in with the admin user.
  - Mocked a GET request to the 'delete_user' view.
  - Asserts that the HTTP status code is 200 (OK).
  - Asserts that the 'confirm_delete_user.html' template is used.

#### Method: test_delete_user_view_post
- Description: Verifies that an admin user can delete a particular user.
- Actions:
  - Logged in with the admin user.
  - Simulated a POST request to the 'delete_user' view.
  - Asserts that an HTTP status code 302 (redirect) is obtained.
  - Asserts that the User object corresponding to the admin user no longer exists in the database.

## Update User Permission Tests

### Test Case: updateUserPermissionTestCase

#### Method: setUp
- Description: Set up necessary data for the test case.
- Actions:
  - Created roles: 'Administrador' and 'Solicitante'.
  - Created admin and applicant users with respective roles.

#### Method: test_user_list_allowed
- Description: Tests if an 'Administrador' user has permission to access the 'user_list' view.
- Actions:
  - Logged in with the admin user.
  - Made a GET request to the 'user_list' view.
  - Asserts that the HTTP status code is 200 (OK).

#### Method: test_user_list_not_allowed
- Description: Tests if a 'Solicitante' user does not have permission to access the 'user_list' view.
- Actions:
  - Logged in with the applicant user.
  - Made a GET request to the 'user_list' view.
  - Asserts that the HTTP status code is 302 (Redirection).

#### Method: test_edit_user_allowed
- Description: Tests if an 'Administrador' user has permission to access the 'edit_user' view.
- Actions:
  - Logged in with the admin user.
  - Mocked a GET request to the 'edit_user' view.
  - Asserts that the HTTP status code is 200 (OK).

#### Method: test_edit_user_not_allowed
- Description: Tests if a 'Solicitante' user does not have permission to access the 'edit_user' view.
- Actions:
  - Logged in with the applicant user.
  - Mocked a GET request to the 'edit_user' view.
  - Asserts that the HTTP status code is 302 (Redirection).

#### Method: test_delete_user_allowed
- Description: Tests if an 'Administrador' user has permission to access the 'delete_user' view.
- Actions:
  - Logged in with the admin user.
  - Mocked a GET request to the 'delete_user' view.
  - Asserts that the HTTP status code is 200 (OK).

#### Method: test_delete_user_not_allowed
- Description: Tests if a 'Solicitante' user does not have permission to access the 'delete_user' view.
- Actions:
  - Logged in with the applicant user.
  - Mocked a GET request to the 'delete_user' view.
  - Asserts that the HTTP status code is 302 (Redirection).

## Tests unitarios totales

### user model:
#### Total: 3 tests

### user update:  
#### Total: 2 tests

### user views:
#### Total: 5 tests

### update User Permission:
#### Total: 5 tests


### Total Final: 15 tests

## Update User Permission E2E Tests

### Test Case: updateUserPermissionTests

#### Method: setUp
- Description: Set up the test environment before running the tests.
- Actions:
  1. Initialize the web browser (Chrome).
  2. Set up the initial data.

#### Method: tearDown
- Description: Clean up the test environment after running the tests.
- Actions:
  1. Close the web browser.

#### Method: type_text
- Description: Simulate typing text into an input field.

#### Method: setup_data
- Description: Set up the initial data required for the tests.

#### Method: setup_roles
- Description: Create the roles in the database if they don't exist.

#### Method: register_user
- Description: Simulate the registration of a new user in the application.
- Actions:
  1. Open the registration page.
  2. Fill in the registration form with provided user data.
  3. Submit the registration form.
  4. Verify successful registration.

#### Method: login
- Description: Log in as a user with the specified credentials.
- Actions:
  1. Open the login page.
  2. Fill in the login form with provided credentials.
  3. Submit the login form.

#### Method: test_admin_can_access_user_list
- Description: Test that an 'Administrador' user can access the 'user_list' view.
- Actions:
  1. Register an 'Administrador' user.
  2. Log in as the 'Administrador' user.
  3. Access the 'user_list' view.
  4. Verify the correct page is displayed.

#### Method: test_lider_cannot_access_user_list
- Description: Test that a 'Lider' user cannot access the 'user_list' view.
- Actions:
  1. Register a 'Lider' user.
  2. Log in as the 'Lider' user.
  3. Attempt to access the 'user_list' view.
  4. Verify the appropriate error message is displayed.


## Tests E2E totales: 
### 2 tests E2E