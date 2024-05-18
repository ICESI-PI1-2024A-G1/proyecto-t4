from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class RegistrationAndLoginTestCase(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()  # O el navegador que prefieras
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def type_text(self, element, text):
        for char in text:
            element.send_keys(char)
            time.sleep(0.02)  # Espera 0.1 segundos después de cada tecla

    def test_registro_e_inicio_sesion(self):
        # Abre la página de registro
        self.browser.get(self.live_server_url + '/registro/')

        # Encuentra los campos del formulario de registro
        name_input = self.browser.find_element(By.ID, 'id_name')
        last_name_input = self.browser.find_element(By.ID, 'id_last_name')
        email_input = self.browser.find_element(By.ID, 'id_email')
        rol_select = self.browser.find_element(By.ID, 'id_rol')
        password1_input = self.browser.find_element(By.ID, 'id_password1')
        password2_input = self.browser.find_element(By.ID, 'id_password2')

        # Llena el formulario con datos de prueba
        self.type_text(name_input, "Pepito")
        self.type_text(last_name_input, "Perez")
        self.type_text(email_input, "usuariosolicitante0@gmail.com")
        rol_select.send_keys("1")
        self.type_text(password1_input, "Pindy000")
        self.type_text(password2_input, "Pindy000")

        # Envía el formulario de registro
        submit_button = self.browser.find_element(By.CSS_SELECTOR, '.btn')
        submit_button.click()

        # Espera un poco para que la página se actualice
        time.sleep(3)

        # Verifica si se ha registrado correctamente
        self.assertIn('Tu cuenta ha sido creada exitosamente.', self.browser.page_source)
        self.assertIn('Registro exitoso.', self.browser.page_source)

        # Abre la página de inicio de sesión
        self.browser.get(self.live_server_url)

        # Encuentra los campos del formulario de inicio de sesión
        username_input = self.browser.find_element(By.NAME, 'email')
        password_input = self.browser.find_element(By.NAME, 'password')

        # Llena el formulario con los datos de inicio de sesión
        self.type_text(username_input, "usuariosolicitante0@gmail.com")
        self.type_text(password_input, "Pindy000")

        # Envía el formulario de inicio de sesión
        submit_button = self.browser.find_element(By.CSS_SELECTOR, '.btn')
        submit_button.click()

        # Espera un poco para que la página se actualice
        time.sleep(5)

        # Verifica si se ha iniciado sesión correctamente
        self.assertIn('Bienvenido al sistema contable', self.browser.page_source)