from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from SistemaContableApp.models import Rol, User
from selenium.webdriver.common.by import By
from mixer.backend.django import mixer
from selenium import webdriver
import time
import os
from SistemaContableApp.models import State
from selenium.webdriver.support.select import Select

class FormTestCase(StaticLiveServerTestCase):
    def setUp(self):
        """
        Set up the test environment before each test case.

        This method initializes the web driver, sets an implicit wait of 5 seconds,
        and sets up any necessary test data.
        """
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)
        self.setup_data()

    def tearDown(self):
        """
        This method is called after each test case is executed to perform any necessary clean-up actions.
        It quits the browser instance.
        """
        self.browser.quit()

    def setup_data(self):
        """
        Sets up the data required for testing.

        This method calls the setup_roles() and setup_states() methods to initialize the necessary roles and states.
        """
        self.setup_roles()
        self.setup_states()

    def setup_roles(self):
        """
        Sets up the roles if they don't already exist.

        This method checks if the roles 'Administrador', 'Líder', 'Gestor', 'Ventanilla única', and 'Contable' exist in the database.
        If any of these roles do not exist, they are created using the mixer.blend() function from the mixer library.
        """
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

    def setup_states(self):
        """
        Sets up the states if they don't already exist.

        This method iterates over the `ESTADOS` list in the `State` class and creates
        new state objects if they don't already exist in the database.

        Args:
            None

        Returns:
            None
        """
        for state, color in State.ESTADOS:
            if not State.objects.filter(state=state).exists():
                mixer.blend(State, state=state, color=color)


    def type_text(self, element, text):
        """
        Types the given text into the specified element.

        Args:
            element: The element to type the text into.
            text: The text to be typed.

        Returns:
            None
        """
        for char in text:
            element.send_keys(char)
            time.sleep(0.02)  # Wait for 0.02 seconds after each key

    def register_user(self, name, last_name, email, rol, password):
        """
        Registers a user with the provided information.

        Args:
            name (str): The user's name.
            last_name (str): The user's last name.
            email (str): The user's email address.
            rol (str): The user's role.
            password (str): The user's password.

        Returns:
            None
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

    def login_as_ventanilla(self):
        """
        Logs in as a 'ventanilla' user.

        This method opens the login page, fills in the login form with the 'ventanilla' user credentials,
        and submits the form. It then waits for the page to refresh.

        Args:
            None

        Returns:
            None
        """
        # Abre la página de inicio de sesión
        self.browser.get(self.live_server_url)

        # Encuentra los campos del formulario de inicio de sesión
        username_input = self.browser.find_element(By.NAME, 'email')
        password_input = self.browser.find_element(By.NAME, 'password')

        # Llena el formulario con los datos de inicio de sesión
        self.type_text(username_input, "ventanilla@example.com")
        self.type_text(password_input, "Unicapass123")

        # Envía el formulario de inicio de sesión
        submit_button = self.browser.find_element(By.CSS_SELECTOR, '.btn')
        submit_button.click()

        # Espera un poco para que la página se actualice
        time.sleep(5)

    def test_onestopshop_form(self):
        """
        Test case for submitting the one-stop shop form.

        Steps:
        1. Register and login as a user with the role of "Ventanilla única".
        2. Navigate to the "Agregar a ventanilla única" form page.
        3. Fill in all the form fields.
        4. Submit the form.
        5. Wait for the success notification to appear.

        This test case verifies that the form can be successfully submitted and the success notification is displayed.

        Returns:
            None
        """
        # Registrar e iniciar sesión con un usuario con el rol de "Ventanilla única"
        self.register_user("Ventanilla", "Test", "ventanilla@example.com", "Ventanilla única", "Unicapass123")
        self.login_as_ventanilla()

        # Navegar hasta la página del formulario "Agregar a ventanilla única"
        self.browser.get(self.live_server_url + '/Agregar a ventanilla única/')  # Corregido el URL

        # Esperar a que aparezcan los campos del formulario
        self.browser.implicitly_wait(5)

        # Identificar y llenar todos los campos del formulario
        creation_date_input = self.browser.find_element(By.ID, 'id_creationDate')
        self.type_text(creation_date_input, "2023-05-12")

