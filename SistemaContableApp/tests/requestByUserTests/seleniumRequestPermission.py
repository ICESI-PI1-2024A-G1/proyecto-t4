import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from SistemaContableApp.models import Rol, User
from selenium.webdriver.common.by import By
from mixer.backend.django import mixer
from selenium import webdriver
import time
from unittest import skipUnless
from django.conf import settings

class RequestsPermissionTestCase(StaticLiveServerTestCase):

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

    def setup_roles(self):
        """
        Create the roles in the database if they don't exist.

        Utilizes the mixer library to create instances of the roles.
        """
       
        # Crea los roles si no existen
        if not Rol.objects.filter(rol="Rol object (1)").exists():
            mixer.blend(Rol, rol="Administrador")
        if not Rol.objects.filter(rol="Rol object (2)").exists():
            mixer.blend(Rol, rol="Líder")
        if not Rol.objects.filter(rol="Rol object (3)").exists():
            mixer.blend(Rol, rol="Gestor")
        if not Rol.objects.filter(rol="Rol object (4)").exists():
            mixer.blend(Rol, rol="Ventanilla única")
        if not Rol.objects.filter(rol="Rol object (5)").exists():
            mixer.blend(Rol, rol="Contable")
        if not Rol.objects.filter(rol="Rol object (6)").exists():
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

    def test_solicitante_can_access_create_charge_account_form(self):
        """
        Test that a user with the 'Solicitante' role can access the 'createChargeAccountForm' view.
        """
        # Registrar un usuario con el rol 'Solicitante'
        self.register_user("Juan", "Pérez", "juan.perez@example.com", "Rol object (6)", "micontraseña")

        # Iniciar sesión como el usuario 'Solicitante'
        self.login("juan.perez@example.com", "micontraseña")

        # Acceder a la vista 'createChargeAccountForm'
        self.browser.get(self.live_server_url + '/chargeAccountForm/')

        # Verificar que se muestra el título de la solicitud
        title_element = self.browser.find_element(By.CSS_SELECTOR, '.title')
        self.assertEqual(title_element.text, 'Formulario de Cuenta de cobro')

    def test_admin_can_access_create_charge_account_form(self):
        """
        Test that a user with the 'Administrador' role can access the 'createChargeAccountForm' view.
        """
        # Registrar un usuario con el rol 'Administrador'
        self.register_user("Juan", "Pérez", "juan.perez@example.com", "Rol object (1)", "micontraseña")

        # Iniciar sesión como el usuario 'Administrador'
        self.login("juan.perez@example.com", "micontraseña")

        # Acceder a la vista 'createChargeAccountForm'
        self.browser.get(self.live_server_url + '/chargeAccountForm/')

        # Verificar que se muestra el título de la solicitud
        title_element = self.browser.find_element(By.CSS_SELECTOR, '.title')
        self.assertEqual(title_element.text, 'Formulario de Cuenta de cobro')



    def test_contable_cannot_access_create_charge_account_form(self):
        """
        Test that a user with the 'Contable' role cannot access the 'createChargeAccountForm' view
        and the appropriate error message is displayed.
        """
        # Registrar un usuario con el rol 'Contable'
        self.register_user("Juan", "Pérez", "juan.perez@example.com", "Rol object (5)", "micontraseña")

        # Iniciar sesión como el usuario 'Contable'
        self.login("juan.perez@example.com", "micontraseña")

        # Intentar acceder a la vista 'createChargeAccountForm'
        self.browser.get(self.live_server_url + '/chargeAccountForm/')

        # Verificar que se muestra el mensaje de error
        error_modal = self.browser.find_element(By.ID, 'error-modal')
        self.assertTrue(error_modal.is_displayed())

        error_message = error_modal.find_element(By.TAG_NAME, 'p').text
        self.assertEqual(error_message, 'No tienes los permisos requeridos')

    def test_admin_can_access_create_Requisition_Form(self):
        """
        Test that a user with the 'Admin' role can access the 'createRequisitionForm' view.
        """
        # Registrar un usuario con el rol 'Administrador'
        self.register_user("Juan", "Pérez", "juan.perez@example.com", "Rol object (1)", "micontraseña")

        # Iniciar sesión como el usuario 'Solicitante'
        self.login("juan.perez@example.com", "micontraseña")

        # Acceder a la vista 'createRequisitionForm'
        self.browser.get(self.live_server_url + '/requisitionForm/')

        # Verificar que se muestra el título de la solicitud
        title_element = self.browser.find_element(By.CSS_SELECTOR, '.title')
        self.assertEqual(title_element.text, 'Formulario de Requisición')

    def test_solicitante_can_access_create_Requisition_Form(self):
        """
        Test that a user with the 'Solicitante' role can access the 'createRequisitionForm' view.
        """
        # Registrar un usuario con el rol 'Solicitante'
        self.register_user("Juan", "Pérez", "juan.perez@example.com", "Rol object (6)", "micontraseña")

        # Iniciar sesión como el usuario 'Solicitante'
        self.login("juan.perez@example.com", "micontraseña")

        # Acceder a la vista 'createRequisitionForm'
        self.browser.get(self.live_server_url + '/requisitionForm/')

        # Verificar que se muestra el título de la solicitud
        title_element = self.browser.find_element(By.CSS_SELECTOR, '.title')
        self.assertEqual(title_element.text, 'Formulario de Requisición')

    def test_contable_cannot_access_create_Requisition_Form(self):
        """
        Test that a user with the 'Contable' role cannot access the 'createRequisitionForm' view
        and the appropriate error message is displayed.
        """
        # Registrar un usuario con el rol 'Contable'
        self.register_user("Juan", "Pérez", "juan.perez@example.com", "Rol object (5)", "micontraseña")

        # Iniciar sesión como el usuario 'Contable'
        self.login("juan.perez@example.com", "micontraseña")

        # Intentar acceder a la vista 'createRequisitionForm'
        self.browser.get(self.live_server_url + '/requisitionForm/')

        # Verificar que se muestra el mensaje de error
        error_modal = self.browser.find_element(By.ID, 'error-modal')
        self.assertTrue(error_modal.is_displayed())

        error_message = error_modal.find_element(By.TAG_NAME, 'p').text
        self.assertEqual(error_message, 'No tienes los permisos requeridos')

    def test_admin_can_access_create_exterior_paymentForm(self):
        """
        Test that a user with the 'Admin' role can access the 'createExteriorPaymentForm' view.
        """
        # Registrar un usuario con el rol 'Administrador'
        self.register_user("Juan", "Pérez", "juan.perez@example.com", "Rol object (1)", "micontraseña")

        # Iniciar sesión como el usuario 'Administrador'
        self.login("juan.perez@example.com", "micontraseña")

        # Acceder a la vista 'createExteriorPaymentForm'
        self.browser.get(self.live_server_url + '/exteriorPaymentForm/')

        # Verificar que se muestra el título de la solicitud
        title_element = self.browser.find_element(By.CSS_SELECTOR, '.text-wrapper')
        self.assertEqual(title_element.text, 'Formulario de requisición de pago al exterior')

    def test_solicitante_can_access_create_exterior_paymentForm(self):
        """
        Test that a user with the 'Solicitante' role can access the 'createExteriorPaymentForm' view.
        """
        # Registrar un usuario con el rol 'Solicitante'
        self.register_user("Juan", "Pérez", "juan.perez@example.com", "Rol object (6)", "micontraseña")

        # Iniciar sesión como el usuario 'Solicitante'
        self.login("juan.perez@example.com", "micontraseña")

        # Acceder a la vista 'createExteriorPaymentForm'
        self.browser.get(self.live_server_url + '/exteriorPaymentForm/')

        # Verificar que se muestra el título de la solicitud
        title_element = self.browser.find_element(By.CSS_SELECTOR, '.text-wrapper')
        self.assertEqual(title_element.text, 'Formulario de requisición de pago al exterior')
    
    def test_contable_cannot_access_create_exterior_paymentForm(self):
        """
        Test that a user with the 'Contable' role cannot access the 'createExteriorPaymentForm' view
        and the appropriate error message is displayed.
        """
        # Registrar un usuario con el rol 'Contable'
        self.register_user("Juan", "Pérez", "juan.perez@example.com", "Rol object (5)", "micontraseña")

        # Iniciar sesión como el usuario 'Contable'
        self.login("juan.perez@example.com", "micontraseña")

        # Intentar acceder a la vista 'createExteriorPaymentForm'
        self.browser.get(self.live_server_url + '/exteriorPaymentForm/')

        # Verificar que se muestra el mensaje de error
        error_modal = self.browser.find_element(By.ID, 'error-modal')
        self.assertTrue(error_modal.is_displayed())

        error_message = error_modal.find_element(By.TAG_NAME, 'p').text
        self.assertEqual(error_message, 'No tienes los permisos requeridos')

    def test_solicitante_can_access_create_legalization_form(self):
        """
        Test that a user with the 'Solicitante' role can access the 'createLegalizationForm' view.
        """
        # Registrar un usuario con el rol 'Solicitante'
        self.register_user("Juan", "Pérez", "juan.perez@example.com", "Rol object (6)", "micontraseña")

        # Iniciar sesión como el usuario 'Solicitante'
        self.login("juan.perez@example.com", "micontraseña")

        # Acceder a la vista 'createLegalizationForm'
        self.browser.get(self.live_server_url + '/legalizationForm/')

        # Verificar que se muestra el título de la solicitud
        title_element = self.browser.find_element(By.CSS_SELECTOR, '.title-legalization')
        self.assertEqual(title_element.text, 'Formulario de legalización de gastos de viaje')

    def test_admin_can_access_create_legalization_form(self):
        """
        Test that a user with the 'Administrador' role can access the 'createLegalizationForm' view.
        """
        # Registrar un usuario con el rol 'Administrador'
        self.register_user("Juan", "Pérez", "juan.perez@example.com", "Rol object (1)", "micontraseña")

        # Iniciar sesión como el usuario 'Administrador'
        self.login("juan.perez@example.com", "micontraseña")

        # Acceder a la vista 'createLegalizationForm'
        self.browser.get(self.live_server_url + '/legalizationForm/')

        # Verificar que se muestra el título de la solicitud
        title_element = self.browser.find_element(By.CSS_SELECTOR, '.title-legalization')
        self.assertEqual(title_element.text, 'Formulario de legalización de gastos de viaje')

    def test_contable_cannot_access_create_exterior_paymentForm(self):
        """
        Test that a user with the 'Contable' role cannot access the 'createLegalizationForm' view
        and the appropriate error message is displayed.
        """
        # Registrar un usuario con el rol 'Contable'
        self.register_user("Juan", "Pérez", "juan.perez@example.com", "Rol object (5)", "micontraseña")

        # Iniciar sesión como el usuario 'Contable'
        self.login("juan.perez@example.com", "micontraseña")

        # Intentar acceder a la vista 'createLegalizationForm'
        self.browser.get(self.live_server_url + '/legalizationForm/')

        # Verificar que se muestra el mensaje de error
        error_modal = self.browser.find_element(By.ID, 'error-modal')
        self.assertTrue(error_modal.is_displayed())

        error_message = error_modal.find_element(By.TAG_NAME, 'p').text
        self.assertEqual(error_message, 'No tienes los permisos requeridos')

    def test_admin_can_access_create_advance_payment_form(self):
        """
        Test that a user with the 'Administrador' role can access the 'createAdvancePaymentForm' view.
        """
        # Registrar un usuario con el rol 'Administrador'
        self.register_user("Juan", "Pérez", "juan.perez@example.com", "Rol object (1)", "micontraseña")

        # Iniciar sesión como el usuario 'Administrador'
        self.login("juan.perez@example.com", "micontraseña")

        # Acceder a la vista 'createAdvancePaymentForm'
        self.browser.get(self.live_server_url + '/advancePaymentForm/')

        # Verificar que se muestra el título de la solicitud
        title_element = self.browser.find_element(By.CSS_SELECTOR, '.title-advance')
        self.assertEqual(title_element.text, 'Formulario de Solicitud de anticipo para gastos de viaje')

    def test_solicitante_can_access_create_advance_payment_form(self):
        """
        Test that a user with the 'Solicitante' role can access the 'createAdvancePaymentForm' view.
        """
        # Registrar un usuario con el rol 'Solicitante'
        self.register_user("Juan", "Pérez", "juan.perez@example.com", "Rol object (6)", "micontraseña")

        # Iniciar sesión como el usuario 'Solicitante'
        self.login("juan.perez@example.com", "micontraseña")

        # Acceder a la vista 'createAdvancePaymentForm'
        self.browser.get(self.live_server_url + '/advancePaymentForm/')

        # Verificar que se muestra el título de la solicitud
        title_element = self.browser.find_element(By.CSS_SELECTOR, '.title-advance')
        self.assertEqual(title_element.text, 'Formulario de Solicitud de anticipo para gastos de viaje')

    def test_contable_cannot_access_create_exterior_paymentForm(self):
        """
        Test that a user with the 'Contable' role cannot access the 'createAdvancePaymentForm' view
        and the appropriate error message is displayed.
        """
        # Registrar un usuario con el rol 'Contable'
        self.register_user("Juan", "Pérez", "juan.perez@example.com", "Rol object (5)", "micontraseña")

        # Iniciar sesión como el usuario 'Contable'
        self.login("juan.perez@example.com", "micontraseña")

        # Intentar acceder a la vista 'createAdvancePaymentForm'
        self.browser.get(self.live_server_url + '/advancePaymentForm/')

        # Verificar que se muestra el mensaje de error
        error_modal = self.browser.find_element(By.ID, 'error-modal')
        self.assertTrue(error_modal.is_displayed())

        error_message = error_modal.find_element(By.TAG_NAME, 'p').text
        self.assertEqual(error_message, 'No tienes los permisos requeridos')