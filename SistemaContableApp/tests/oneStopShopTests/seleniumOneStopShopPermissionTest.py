import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from SistemaContableApp.models import Rol, User, State
from selenium.webdriver.common.by import By
from mixer.backend.django import mixer
from selenium import webdriver
import time
from unittest import skipUnless
from django.conf import settings
from SistemaContableApp.models import  *
from SistemaContableApp.views import  *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class OneStopShopPermissionTestCase(StaticLiveServerTestCase):
    def setUp(self):
        """
        Set up the test environment before running the tests.

        Initializes the web browser (Chrome) and sets up the initial data
        by calling the setup_data() method.
        """
       
        self.browser = webdriver.Chrome()  # O el navegador que prefieras
        self.browser.implicitly_wait(10)
        self.setup_data()

    def tearDown(self):
        """
        Clean up the test environment after running the tests.

        Closes the web browser.
        """
       
        self.browser.quit()

    def type_text(self, element, text):
        """
        Simulate typing text into an input field.

        Args:
            element (WebElement): The DOM element where the text will be typed.
            text (str): The text to be typed into the input field.

        Sends each character of the text to the element with a small delay to avoid
        synchronization issues.
        """
       
        for char in text:
            element.send_keys(char)
            time.sleep(0.02)  # Espera 0.2 segundos después de cada tecla

    def setup_data(self):
        """
        Set up the initial data required for the tests.

        Creates the roles in the database if they don't exist.
        """
       
        self.setup_roles()
        self.setup_state()

    def setup_state(self):
        """
        Create the "Enviado" state in the database if it doesn't exist.
        """
        if not State.objects.filter(state="En revisión").exists():
            mixer.blend(State, state="En revisión", color="#FFFFFF")
        if not State.objects.filter(state="Revisado").exists():
            mixer.blend(State, state="Revisado", color="#FFFFFF")

    def setup_roles(self):
        """
        Create the roles in the database if they don't exist.

        Utilizes the mixer library to create instances of the roles.
        """
       
        # Crea los roles si no existen
        if not Rol.objects.filter(rol="Administrador").exists():
            mixer.blend(Rol, rol="Administrador")
        if not Rol.objects.filter(rol="Líder").exists():
            mixer.blend(Rol, rol="Líder")
        if not Rol.objects.filter(rol="Gestor").exists():
            mixer.blend(Rol, rol="Gestor")
        if not Rol.objects.filter(rol="Ventanilla única").exists():
            mixer.blend(Rol, rol="Ventanilla única")
        if not Rol.objects.filter(rol="Contable").exists():
            mixer.blend(Rol, rol="Contable")
        if not Rol.objects.filter(rol="Solicitante").exists():
            mixer.blend(Rol, rol="Solicitante")

    def register_user(self, name, last_name, email, rol, password):
        """
        Simulate the registration of a new user in the application.

        Args:
            name (str): The user's first name.
            last_name (str): The user's last name.
            email (str): The user's email address.
            rol (str): The user's role.
            password (str): The user's password.

        Navigates to the registration form, fills in the fields, and verifies that
        the registration was successful.
        """
       
        # Abre la página de registro
        self.browser.get(self.live_server_url + '/registro/')

        # Encuentra los campos del formulario de registro
        name_input = self.browser.find_element(By.ID, 'id_name')
        last_name_input = self.browser.find_element(By.ID, 'id_last_name')
        email_input = self.browser.find_element(By.ID, 'id_email')
        rol_select = self.browser.find_element(By.ID, 'id_rol')
        password1_input = self.browser.find_element(By.ID, 'id_password1')
        password2_input = self.browser.find_element(By.ID, 'id_password2')

        # Llena el formulario con los datos proporcionados
        self.type_text(name_input, name)
        self.type_text(last_name_input, last_name)
        self.type_text(email_input, email)
        rol_select.send_keys(rol)
        self.type_text(password1_input, password)
        self.type_text(password2_input, password)

        # Envía el formulario de registro
        submit_button = self.browser.find_element(By.CSS_SELECTOR, '.btn')
        submit_button.click()

        # Espera un poco para que la página se actualice
        time.sleep(3)

        # Verifica si se ha registrado correctamente
        self.assertIn('Tu cuenta ha sido creada exitosamente.', self.browser.page_source)
        self.assertIn('Registro exitoso.', self.browser.page_source)

    def login(self, email, password):
        """
        Log in as a user with the specified credentials.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.
            role (str, optional): The role of the user. If provided, the function
                will check that the user has the specified role.

        Navigates to the login page, fills in the fields with the provided
        credentials, and verifies that the login was successful. If a role is
        provided, it also checks that the user has the specified role.
        """
        # Abre la página de inicio de sesión
        self.browser.get(self.live_server_url)

        # Encuentra los campos del formulario de inicio de sesión
        email_input = self.browser.find_element(By.NAME, 'email')
        password_input = self.browser.find_element(By.NAME, 'password')

        # Llena el formulario con los datos de inicio de sesión
        self.type_text(email_input, email)
        self.type_text(password_input, password)

        # Envía el formulario de inicio de sesión
        submit_button = self.browser.find_element(By.CSS_SELECTOR, '.btn')
        submit_button.click()

        # Espera un poco para que la página se actualice
        time.sleep(5)

    def test_admin_can_access_summary_one_stop_shop_view(self):
        """
        Test that a user with the 'admin' role can access the 'summaryOneStopShopView' view.
        """
        # Registrar un usuario con el rol 'Administrador'
        self.register_user("Juan", "Pérez", "juan.perez@example.com", "Administrador", "micontraseña")

        # Iniciar sesión como el usuario 'Administrador'
        self.login("juan.perez@example.com", "micontraseña")

        # Acceder a la vista 'summaryOneStopShopView'
        self.browser.get(self.live_server_url + '/Ventanilla única resumida/')

        # Verificar que se muestra el título
        title_element = self.browser.find_element(By.CSS_SELECTOR, '.heading')
        self.assertEqual(title_element.text, 'Ventanilla unica resumida')

    def test_lider_can_access_summary_one_stop_shop_view(self):
        """
        Test that a user with the 'Líder' role can access the 'summaryOneStopShopView' view.
        """
        # Registrar un usuario con el rol 'Líder'
        self.register_user("Juan", "Pérez", "juan.perez@example.com", "Líder", "micontraseña")

        # Iniciar sesión como el usuario 'Líder'
        self.login("juan.perez@example.com", "micontraseña")

        # Acceder a la vista 'summaryOneStopShopView'
        self.browser.get(self.live_server_url + '/Ventanilla única resumida/')

        # Verificar que se muestra el título
        title_element = self.browser.find_element(By.CSS_SELECTOR, '.heading')
        self.assertEqual(title_element.text, 'Ventanilla unica resumida')

    def test_gestor_can_access_summary_one_stop_shop_view(self):
        """
        Test that a user with the 'Gestor' role can access the 'summaryOneStopShopView' view.
        """
        # Registrar un usuario con el rol 'Gestor'
        self.register_user("Juan", "Pérez", "juan.perez@example.com", "Gestor", "micontraseña")

        # Iniciar sesión como el usuario 'Gestor'
        self.login("juan.perez@example.com", "micontraseña")

        # Acceder a la vista 'summaryOneStopShopView'
        self.browser.get(self.live_server_url + '/Ventanilla única resumida/')

        # Verificar que se muestra el título
        title_element = self.browser.find_element(By.CSS_SELECTOR, '.heading')
        self.assertEqual(title_element.text, 'Ventanilla unica resumida')

    def test_solicitante_cannot_access_summary_one_stop_shop_view(self):
        """
        Test that a user with the 'Solicitante' role cannot access the 'summaryOneStopShopView' view
        and the appropriate error message is displayed.
        """
        # Registrar un usuario con el rol 'Solicitante'
        self.register_user("Juan", "Pérez", "juan.perez@example.com", "Solicitante", "micontraseña")

        # Iniciar sesión como el usuario 'Solicitante'
        self.login("juan.perez@example.com", "micontraseña")

        # Intentar acceder a la vista
        self.browser.get(self.live_server_url + '/Ventanilla única resumida/')

        # Verificar que se muestra el mensaje de error
        error_modal = self.browser.find_element(By.ID, 'error-modal')
        self.assertTrue(error_modal.is_displayed())

        error_message = error_modal.find_element(By.TAG_NAME, 'p').text
        self.assertEqual(error_message, 'No tienes los permisos requeridos')

    def test_gestor_can_access_full_one_stop_shop_view(self):
        """
        Test that a user with the 'Gestor' role can access the 'fullOneStopShopView' view.
        """
        # Registrar un usuario con el rol 'Gestor'
        self.register_user("Juan", "Pérez", "juan.perez@example.com", "Gestor", "micontraseña")

        # Iniciar sesión como el usuario 'Gestor'
        self.login("juan.perez@example.com", "micontraseña")

        # Acceder a la vista 'fullOneStopShopView'
        self.browser.get(self.live_server_url + '/Ventanilla_unica/')

        # Verificar que se muestra el título
        title_element = self.browser.find_element(By.CSS_SELECTOR, '.heading')
        self.assertEqual(title_element.text, 'Centro compartido de servicios')

    def test_admin_can_access_full_one_stop_shop_view(self):
        """
        Test that a user with the 'Administrador' role can access the 'fullOneStopShopView' view.
        """
        # Registrar un usuario con el rol 'Administrador'
        self.register_user("Juan", "Pérez", "juan.perez@example.com", "Administrador", "micontraseña")

        # Iniciar sesión como el usuario 'Administrador'
        self.login("juan.perez@example.com", "micontraseña")

        # Acceder a la vista 'fullOneStopShopView'
        self.browser.get(self.live_server_url + '/Ventanilla_unica/')

        # Verificar que se muestra el título
        title_element = self.browser.find_element(By.CSS_SELECTOR, '.heading')
        self.assertEqual(title_element.text, 'Centro compartido de servicios')

    def test_solicitante_cannot_access_full_one_stop_shop_view(self):
        """
        Test that a user with the 'Solicitante' role cannot access the 'fullOneStopShopView' view
        and the appropriate error message is displayed.
        """
        # Registrar un usuario con el rol 'Solicitante'
        self.register_user("Juan", "Pérez", "juan.perez@example.com", "Solicitante", "micontraseña")

        # Iniciar sesión como el usuario 'Solicitante'
        self.login("juan.perez@example.com", "micontraseña")

        # Intentar acceder a la vista
        self.browser.get(self.live_server_url + '/Ventanilla_unica/')

        # Verificar que se muestra el mensaje de error
        error_modal = self.browser.find_element(By.ID, 'error-modal')
        self.assertTrue(error_modal.is_displayed())

        error_message = error_modal.find_element(By.TAG_NAME, 'p').text
        self.assertEqual(error_message, 'No tienes los permisos requeridos')

    def test_ventanilla_can_access_one_stop_shop_form_view(self):
        """
        Test that a user with the 'Ventanilla única' role can access the 'oneStopShopFormView' view.
        """
        # Registrar un usuario con el rol 'Ventanilla única'
        self.register_user("Juan", "Pérez", "juan.perez@example.com", "Ventanilla única", "micontraseña")

        # Iniciar sesión como el usuario 'Ventanilla única'
        self.login("juan.perez@example.com", "micontraseña")

        # Acceder a la vista 'oneStopShopFormView'
        self.browser.get(self.live_server_url + '/Agregar a ventanilla única/')

        # Verificar que se muestra el título
        title_element = self.browser.find_element(By.CSS_SELECTOR, '.heading')
        self.assertEqual(title_element.text, 'Agregar a Ventanilla única')

    def test_admin_cannot_access_access_one_stop_shop_form_view(self):
        """
        Test that a user with the 'Administrador' role cannot access the 'oneStopShopFormView' view
        and the appropriate error message is displayed.
        """
        # Registrar un usuario con el rol 'Administrador'
        self.register_user("Juan", "Pérez", "juan.perez@example.com", "Administrador", "micontraseña")

        # Iniciar sesión como el usuario 'Administrador'
        self.login("juan.perez@example.com", "micontraseña")

        # Intentar acceder a la vista
        self.browser.get(self.live_server_url + '/Agregar a ventanilla única/')

        # Verificar que se muestra el mensaje de error
        error_modal = self.browser.find_element(By.ID, 'error-modal')
        self.assertTrue(error_modal.is_displayed())

        error_message = error_modal.find_element(By.TAG_NAME, 'p').text
        self.assertEqual(error_message, 'No tienes los permisos requeridos')

    def test_lider_cannot_access_access_one_stop_shop_form_view(self):
        """
        Test that a user with the 'Lider' role cannot access the 'oneStopShopFormView' view
        and the appropriate error message is displayed.
        """
        # Registrar un usuario con el rol 'Lider'
        self.register_user("Juan", "Pérez", "juan.perez@example.com", "Líder", "micontraseña")

        # Iniciar sesión como el usuario 'Lider'
        self.login("juan.perez@example.com", "micontraseña")

        # Intentar acceder a la vista
        self.browser.get(self.live_server_url + '/Agregar a ventanilla única/')

        # Verificar que se muestra el mensaje de error
        error_modal = self.browser.find_element(By.ID, 'error-modal')
        self.assertTrue(error_modal.is_displayed())

        error_message = error_modal.find_element(By.TAG_NAME, 'p').text
        self.assertEqual(error_message, 'No tienes los permisos requeridos')

    def test_gestor_cannot_access_access_one_stop_shop_form_view(self):
        """
        Test that a user with the 'Gestor' role cannot access the 'oneStopShopFormView' view
        and the appropriate error message is displayed.
        """
        # Registrar un usuario con el rol 'Gestor'
        self.register_user("Juan", "Pérez", "juan.perez@example.com", "Gestor", "micontraseña")

        # Iniciar sesión como el usuario 'Gestor'
        self.login("juan.perez@example.com", "micontraseña")

        # Intentar acceder a la vista
        self.browser.get(self.live_server_url + '/Agregar a ventanilla única/')

        # Verificar que se muestra el mensaje de error
        error_modal = self.browser.find_element(By.ID, 'error-modal')
        self.assertTrue(error_modal.is_displayed())

        error_message = error_modal.find_element(By.TAG_NAME, 'p').text
        self.assertEqual(error_message, 'No tienes los permisos requeridos')

    

    def test_update_state_allowed_users(self):
        """
        tests that the Administrador or Gestor user can update the status correctly
        """
        # Registrar un usuario con permisos
        self.register_user("Juan", "Pérez", "usuario@example.com", "Administrador", "micontraseña")

        # Crear un nuevo objeto Following
        following = Following.objects.create(
            creationDate='2023-04-01',
            creator='Daniela',
            type='Solicitud',
            supplier='Acme Inc.',
            supplierId='12345',
            documentNumber='DOC001',
            manager='Jane Smith',
            concept='Compra de suministros',
            moneyType='USD',
            amount=1000,
            cenco='CENCO1',
            cexNumber='CEX001',
            observations='Ninguna',
            currentState=State.objects.get(state="En revisión"),
            closeDate='2023-04-30',
        )

        # Iniciar sesión como el usuario
        self.login("usuario@example.com", "micontraseña")

        # Intentar acceder a la vista
        self.browser.get(self.live_server_url + '/Ventanilla_unica/')

        edit_button = self.browser.find_element(By.CSS_SELECTOR, 'button.edit-btn')
        edit_button.click()
            
        # Cambiar el estado
        wait = WebDriverWait(self.browser, 10)
        new_state = "Revisado"
        popup = wait.until(EC.visibility_of_element_located((By.ID, f'popup_{following.id}')))
        estado_select = popup.find_element(By.ID, f'state_{following.id}')
        select_state = Select(estado_select)
        select_state.select_by_visible_text(new_state)
        # Encontrar el elemento de texto para la descripción
        description_textarea = popup.find_element(By.ID, f'description_{following.id}')

        # Ingresar una descripción para el cambio de estado
        description_textarea.send_keys('Descripción del cambio de estado')
        # Enviar el formulario
        self.browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        
        # Verificar que el estado se haya actualizado correctamente
        updated_following = Following.objects.get(id=following.id)
        self.assertEqual(updated_following.currentState.state, new_state)

    def test_update_state_not_allowed_users(self):
        """
        Test que los usuarios sin el rol 'Administrador' o 'Gestor'
        no pueden actualizar el estado de un following.
        """
        # Registrar un usuario sin permisos
        self.register_user("Juan", "Pérez", "usuario@example.com", "Ventanilla única", "micontraseña")

        # Crear un nuevo objeto Following
        following = Following.objects.create(
            creationDate='2023-04-01',
            creator='Daniela',
            type='Solicitud',
            supplier='Acme Inc.',
            supplierId='12345',
            documentNumber='DOC001',
            manager='Jane Smith',
            concept='Compra de suministros',
            moneyType='USD',
            amount=1000,
            cenco='CENCO1',
            cexNumber='CEX001',
            observations='Ninguna',
            currentState=State.objects.get(state="En revisión"),
            closeDate='2023-04-30',
        )

        # Iniciar sesión como el usuario sin permisos
        self.login("usuario@example.com", "micontraseña")

        # Intentar acceder a la vista
        self.browser.get(self.live_server_url + '/Ventanilla_unica/')

        edit_button = self.browser.find_element(By.CSS_SELECTOR, 'button.edit-btn')
        edit_button.click()
            
        # Cambiar el estado
        wait = WebDriverWait(self.browser, 10)
        new_state = "Revisado"
        popup = wait.until(EC.visibility_of_element_located((By.ID, f'popup_{following.id}')))
        estado_select = popup.find_element(By.ID, f'state_{following.id}')
        select_state = Select(estado_select)
        select_state.select_by_visible_text(new_state)
        # Encontrar el elemento de texto para la descripción
        description_textarea = popup.find_element(By.ID, f'description_{following.id}')

        # Ingresar una descripción para el cambio de estado
        description_textarea.send_keys('Descripción del cambio de estado')
        # Enviar el formulario
        self.browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

         # Verificar que se muestra el mensaje de error
        error_modal = self.browser.find_element(By.ID, 'error-modal')
        self.assertTrue(error_modal.is_displayed())

        error_message = error_modal.find_element(By.TAG_NAME, 'p').text
        self.assertEqual(error_message, 'No tienes los permisos requeridos')

        # Verificar que el estado del following no haya cambiado
        updated_following = Following.objects.get(id=following.id)
        self.assertEqual(updated_following.currentState.state, "En revisión")



    def test_approval_comment_not_allowed_user(self):
        """
        Test que un usuario sin el rol 'Administrador' o 'Gestor' no puede agregar un comentario de aprobación.
        """
        # Registrar un usuario sin permisos
        self.register_user("Juan", "Pérez", "usuario@example.com", "Líder", "micontraseña")

        # Crear un nuevo objeto Following
        following = Following.objects.create(
            creationDate='2023-04-01',
            creator='Daniela',
            type='Solicitud',
            supplier='Acme Inc.',
            supplierId='12345',
            documentNumber='DOC001',
            manager='Jane Smith',
            concept='Compra de suministros',
            moneyType='USD',
            amount=1000,
            cenco='CENCO1',
            cexNumber='CEX001',
            observations='Ninguna',
            currentState=State.objects.get(state="En revisión"),
            closeDate='2023-04-30',
        )

        # Iniciar sesión como el usuario sin permisos
        self.login("usuario@example.com", "micontraseña")

        # Acceder a la vista de comentario de aprobación
        self.browser.get(self.live_server_url + '/Ventanilla_unica/')

         # Abrir el modal de comentario de aprobación
        comment_button = self.browser.find_element(By.CSS_SELECTOR, f'button[onclick="openCommentModal(\'{following.id}\', \'approval\')"]')
        comment_button.click()

        # Esperar a que el modal se abra
        wait = WebDriverWait(self.browser, 10)
        popup = wait.until(EC.visibility_of_element_located((By.ID, f'commentModal_approval_{following.id}')))

        # Ingresar un comentario de aprobación
        approval_comment_textarea = popup.find_element(By.ID, f'approval_state_{following.id}')
        approval_comment_textarea.send_keys('Comentario de aprobación')

        # Enviar el formulario
        popup.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        # Verificar que se muestra el mensaje de error
        error_modal = self.browser.find_element(By.ID, 'error-modal')
        self.assertTrue(error_modal.is_displayed())

        error_message = error_modal.find_element(By.TAG_NAME, 'p').text
        self.assertEqual(error_message, 'No tienes los permisos requeridos')
        
        # Verificar que el comentario de aprobación no haya cambiado
        updated_following = Following.objects.get(id=following.id)
        self.assertIsNone(updated_following.approvalComments)


    def test_acceptance_state_not_allowed_user(self):
        """
        Test que un usuario sin el rol 'Administrador' o 'Gestor' no puede editar el estado de aceptación.
        """
        # Registrar un usuario sin permisos
        self.register_user("Juan", "Pérez", "usuario@example.com", "Líder", "micontraseña")

        # Crear un nuevo objeto Following
        following = Following.objects.create(
            creationDate='2023-04-01',
            creator='Daniela',
            type='Solicitud',
            supplier='Acme Inc.',
            supplierId='12345',
            documentNumber='DOC001',
            manager='Jane Smith',
            concept='Compra de suministros',
            moneyType='USD',
            amount=1000,
            cenco='CENCO1',
            cexNumber='CEX001',
            observations='Ninguna',
            currentState=State.objects.get(state="En revisión"),
            closeDate='2023-04-30',
        )

        # Iniciar sesión como el usuario sin permisos
        self.login("usuario@example.com", "micontraseña")
        # Acceder a la vista de comentario de aprobación
        self.browser.get(self.live_server_url + '/Ventanilla_unica/')

        # Abrir el modal de comentario de aprobación
        comment_button = self.browser.find_element(By.CSS_SELECTOR, f'button[onclick="openCommentModal(\'{following.id}\', \'accounting\')"]')
        comment_button.click()

        # Esperar a que el modal se abra
        wait = WebDriverWait(self.browser, 10)
        popup = wait.until(EC.visibility_of_element_located((By.ID, f'commentModal_accounting_{following.id}')))

        # Ingresar un comentario de aprobación
        approval_comment_textarea = popup.find_element(By.ID, f'accounting_comment_{following.id}')
        approval_comment_textarea.send_keys('Comentario de aprobación')

        # Enviar el formulario
        popup.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        # Verificar que se muestra el mensaje de error
        error_modal = self.browser.find_element(By.ID, 'error-modal')
        self.assertTrue(error_modal.is_displayed())

        error_message = error_modal.find_element(By.TAG_NAME, 'p').text
        self.assertEqual(error_message, 'No tienes los permisos requeridos')
            
        # Verificar que el comentario de aprobación no haya cambiado
        updated_following = Following.objects.get(id=following.id)
        self.assertIsNone(updated_following.approvalComments)

    def test_acceptance_state_not_allowed_user(self):
        """
        Test que un usuario sin el rol 'Administrador' o 'Gestor' no puede editar el estado de aceptación.
        """
        # Registrar un usuario sin permisos
        self.register_user("Juan", "Pérez", "usuario@example.com", "Líder", "micontraseña")

        # Crear un nuevo objeto Following
        following = Following.objects.create(
            creationDate='2023-04-01',
            creator='Daniela',
            type='Solicitud',
            supplier='Acme Inc.',
            supplierId='12345',
            documentNumber='DOC001',
            manager='Jane Smith',
            concept='Compra de suministros',
            moneyType='USD',
            amount=1000,
            cenco='CENCO1',
            cexNumber='CEX001',
            observations='Ninguna',
            currentState=State.objects.get(state="En revisión"),
            closeDate='2023-04-30',
        )

        # Iniciar sesión como el usuario sin permisos
        self.login("usuario@example.com", "micontraseña")

        # Acceder a la vista de comentario de aceptación
        self.browser.get(self.live_server_url + '/Ventanilla_unica/')

        # Abrir el modal de comentario de aceptación
        comment_button = self.browser.find_element(By.CSS_SELECTOR, f'button[onclick="openCommentModal(\'{following.id}\', \'acceptance\')"]')
        comment_button.click()

        # Esperar a que el modal se abra
        wait = WebDriverWait(self.browser, 10)
        popup = wait.until(EC.visibility_of_element_located((By.ID, f'commentModal_acceptance_{following.id}')))

        # Ingresar un comentario de aceptación
        acceptance_state_textarea = popup.find_element(By.ID, f'acceptance_state_{following.id}')
        acceptance_state_textarea.send_keys('Estado de aceptación actualizado')

        # Enviar el formulario
        popup.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        # Verificar que se muestra el mensaje de error
        error_modal = self.browser.find_element(By.ID, 'error-modal')
        self.assertTrue(error_modal.is_displayed())

        error_message = error_modal.find_element(By.TAG_NAME, 'p').text
        self.assertEqual(error_message, 'No tienes los permisos requeridos')
      
        # Verificar que el estado de aceptación no haya cambiado
        updated_following = Following.objects.get(id=following.id)
        self.assertIsNone(updated_following.acceptanceState)


    def test_revision_state_not_allowed_user(self):
        """
        Test que un usuario sin el rol 'Administrador' o 'Gestor' no puede editar el estado de revisión.
        """
        # Registrar un usuario sin permisos
        self.register_user("Juan", "Pérez", "usuario@example.com", "Líder", "micontraseña")

        # Crear un nuevo objeto Following
        following = Following.objects.create(
            creationDate='2023-04-01',
            creator='Daniela',
            type='Solicitud',
            supplier='Acme Inc.',
            supplierId='12345',
            documentNumber='DOC001',
            manager='Jane Smith',
            concept='Compra de suministros',
            moneyType='USD',
            amount=1000,
            cenco='CENCO1',
            cexNumber='CEX001',
            observations='Ninguna',
            currentState=State.objects.get(state="En revisión"),
            closeDate='2023-04-30',
        )

        # Iniciar sesión como el usuario sin permisos
        self.login("usuario@example.com", "micontraseña")

        # Acceder a la vista de comentario de aceptación
        self.browser.get(self.live_server_url + '/Ventanilla_unica/')

        # Abrir el modal de comentario de aceptación
        comment_button = self.browser.find_element(By.CSS_SELECTOR, f'button[onclick="openCommentModal(\'{following.id}\', \'revision\')"]')
        comment_button.click()

        # Esperar a que el modal se abra
        wait = WebDriverWait(self.browser, 10)
        popup = wait.until(EC.visibility_of_element_located((By.ID, f'commentModal_revision_{following.id}')))

        # Ingresar un comentario de aceptación
        acceptance_state_textarea = popup.find_element(By.ID, f'revision_state_{following.id}')
        acceptance_state_textarea.send_keys('Estado de aceptación actualizado')

        # Enviar el formulario
        popup.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        # Verificar que se muestra el mensaje de error
        error_modal = self.browser.find_element(By.ID, 'error-modal')
        self.assertTrue(error_modal.is_displayed())

        error_message = error_modal.find_element(By.TAG_NAME, 'p').text
        self.assertEqual(error_message, 'No tienes los permisos requeridos')
      
        # Verificar que el estado de aceptación no haya cambiado
        updated_following = Following.objects.get(id=following.id)
        self.assertIsNone(updated_following.acceptanceState)

    def test_approval_state_not_allowed_user(self):
        """
        Test que un usuario sin el rol 'Administrador' o 'Gestor' no puede editar el estado de aprobación.
        """
        # Registrar un usuario sin permisos
        self.register_user("Juan", "Pérez", "usuario@example.com", "Líder", "micontraseña")

        # Crear un nuevo objeto Following
        following = Following.objects.create(
            creationDate='2023-04-01',
            creator='Daniela',
            type='Solicitud',
            supplier='Acme Inc.',
            supplierId='12345',
            documentNumber='DOC001',
            manager='Jane Smith',
            concept='Compra de suministros',
            moneyType='USD',
            amount=1000,
            cenco='CENCO1',
            cexNumber='CEX001',
            observations='Ninguna',
            currentState=State.objects.get(state="En revisión"),
            closeDate='2023-04-30',
        )

        # Iniciar sesión como el usuario sin permisos
        self.login("usuario@example.com", "micontraseña")

        # Acceder a la vista de edición de estado de aprobación
        self.browser.get(self.live_server_url + '/Ventanilla_unica/')

        # Intentar abrir el modal de comentario de aprobación
        comment_button = self.browser.find_element(By.CSS_SELECTOR, f'button[onclick="openCommentModal(\'{following.id}\', \'approval\')"]')
        comment_button.click()

        # Esperar a que el modal se abra
        wait = WebDriverWait(self.browser, 10)
        popup = wait.until(EC.visibility_of_element_located((By.ID, f'commentModal_approval_{following.id}')))

        # Ingresar un comentario de aceptación
        acceptance_state_textarea = popup.find_element(By.ID, f'approval_state_{following.id}')
        acceptance_state_textarea.send_keys('Estado de aceptación actualizado')

        # Enviar el formulario
        popup.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        # Verificar que se muestra el mensaje de error
        error_modal = self.browser.find_element(By.ID, 'error-modal')
        self.assertTrue(error_modal.is_displayed())

        error_message = error_modal.find_element(By.TAG_NAME, 'p').text
        self.assertEqual(error_message, 'No tienes los permisos requeridos')
      
        # Verificar que el estado de aprobación no haya cambiado
        updated_following = Following.objects.get(id=following.id)
        self.assertIsNone(updated_following.approvalState)