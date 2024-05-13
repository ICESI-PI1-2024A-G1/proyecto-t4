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

class RegistrationAndLoginTestCase(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)
        self.setup_data()

    def tearDown(self):
        self.browser.quit()

    def setup_data(self):
        self.setup_roles()
        self.setup_states()

    def setup_roles(self):
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

    def setup_states(self):
        # Crea los estados si no existen
        for state, color in State.ESTADOS:
            if not State.objects.filter(state=state).exists():
                mixer.blend(State, state=state, color=color)


    def type_text(self, element, text):
        for char in text:
            element.send_keys(char)
            time.sleep(0.02)  # Espera 0.02 segundos después de cada tecla

    def register_user(self, name, last_name, email, rol, password):
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
        # Registrar e iniciar sesión con un usuario con el rol de "Ventanilla única"
        self.register_user("Ventanilla", "Test", "ventanilla@example.com", "Rol Object (4)", "Unicapass123")
        self.login_as_ventanilla()

        # Navegar hasta la página del formulario "Agregar a ventanilla única"
        self.browser.get(self.live_server_url + '/Agregar a ventanilla única/')  # Corregido el URL

        # Esperar a que aparezcan los campos del formulario
        self.browser.implicitly_wait(5)

       # Identificar y llenar todos los campos del formulario
        creation_date_input = self.browser.find_element(By.ID, 'id_creationDate')
        self.type_text(creation_date_input, "2023-05-12")

        creator_input = self.browser.find_element(By.ID, 'id_creator')
        self.type_text(creator_input, "Dana")

        type_input = self.browser.find_element(By.ID, 'id_type')
        self.type_text(type_input, "Requisicion")

        supplier_input = self.browser.find_element(By.ID, 'id_supplier')
        self.type_text(supplier_input, "Pedro")

        supplier_id_input = self.browser.find_element(By.ID, 'id_supplierId')
        self.type_text(supplier_id_input, "Pedro123")

        document_number_input = self.browser.find_element(By.ID, 'id_documentNumber')
        self.type_text(document_number_input, "1110092846")

        concept_input = self.browser.find_element(By.ID, 'id_concept')
        self.type_text(concept_input, "Financiero")

        supplier_email_input = self.browser.find_element(By.ID, 'id_supplierEmail')
        self.type_text(supplier_email_input, "pedro123@example.com")

        money_type_input = self.browser.find_element(By.ID, 'id_moneyType')
        self.type_text(money_type_input, "USD")

        amount_input = self.browser.find_element(By.ID, 'id_amount')
        self.type_text(amount_input, "1000")

        cenco_input = self.browser.find_element(By.ID, 'id_cenco')
        self.type_text(cenco_input, "50")
        cex_number_input = self.browser.find_element(By.ID, 'id_cexNumber')
        self.type_text(cex_number_input, "Cex102")

        observations_input = self.browser.find_element(By.ID, 'id_observations')
        self.type_text(observations_input, "Ninguna")

        current_state_select = Select(self.browser.find_element(By.ID, 'id_currentState'))
        current_state_select.select_by_visible_text("Aprobado")


        close_date_input = self.browser.find_element(By.ID, 'id_closeDate')
        self.type_text(close_date_input, "2023-05-12")

        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'static', 'mediaTest', 'A.docx'))
        file_field = self.browser.find_element(By.ID, 'id_file')  # Define el campo del archivo
        file_field.send_keys(file_path)  # Envía la ruta del archivo al campo del archivo

        submit_button = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.ID, 'submit_button_id'))
            )
            # Realizar clic utilizando JavaScript
        self.browser.execute_script("arguments[0].click();", submit_button)

        # Esperar un poco para que la página se actualice
        time.sleep(5)

        # Esperar a que aparezca la notificación de envío exitoso
        wait = WebDriverWait(self.browser, 15)
        success_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.alert.alert-success')))